import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Prueba 1: joy
        resultado_1 = emotion_detector("I am glad this happened")
        self.assertEqual(resultado_1['dominant_emotion'], 'joy')
        
        # Prueba 2: anger
        resultado_2 = emotion_detector("I am really mad about this")
        self.assertEqual(resultado_2['dominant_emotion'], 'anger')
        
        # Prueba 3: disgust
        resultado_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(resultado_3['dominant_emotion'], 'disgust')
        
        # Prueba 4: sadness
        resultado_4 = emotion_detector("I am so sad about this")
        self.assertEqual(resultado_4['dominant_emotion'], 'sadness')
        
        # Prueba 5: fear
        resultado_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(resultado_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()