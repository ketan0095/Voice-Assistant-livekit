from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import noise_cancellation
from config.config_llm import get_azure_openai_llm
from config.config_tts import get_elevenlabs_tts
from config.config_stt import get_deepgram_stt
from config.config_noise_adapter import get_vad_config,get_turn_config


def create_session() -> AgentSession:
    """Create agent session."""
    return AgentSession(
        stt=get_deepgram_stt(),
        llm=get_azure_openai_llm(),
        tts=get_elevenlabs_tts(),
        vad=get_vad_config(),
        turn_detection=get_turn_config(),
    )

def get_room_options() -> RoomInputOptions:
    """Collect room options for agent."""
    return RoomInputOptions(
        noise_cancellation=noise_cancellation.BVC()
    )
