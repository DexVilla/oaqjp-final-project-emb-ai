from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Recibe el texto del usuario, lo analiza y devuelve 
    una frase con los resultados en el formato requerido.
    """
    # Punto 2: Recibir el texto a analizar
    text_to_analyze = request.args.get('textToAnalyze')

    # Ejecutar la función de detección de emociones
    response = emotion_detector(text_to_analyze)

    # Extraer los valores del diccionario de respuesta
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Manejo en caso de que la entrada sea inválida o nula
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Punto 3: Retornar la respuesta en el formato de cadena (String) solicitado
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Punto 4 inicial: Ejecutar en el puerto 5000
    app.run(host="0.0.0.0", port=5000)