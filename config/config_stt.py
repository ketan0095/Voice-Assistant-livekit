"""Handle STT configs for agent."""

from livekit.plugins import deepgram,openai
from livekit.plugins.azure import stt
from config.config import Config # pylint: disable=import-error
from utils.helper import require

# Deepgram
def get_deepgram_stt():
    """Get Deepgram model."""
    return deepgram.STT(
        api_key=require(Config.DEEPGRAM_API_KEY, "DEEPGRAM_API_KEY"),
        model=require(Config.DEEPGRAM_MODEL, "DEEPGRAM_MODEL"),
        language=getattr(Config, "DEEPGRAM_LANGUAGE", "en"),  # optional
    )

# OpenAI Whisper
def get_whisper_api_stt():
    """Get Whisper STT model"""
    return openai.STT(
    api_key=Config.OPENAI_API_KEY,
    model=Config.WHISPER_API_MODEL,  # e.g., "whisper-1"
    language=Config.WHISPER_API_LANGUAGE,
)


# Azure Speech
def get_azure_stt():
    """Get Azure STT model"""
    return stt.STT(
        speech_key=require(Config.AZURE_SPEECH_KEY, "AZURE_SPEECH_KEY"),
        speech_region=require(Config.AZURE_SPEECH_REGION, "AZURE_SPEECH_REGION"),
        language=getattr(Config, "AZURE_SPEECH_LANGUAGE", "en-US"),
        # Optionally add speech_host if needed
        speech_host=Config.AZURE_SPEECH_HOST,  # optional override
    )
