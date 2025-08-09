from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os

# Load API key
load_dotenv()

def get_chatbot():
    """
    Create and return a Hugging Face API-based chatbot model.
    """
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
        task="text-generation",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        temperature=0.7,
        max_new_tokens=256
    )
    return ChatHuggingFace(llm=llm)

def get_response(prompt: str, tone: str = "Friendly") -> str:
    """
    Get a chatbot response with a specific tone.
    """
    try:
        chatbot = get_chatbot()
        final_prompt = f"Respond in a {tone.lower()} tone: {prompt}"
        output = chatbot.invoke(final_prompt)
        return output.content.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
