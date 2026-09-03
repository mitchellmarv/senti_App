import random
from textblob import TextBlob
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title('¡Ánimo Vaquero! Estoy aquí para escuchar tus pensamientos.')

image = Image.open('therapist.jpg')
st.image(image)

st.subheader("Por favor escribe en el campo de texto cómo te sientes")

translator = Translator()

with st.sidebar:
    st.subheader("¿Cómo funciona esta herramienta?")
    st.write(
        """
        Esta herramienta analiza lo que escribes para identificar cómo te sientes.

        Si detecta un sentimiento positivo, te felicitará y te animará a seguir así.

        Si detecta un sentimiento neutral, te dará un pequeño empujón para
        ayudarte a mejorar tu ánimo.

        Y si detecta un sentimiento negativo, te mostrará una frase de ánimo
        junto con un gif para sacarte una sonrisa 💛
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

# Frases de ánimo para cuando se detecta un sentimiento neutral
frases_animo_neutral = [
    "Un pequeño paseo o una buena canción pueden mejorar tu día 🎶",
    "¿Qué tal si te tomas un momento para hacer algo que disfrutes? 🌤️",
    "A veces basta un pequeño gesto contigo mismo/a para sentirte mejor 🙂",
    "Sonríe un poco, ¡seguro que hoy también pasan cosas buenas! 😊",
    "Regálate un momento de calma, te lo mereces 💛",
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
            frase = random.choice(frases_animo_neutral)
            st.write('Tu ánimo parece neutral 😐')
            st.write(frase)
        else:
            frase = random.choice(frases_animo)
            st.write(frase)
            st.write('¡Aquí tienes algo que puede sacarte una sonrisa, baila con el perro!')
            st.image('epico.gif')
