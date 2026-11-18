"""Flask web application for IBM Watson NLP emotion detection."""

import requests
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Display the original IBM emotion detection interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Read textToAnalyze and return an emotion summary or an error."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    try:
        result = emotion_detector(text_to_analyze)
    except requests.RequestException:
        app.logger.exception("Unable to contact the Watson NLP service")
        return "Emotion detection service unavailable. Please try again later.", 503
    except (KeyError, ValueError, IndexError, TypeError):
        app.logger.exception("Watson NLP response could not be parsed")
        return "Emotion detection service returned an invalid response.", 502

    # Return HTTP 200 for invalid input so the browser displays the message.
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
