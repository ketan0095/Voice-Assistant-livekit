from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import openai, deepgram, silero, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins.elevenlabs import TTS as ElevenLabsTTS
from config import config

def create_session() -> AgentSession:
    return AgentSession(
        stt=deepgram.STT(model=config.DEEPGRAM_MODEL, language="multi"),
        llm=openai.LLM(model=config.OPENAI_MODEL),
        tts=ElevenLabsTTS(voice=config.ELEVENLABS_VOICE, api_key=config.ELEVENLABS_API_KEY),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

def get_room_options() -> RoomInputOptions:
    return RoomInputOptions(
        noise_cancellation=noise_cancellation.BVC()
    )
