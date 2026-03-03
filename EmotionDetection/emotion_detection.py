import requests
import json

def emotion_detector(text_to_analyze):
    # Esta URL debe ser exacta. Asegúrate de que no tenga espacios extra.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Estos encabezados son CRÍTICOS. Si falta uno, Watson devuelve None (Error 400)
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # El cuerpo de la petición
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    # Convertimos la respuesta a diccionario
    formatted_response = json.loads(response.text)

    # Si la respuesta es exitosa (200)
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        emotion_list = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_list, key=emotion_list.get)
        
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    # Si Watson falla (400, 500, etc.), devolvemos None
    else:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }