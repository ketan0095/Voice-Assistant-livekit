"""All TTS config for agent."""

from livekit.plugins import elevenlabs, openai
from config.config import Config  # pylint: disable=import-error
from utils.helper import require


# Elevenlabs
def get_elevenlabs_tts():
    """Get Elevenlabs TTS model."""
    return elevenlabs.TTS(
        api_key=require(Config.ELEVENLABS_API_KEY, "ELEVENLABS_API_KEY"),
    )


# OpenAI TTS (tts-1)
def get_openai_tts():
    """Get open AI TTS model"""
    return openai.TTS(
        api_key=require(Config.OPENAI_API_KEY, "OPENAI_API_KEY"),
        voice=require(Config.OPENAI_TTS_VOICE, "OPENAI_TTS_VOICE"),
    )
