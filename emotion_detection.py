import requests

def emotion_detector(text_to_analyze):
    # 1. Definimos la URL (¡Ojo! Verifica en tu pantalla si hay algo más después de "NlpService" deslizando a la derecha)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # 2. Definimos los Headers (cabeceras) que nos pide la instrucción
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # 3. Definimos el formato del JSON de entrada
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # 4. Hacems la petición POST usando la librería requests
    response = requests.post(url, headers=headers, json=input_json)
    
    # 5. Por ahora, simplemente retornamos el texto de la respuesta para ver qué nos devuelve Watson
    return response.text