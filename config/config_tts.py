from livekit.plugins import elevenlabs, openai
from config.config import Config
from utils.helper import require

# Elevenlabs
def get_elevenlabs_tts():
    return elevenlabs.TTS(
        api_key=require(Config.ELEVENLABS_API_KEY, "ELEVENLABS_API_KEY"),
    )

# OpenAI TTS (tts-1)
def get_openai_tts():
    return openai.TTS.with_openai(
        api_key=require(Config.OPENAI_API_KEY, "OPENAI_API_KEY"),
        voice=require(Config.OPENAI_TTS_VOICE, "OPENAI_TTS_VOICE"),  # e.g., "echo" or "alloy"
    )

# Local TTS
# def get_local_tts():
#     return local.TTS(
#         command=require(Config.LOCAL_TTS_COMMAND, "LOCAL_TTS_COMMAND"),  # e.g., "say" on macOS or "espeak"
#     )
