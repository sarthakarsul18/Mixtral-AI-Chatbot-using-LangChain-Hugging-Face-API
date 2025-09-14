# 🤖 Mixtral AI Chatbot

An **AI-powered conversational chatbot** built using **LangChain**, **Hugging Face API** (`Mixtral-8x7B-Instruct`), and **Streamlit** — featuring tone control, quick-reply buttons, emoji reactions, and real-time cloud-based responses without downloading models locally.

---

## 🚀 Features
- 🌐 **Cloud-based AI** using Hugging Face API — no local model setup required.
- 🎭 **Tone Control** — Switch between *Friendly* and *Professional* responses.
- ⚡ **Quick Replies** — Predefined questions for instant interaction.
- 😀 **Emoji Reactions** — Fun, dynamic bot responses.
- ⏳ **Typing Animation** — Simulated real-time typing for natural UX.
- 🛡 **Secure API Integration** — `.env` for storing API keys safely.
- 📂 **Modular Code** — Clean separation of backend (`chatbot.py`) and frontend (`app.py`).

---

## 🛠 Tech Stack
- **Python 3.9+**
- [LangChain](https://www.langchain.com/)
- [Hugging Face API](https://huggingface.co/)
- [Streamlit](https://streamlit.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Installation & Setup

1️⃣ **Clone the repository**
```bash
git clone https://github.com/sarthakarsul18/Mixtral-AI-Chatbot-using-LangChain-Hugging-Face-API
```
```
cd Mixtral-AI-Chatbot-using-LangChain-Hugging-Face-API
```

2️⃣ **Install dependencies**
```
pip install -r requirements.txt
```
3️⃣ **Add your Hugging Face API Key**

```
HF_TOKEN=your_huggingface_api_key_here
```
4️⃣ **Run the app**
```
streamlit run app.py
```
**📜 License**

This project is licensed under the MIT License — feel free to use and modify.
