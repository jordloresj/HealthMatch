import streamlit as st
from openai import OpenAI
import dotenv
import os
import re

OpenAI.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def generate_diag(words):
    # Generar el prompt
    prompt = f"Basado en la siguiente lista de síntomas introducidos por un usuario, \
    analiza y determina cuál o cuáles especialistas médicos serían los más adecuados para tratar su caso. \
    Los síntomas son:{words}. Solo entrega los nombres de las especialidades médicas verificando que estas existan y se llamen de esta forma, \
    señalandolo de la forma: \
    'La especialidad medica [nombre1] y [nombre2] son las más adecuadas para tratar su caso.'"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
         ]
    )
        
    # Obtener la respuesta
    answer = response.choices[0].message.content
    return answer


def main():
    col1, col2 = st.columns([1, 7]) 
    
    with col1:
        st.image("./icon.webp", width=80)

    with col2:
        st.title("HealthMatch")    
    st.header("Tu asistente en la busqueda de especialistas médicos")
    st.subheader("Este asistente te ayudará a encontrar el especialista médico adecuado para tratar tus síntomas.")

    words = st.text_input("Ingresa tus sintomas separados por comas: ")
    
    if st.button("Busca mi especialista"):
        specialists = generate_diag(words)
        st.write(specialists)

if __name__ == "__main__":
    main() 
