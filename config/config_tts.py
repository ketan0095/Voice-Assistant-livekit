from livekit.plugins.elevenlabs import TTS as ElevenLabsTTS
from config.config import Config

def get_tts_config():
    return ElevenLabsTTS(api_key=Config.ELEVENLABS_API_KEY)