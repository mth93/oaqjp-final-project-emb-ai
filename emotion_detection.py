import requests
import json

def emotion_detector(text_to_analyze):
    """
    Performs emotion detection on text using the Watson NLP API.

    Args:
        text_to_analyze (str): The text to be analyzed.

    Returns:
        str: The raw text response from the API.
    """
    
    # URL for the Watson NLP Emotion Predict endpoint.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers to specify the model for emotion analysis.
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Construct the JSON payload with the text to analyze.
    json_payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Send the POST request to the API.
        response = requests.post(url, json=json_payload, headers=headers)
        
        # Check if the request was successful (status code 200).
        if response.status_code == 200:
            # Return the raw text of the response, as specified in the task description.
            return response.text
        else:
            # Handle unsuccessful responses.
            return None
            
    except requests.exceptions.RequestException:
        # Handle network-related errors.
        return None
