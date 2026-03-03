import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.casemix.cloud/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Este es el header oficial para este modelo de Watson
    header = {"grpc-metadata-mm-model-id": "emotion_integrated-v1-aggregator-prediction"}
    
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, json=myobj, headers=header)
        
        # Si el texto es vacío, Watson suele devolver 400
        if response.status_code == 400:
            return {
                'anger': None, 'disgust': None, 'fear': None, 
                'joy': None, 'sadness': None, 'dominant_emotion': None
            }

        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions['anger'], 'disgust': emotions['disgust'],
            'fear': emotions['fear'], 'joy': emotions['joy'],
            'sadness': emotions['sadness'], 'dominant_emotion': dominant_emotion
        }

    except Exception:
        # Si falla la conexión o el host no resuelve
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }