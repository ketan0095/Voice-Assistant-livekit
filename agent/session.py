from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import noise_cancellation
from config.config_llm import get_llm_config
from config.config_tts import get_tts_config
from config.config_stt import get_stt_config
from config.config_noise_adapter import get_vad_config,get_tunr_config


def create_session() -> AgentSession:
    return AgentSession(
        stt=get_stt_config(),
        llm=get_llm_config(),
        tts=get_tts_config(),
        vad=get_vad_config(),
        turn_detection=get_tunr_config(),
    )

def get_room_options() -> RoomInputOptions:
    return RoomInputOptions(
        noise_cancellation=noise_cancellation.BVC()
    )
