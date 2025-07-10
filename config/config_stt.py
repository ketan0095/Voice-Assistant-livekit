from livekit.plugins import deepgram
from config import config

def get_stt_config():
    return deepgram.STT(model=config.DEEPGRAM_MODEL, language="multi")