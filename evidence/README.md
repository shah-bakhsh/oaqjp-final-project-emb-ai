# Final project — evidence checklist

Capture genuine terminal output and screenshots from the Skills Network Theia lab. Do not submit offline mock responses as live Watson results.

## Option 1: AI-graded (16 points)

- Task 1: Public README link, containing the exact title "Final project": https://github.com/shah-bakhsh/oaqjp-final-project-emb-ai/blob/main/README.md
- Task 2A: Code from EmotionDetection/emotion_detection.py defining emotion_detector (initial request logic).
- Task 2B: Terminal import and live result for "I love this new technology."
- Task 3A: Code with five emotion scores and dominant_emotion formatted as a dictionary.
- Task 3B: Theia terminal output for "I am so happy I am doing this" (dominant: joy).
- Task 4A: Public package import file link: https://github.com/shah-bakhsh/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
- Task 4B: Theia terminal output importing the package, then testing "I hate working long hours" (dominant: anger).
- Task 5A: Source code from test_emotion_detection.py containing all five required statements.
- Task 5B: Theia output showing all five live unit tests passed.
- Task 6A: server.py code showing the Flask root and /emotionDetector routes.
- Task 6B: 6b_deployment_test.png with successful application output for "I think I am having fun".
- Task 7A: emotion_detection.py code handling HTTP status code 400 with six None values.
- Task 7B: server.py code displaying "Invalid text! Please try again!" on invalid input.
- Task 7C: 7c_error_handling_interface.png from the deployed UI showing the actual error message.
- Task 8A: final server.py with docstrings and Pylint-friendly formatting.
- Task 8B: actual Theia pylint server.py output demonstrating 10.00/10.

## Option 2: peer-graded screenshot names

- Task 1: 1_folder_structure.png
- Task 2: 2a_emotion_detection.png, 2b_application_creation.png
- Task 3: 3a_output_formatting.png, 3b_formatted_output_test.png
- Task 4: 4a_packaging.png, 4b_packaging_test.png
- Task 5: 5a_unit_testing.png, 5b_unit_testing_result.png
- Task 6: 6a_server.png, 6b_deployment_test.png
- Task 7: 7a_error_handling_function.png, 7b_error_handling_server.png, 7c_error_handling_interface.png
- Task 8: 8a_server_modified.png, 8b_static_code_analysis.png

## Saving work

The lab environment is not persistent. Commit and push changes after tasks, and download evidence screenshots before closing Theia.

    git add .
    git commit -m "Complete IBM Watson NLP final project"
    git push origin main
