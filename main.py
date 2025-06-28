import speech_recognition as sr
import requests
import pyttsx3
import logging
import dotenv
import os
import keyboard
import json

# Load environment variables
dotenv.load_dotenv('.env')
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Logging setup
logging.basicConfig(filename='assistant.log', level=logging.INFO)

def listen_while_hotkey(hotkey='space'):
    r = sr.Recognizer()
    mic = sr.Microphone()
    print(f"Hold '{hotkey}' to speak...")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = None
        while True:
            if keyboard.is_pressed(hotkey):
                print("Listening...")
                audio = r.listen(source, phrase_time_limit=10)
                print("Processing...")
                break
    try:
        return r.recognize_google(audio, language="pt-BR")
    except Exception as e:
        print(f"Erro ao reconhecer áudio: {e}")
        logging.error(f"Erro ao reconhecer áudio: {e}")
        return None

def call_open_router(text, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": f"{json.load(open('config.json'))['model']}",
        "messages": [{"role": "user", "content": text}]
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Erro na API: {e}")
        logging.error(f"Erro na API: {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    if not API_KEY:
        print("API key not found. Please set OPENROUTER_API_KEY in your .env file.")
        exit(1)
    while True:
        print("Ready. Hold the hotkey to speak (press ESC to exit).")
        if keyboard.is_pressed('esc'):
            print("Exiting assistant.")
            break
        query = listen_while_hotkey('space')
        if query:
            print(f"Você disse: {query}")
            response = call_open_router(query, API_KEY)
            if response:
                print(f"Resposta: {response}")
                speak(response)
                logging.info(f"Q: {query} | A: {response}")