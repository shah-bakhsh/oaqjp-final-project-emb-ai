"""Analyze text emotions using the Skills Network Watson NLP endpoint."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return all six required fields with None values for invalid text."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze):
    """Predict five emotion scores and the strongest emotion in the text.

    Return a dictionary containing all five scores and dominant_emotion.
    An empty input or a Watson HTTP 400 response returns six None values.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    response = requests.post(
        WATSON_URL,
        headers=WATSON_HEADERS,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=20,
    )

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    response_dictionary = response.json()
    emotion_scores = response_dictionary["emotionPredictions"][0]["emotion"]
    result = {emotion: emotion_scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(EMOTIONS, key=result.get)
    return result
