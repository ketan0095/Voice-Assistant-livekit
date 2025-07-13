from livekit.plugins import silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

def get_vad_config():
    return silero.VAD.load()

def get_turn_config():
    return MultilingualModel()