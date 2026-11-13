/** Submit text to Flask and display a result or a visible error message. */
function RunSentimentAnalysis() {
    const input = document.getElementById("textToAnalyze");
    const output = document.getElementById("system_response");
    if (!input || !output) {
        return;
    }

    output.textContent = "Analyzing...";
    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState !== 4) {
            return;
        }
        if (this.status === 200) {
            output.textContent = this.responseText;
        } else if (this.status === 503) {
            output.textContent =
                "Watson NLP is unavailable. For live emotion detection, " +
                "run this project inside the IBM Skills Network Theia Lab. " +
                (this.responseText || "");
        } else {
            output.textContent =
                this.responseText ||
                `Emotion detection failed (HTTP ${this.status}). Check the Flask terminal.`;
        }
    };

    xhttp.onerror = function () {
        output.textContent = "Cannot reach the Flask server. Check that port 5000 is running.";
    };

    xhttp.ontimeout = function () {
        output.textContent = "The emotion detection request timed out. Please try again.";
    };

    xhttp.timeout = 30000;
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(input.value), true);
    xhttp.send();
}
