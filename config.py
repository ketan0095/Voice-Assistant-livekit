from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    DEEPGRAM_MODEL = os.getenv("DEEPGRAM_MODEL", "nova-3")
    ELEVENLABS_VOICE = os.getenv("ELEVENLABS_VOICE_ID")  # required
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  # required

config = Config()
