from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    DEEPGRAM_MODEL = os.getenv("DEEPGRAM_MODEL", "nova-3")
    ELEVENLABS_VOICE = os.getenv("ELEVENLABS_VOICE_ID")  
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  
    AZURE_OPENAI_ENDPOINT=os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_KEY=os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_DEPLOYMENT=os.getenv("AZURE_OPENAI_DEPLOYMENT")
    AZURE_API_VERSION=os.getenv("AZURE_API_VERSION")


    # ========== LLM PROVIDERS ==========
    # OpenAI (Public API)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

    # Anthropic (Claude)
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")

    # Mistral
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MISTRAL_MODEL = os.getenv("MISTRAL_MODEL", "mistral-small")

    # Together AI
    TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
    TOGETHER_MODEL = os.getenv("TOGETHER_MODEL", "meta-llama/Llama-3-70b-chat-hf")

    # Cohere
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    COHERE_MODEL = os.getenv("COHERE_MODEL", "command-r-plus")

    # Ollama (local)
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    # ========== STT PROVIDERS ==========
    # Whisper API (OpenAI)
    WHISPER_API_MODEL = os.getenv("WHISPER_API_MODEL", "whisper-1")
    WHISPER_API_LANGUAGE = os.getenv("WHISPER_API_LANGUAGE", "en")

    # Whisper.cpp (local)
    WHISPER_CPP_MODEL_PATH = os.getenv("WHISPER_CPP_MODEL_PATH", "./models/ggml-base.en.bin")
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


config = Config()
