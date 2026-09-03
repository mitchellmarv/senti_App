import random
from textblob import TextBlob
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title('¡Ánimo Vaquero!')

image = Image.open('emotions.jfif')
st.image(image)

st.subheader("Por favor escribe en el campo de texto cómo te sientes")

translator = Translator()

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write(
        """
        Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral.
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

        Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
        """
    )

# Frases de ánimo para cuando se detecta un sentimiento negativo
frases_animo = [
    "Recuerda que cada día trae una nueva oportunidad para sonreír. ¡Tú puedes! 💪",
    "No estás solo/a en esto, los momentos difíciles también pasan. ¡Ánimo! 🌈",
    "Eres más fuerte de lo que crees. ¡Sigue adelante! ✨",
    "Respira profundo, todo va a estar bien. Cree en ti mismo/a 🌻",
    "Hoy es un buen día para darte una pausa y cuidarte un poco más 💛",
]

with st.expander('Analizar cómo te sientes'):
    text = st.text_input('Escribe por favor: ')
    if text:
        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        polaridad = round(blob.sentiment.polarity, 2)
        subjetividad = round(blob.sentiment.subjectivity, 2)

        st.write('Polarity: ', polaridad)
        st.write('Subjectivity: ', subjetividad)

        if polaridad > 0.0:
            st.write('¡Muy bien! Se nota un sentimiento positivo 😊 ¡Sigue así!')
        elif polaridad == 0.0:
            st.write('Tu ánimo parece neutral 😐 Podrías intentar hacer algo que te haga sentir mejor.')
        else:
            frase = random.choice(frases_animo)
            st.write(frase)
            st.write('Aquí tienes algo que puede sacarte una sonrisa 😔➡️😊')
            gif = Image.open('Showtime.gif')
            st.image(gif)
