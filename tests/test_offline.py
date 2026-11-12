"""Local, mocked tests that do not require access to the IBM lab network."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector
from server import app

EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


class TestOffline(unittest.TestCase):
    """Verify result structure, HTTP 400 handling and Flask responses."""

    def setUp(self):
        """Create Flask's built-in testing client."""
        self.client = app.test_client()

    def _mock_response(self, dominant):
        """Create a successful mock emotion prediction for an emotion."""
        scores = dict.fromkeys(EMOTIONS, 0.01)
        scores[dominant] = 0.90
        response = Mock(status_code=200)
        response.json.return_value = {"emotionPredictions": [{"emotion": scores}]}
        return response

    def test_five_emotions_are_mapped_correctly(self):
        """Check all five score keys and dominant scores."""
        for emotion in EMOTIONS:
            with self.subTest(emotion=emotion):
                with patch("EmotionDetection.emotion_detection.requests.post") as post:
                    post.return_value = self._mock_response(emotion)
                    result = emotion_detector("A test sentence")
                    self.assertEqual(result["dominant_emotion"], emotion)
                    self.assertEqual(set(result), set(EMOTIONS) | {"dominant_emotion"})
                    self.assertEqual(result[emotion], 0.90)

    def test_empty_input_returns_six_none_values(self):
        """Blank text returns None without making an HTTP call."""
        with patch("EmotionDetection.emotion_detection.requests.post") as post:
            result = emotion_detector("   ")
            self.assertTrue(all(value is None for value in result.values()))
            post.assert_not_called()

    def test_400_returns_six_none_values(self):
        """HTTP 400 from Watson is treated as invalid text."""
        with patch("EmotionDetection.emotion_detection.requests.post") as post:
            post.return_value = Mock(status_code=400)
            result = emotion_detector("invalid")
            self.assertTrue(all(value is None for value in result.values()))

    def test_flask_root_page(self):
        """Flask serves IBM's existing HTML page successfully."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"NLP - Emotion Detection", response.data)

    def test_flask_invalid_text_message(self):
        """Blank input is visible with the starter JavaScript (HTTP 200)."""
        response = self.client.get("/emotionDetector?textToAnalyze=")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Invalid text! Please try again!")

    def test_flask_success_message(self):
        """Flask displays the five expected emotion scores."""
        with patch("server.emotion_detector") as detector:
            detector.return_value = {
                "anger": 0.01,
                "disgust": 0.01,
                "fear": 0.01,
                "joy": 0.90,
                "sadness": 0.01,
                "dominant_emotion": "joy",
            }
            response = self.client.get("/emotionDetector?textToAnalyze=good")
            self.assertEqual(response.status_code, 200)
            self.assertIn("dominant emotion is joy", response.get_data(as_text=True))

    def test_watson_post_contract(self):
        """Use the exact Skills Network Watson URL, header and JSON structure."""
        with patch("EmotionDetection.emotion_detection.requests.post") as post:
            post.return_value = self._mock_response("joy")
            emotion_detector("example")
            args, kwargs = post.call_args
            self.assertEqual(len(args), 1)
            self.assertIn("/NlpService/EmotionPredict", args[0])
            self.assertEqual(kwargs["headers"]["grpc-metadata-mm-model-id"],
                             "emotion_aggregated-workflow_lang_en_stock")
            self.assertEqual(kwargs["json"], {"raw_document": {"text": "example"}})


if __name__ == "__main__":
    unittest.main()
