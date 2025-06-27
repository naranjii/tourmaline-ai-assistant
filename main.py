# main.py
import speech_recognition as sr
import requests
import json
import pyttsx3
import logging

api_key = json.load(open('.env'))['OPENROUTER_API_KEY']

# Configuração do logging
logging.basicConfig(filename='assistant.log', level=logging.INFO)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {text}")
        return text
    except Exception as e:
        logging.error(f"Erro no STT: {e}")
        return None

def call_open_router(text, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Altere para o modelo desejado
        "messages": [{"role": "user", "content": text}]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        logging.error(f"Erro na API: {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    API_KEY = "SUA_API_KEY_AQUI"  # Substitua pela sua chave
    query = listen()
    if query:
        response = call_open_router(query, API_KEY)
        if response:
            print(f"Resposta: {response}")
            speak(response)
            logging.info(f"Q: {query} | A: {response}")