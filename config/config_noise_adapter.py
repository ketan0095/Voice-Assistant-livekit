"""Background noise congis for agent."""

from livekit.plugins import silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

def get_vad_config():
    """load VAD config"""
    return silero.VAD.load()

def get_turn_config():
    """Get turn detection config."""
    return MultilingualModel()
