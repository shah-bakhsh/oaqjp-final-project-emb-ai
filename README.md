# Final Project

IBM Skills Network final assessment: Emotion Detection using Watson NLP and Flask.

## Overview

This Python web application accepts text, calls the course-hosted Watson NLP EmotionPredict endpoint, and displays scores for anger, disgust, fear, joy, and sadness, together with the dominant emotion.

This repository is a fork of the official IBM starter project. The original templates/index.html and static/mywebscript.js files have been preserved unchanged as required by the course.

## Project layout

- EmotionDetection/__init__.py: exports the emotion_detector function
- EmotionDetection/emotion_detection.py: Watson NLP request, output formatting, HTTP 400 handling
- server.py: Flask application with / and /emotionDetector routes and blank-input handling
- test_emotion_detection.py: five course-required live integration unit tests
- tests/test_offline.py: offline mock tests for GitHub Codespaces and normal development
- requirements.txt: Python dependencies
- evidence/README.md: instructions and exact filenames for assessment evidence
- templates/index.html and static/mywebscript.js: IBM starter interface, unchanged

## Skills Network Theia Lab: REQUIRED for actual Watson tests

The Watson service is hosted on the Skills Network platform and, as stated by the course, is only accessible within the Skills Network Theia Lab. GitHub Codespaces is suitable for reviewing, editing, committing and running offline tests, but NOT as a substitute for the live Watson tests and screenshots required for assessment.

Clone this public fork in the Theia terminal:

    mkdir final_project
    git clone https://github.com/shah-bakhsh/oaqjp-final-project-emb-ai.git final_project
    cd final_project

Install needed Python packages as permitted by the lab:

    python3 -m pip install -r requirements.txt

Check Watson access and formatting:

    python3 -c "from EmotionDetection import emotion_detector; print(emotion_detector('I am so happy I am doing this'))"

Run the FIVE real Watson tests in Theia:

    python3 -m unittest -v test_emotion_detection

Perform static analysis:

    pylint server.py

Start Flask:

    python3 server.py

Visit localhost:5000 (or the Skills Network lab's port-5000 preview). Enter "I think I am having fun" and capture 6b_deployment_test.png. Then clear the text field, submit, verify "Invalid text! Please try again!" and capture 7c_error_handling_interface.png.

## GitHub Codespaces: offline checks only

    python3 -m pip install -r requirements.txt
    python3 -m unittest discover -s tests -v
    python3 -m compileall -q EmotionDetection server.py test_emotion_detection.py
    pylint server.py

The course tests in test_emotion_detection.py deliberately call the live Watson endpoint. They cannot be considered passing until executed in Theia.

## Submission

Use the GitHub links for Task 1 and Task 4:

- Task 1: https://github.com/shah-bakhsh/oaqjp-final-project-emb-ai/blob/main/README.md
- Task 4: https://github.com/shah-bakhsh/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py

See evidence/README.md for the remaining 14 grading items. Save authentic screenshots and terminal output in Theia; do not submit mock outputs as real API results.

## Saving progress

The Theia lab may reset. Commit and push changes or download screenshots before leaving:

    git add .
    git commit -m "Finalize IBM Emotion Detection course project"
    git push origin main
