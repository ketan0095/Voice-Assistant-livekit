import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    LIVEKIT_URL = os.getenv("LIVEKIT_URL")
    LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
    LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
    AGENT_ID = os.getenv("AGENT_ID", "test-agent")
    AGENT_NAME = os.getenv("AGENT_NAME", "Test Agent")
    ROOM = os.getenv("LIVEKIT_ROOM", "test-room")

    ENABLE_AUDIO = os.getenv("ENABLE_AUDIO", "true").lower() == "true"
    ENABLE_TEXT = os.getenv("ENABLE_TEXT", "true").lower() == "true"

    # STT / LLM / TTS
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "Rachel")

settings = Settings()
