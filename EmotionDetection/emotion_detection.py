import requests
import json

def emotion_detector(text_to_analyze):
    """
    Performs emotion detection on text using the Watson NLP API.

    Args:
        text_to_analyze (str): The text to be analyzed.

    Returns:
        dict: A dictionary of detected emotions and their scores, including the dominant emotion.
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
            # Parse the JSON response.
            formatted_response = json.loads(response.text)
            
            # Extract the dictionary of emotion scores.
            emotion_data = formatted_response['emotionPredictions'][0]['emotion']
            
            # Find the dominant emotion.
            dominant_emotion = max(emotion_data, key=emotion_data.get)
            
            # Prepare the output dictionary in the requested format.
            output_format = {
                'anger': emotion_data['anger'],
                'disgust': emotion_data['disgust'],
                'fear': emotion_data['fear'],
                'joy': emotion_data['joy'],
                'sadness': emotion_data['sadness'],
                'dominant_emotion': dominant_emotion
            }
            
            # Return the dictionary.
            return output_format
        else:
            # Handle unsuccessful responses.
            return None
            
    except requests.exceptions.RequestException:
        # Handle network-related errors.
        return None
