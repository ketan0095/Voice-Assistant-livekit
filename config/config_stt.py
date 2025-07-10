from livekit.plugins import deepgram
from config.config import Config

def get_stt_config():
    return deepgram.STT(model=Config.DEEPGRAM_MODEL, language="multi")