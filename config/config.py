"""Handle all secret keys"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    """Gather all required env vars."""
    # ------- LLM provider ----
    AZURE_OPENAI_ENDPOINT=os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY=os.getenv("AZURE_OPENAI_KEY")
    AZURE_DEPLOYMENT_NAME=os.getenv("AZURE_OPENAI_DEPLOYMENT")
    AZURE_API_VERSION=os.getenv("AZURE_API_VERSION")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    # ------- STT provider ----
    DEEPGRAM_MODEL = os.getenv("DEEPGRAM_MODEL", "nova-3")
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
    # ------- TTS provider ----
    ELEVENLABS_VOICE = os.getenv("ELEVENLABS_VOICE_ID")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")



    # ========== Other LLM PROVIDERS ==========
    # OpenAI (Public API)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

    # Anthropic (Claude)
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")

    # Ollama (local)
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    # ========== Other STT PROVIDERS ==========

    #Azure
    AZURE_SPEECH_HOST =os.getenv("AZURE_SPEECH_HOST","")
    # Whisper API (OpenAI)
    WHISPER_API_MODEL = os.getenv("WHISPER_API_MODEL", "whisper-1")
    WHISPER_API_LANGUAGE = os.getenv("WHISPER_API_LANGUAGE", "en")

    # Whisper.cpp (local)
    WHISPER_CPP_MODEL_PATH = os.getenv("WHISPER_CPP_MODEL_PATH", ".")
    WHISPER_CPP_LANGUAGE = os.getenv("WHISPER_CPP_LANGUAGE", "en")

    # Azure Speech-to-Text
    AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
    AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION", "australiaeast")
    AZURE_SPEECH_LANGUAGE = os.getenv("AZURE_SPEECH_LANGUAGE", "en-US")

    # Google Cloud Speech-to-Text
    GOOGLE_CLOUD_CREDENTIALS_JSON = os.getenv("GOOGLE_CLOUD_CREDENTIALS_JSON")
    GOOGLE_SPEECH_LANGUAGE = os.getenv("GOOGLE_SPEECH_LANGUAGE", "en-US")

    # AssemblyAI
    ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
    ASSEMBLYAI_MODEL = os.getenv("ASSEMBLYAI_MODEL", "latest")
    ASSEMBLYAI_LANGUAGE = os.getenv("ASSEMBLYAI_LANGUAGE", "en")


    # ========== Other TTS PROVIDERS ==========
    # OpenAI TTS
    OPENAI_TTS_VOICE = os.getenv("OPENAI_TTS_VOICE")  # e.g., "alloy", "shimmer"

    # Local system TTS
    LOCAL_TTS_COMMAND = os.getenv("LOCAL_TTS_COMMAND")  # e.g., "say" or "espeak"


config = Config()
