from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the main index.html page for the web application.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint for emotion detection.
    Receives text from the client, analyzes it for emotions,
    and returns a formatted string response.
    """
    # Get the text to analyze from the request's query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Check for empty or invalid input
    if not text_to_analyze:
        return "Invalid text. Please provide some text to analyze."

    # Call the emotion_detector function to get the analysis result
    response = emotion_detector(text_to_analyze)
    
    # Check if the response from the emotion_detector is valid
    if response is None:
        return "Error: Could not get a valid response from the emotion detection service."

    # Format the output string as per the task requirements
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return formatted_output

if __name__ == "__main__":
    # Run the application on localhost with port 5000
    app.run(port=5000)
