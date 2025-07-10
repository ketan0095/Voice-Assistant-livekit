from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    DEEPGRAM_MODEL = os.getenv("DEEPGRAM_MODEL", "nova-3")
    ELEVENLABS_VOICE = os.getenv("ELEVENLABS_VOICE_ID")  
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  
    AZURE_OPENAI_ENDPOINT=os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY=os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_DEPLOYMENT=os.getenv("AZURE_OPENAI_DEPLOYMENT")
    AZURE_API_VERSION=os.getenv("AZURE_API_VERSION")

config = Config()
