# 🟣 Tourmaline — Local Voice-Driven AI Assistant

<p align="left">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" alt="Python"></a>
  <a href="https://openrouter.ai/"><img src="https://img.shields.io/badge/OpenRouter-API-brightgreen?logo=openai" alt="OpenRouter"></a>
  <a href="https://pypi.org/project/pyttsx3/"><img src="https://img.shields.io/badge/TTS-pyttsx3-orange" alt="TTS"></a>
</p>

**Tourmaline** is a Python-based voice assistant that captures your speech, transcribes it to text, sends the query to an LLM via the [OpenRouter](https://openrouter.ai) API, and speaks the AI's response aloud via TTS — all triggered by a simple **hotkey**.

Ideal for hands-free prompts, accessibility use-cases, or desktop automation with a human-like interface.

> ⚠️ **Disclaimer**  
> This project is intended for **educational** and **personal productivity** purposes. It makes use of voice input and TTS output via local system libraries, and queries OpenRouter via your API key. Please use responsibly and ensure you comply with the terms of service of OpenRouter and any LLM providers you use.

---

## ✨ Features

- 🎙️ Voice-to-text capture using your microphone
- 🔗 Sends transcribed prompt to any LLM via OpenRouter API
- 🗣️ Responds using local text-to-speech (TTS)
- ⌨️ Triggered by a global hotkey (e.g. `Ctrl+Alt+T`)
- 📦 Minimal Python-based stack, fully local except for LLM query

---

## 🛠 Requirements

- Python 3.9+
- Microphone input device
- `pyttsx3`, `speechrecognition`, `keyboard`, `requests`
- [OpenRouter API key](https://openrouter.ai/)
- Optional: `python-dotenv` for `.env` file support

---

## 📦 Installation

```bash
git clone https://github.com/naranjii/tourmaline-ai-assistant.git
cd tourmaline-ai-assistant
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔧 Configuration

You must provide your **OpenRouter API key**. You can either:

- Export it via environment variable:

```bash
export OPENROUTER_API_KEY="your_key_here"
```

- Or use a `.env` file (if supported in the code):

```
OPENROUTER_API_KEY=your_key_here
```

You can customize:
- The **hotkey** for voice activation
- The **OpenRouter model ID** (e.g. `openai/gpt-4`, `mistralai/mistral-7b`)
- TTS voice and speech rate (via `pyttsx3` config in code)

---

## 🚀 Usage

Start the assistant:

```bash
python tourmaline.py
```

Press the configured hotkey → speak your query → hear the AI's response.

Example interaction:

```text
[You]  → “Summarize the latest AI safety paper by Anthropic.”
[AI]   → “Sure. The paper highlights interpretability, adversarial robustness, and scalable oversight as core priorities...”
```

---

## 🧠 How It Works

1. Waits for hotkey (e.g. `Ctrl+Alt+T`)
2. Activates microphone and transcribes your speech via `speech_recognition`
3. Sends prompt to OpenRouter API
4. Receives model response
5. Speaks response using `pyttsx3`

---

## 🗂 File Structure

```
tourmaline-ai-assistant/
├── tourmaline.py           # Main script
├── requirements.txt
├── .env                    # Optional (for API key)
└── README.md
```

---

## 🚧 To-do

- [ ] Add whisper or Vosk as offline STT backend
- [ ] Integrate faster TTS (edge-tts, gTTS, etc.)
- [ ] Add memory / context window
- [ ] Optional GUI overlay
- [ ] Multi-platform hotkey compatibility

---

## 🛡 License

MIT License. See [`LICENSE`](./LICENSE) for more.

---

## 👨‍💻 Author

Created by [@naranjii](https://github.com/naranjii) — feedback and contributions welcome!
