from livekit import agents
from agent.agent import Assistant
from agent.session import create_session, get_room_options
from utils.handler import speech_handler,handle_participant_disconnected
from utils.logger import VirtualAssistantLogger
import asyncio

agent_logger =VirtualAssistantLogger()

async def entrypoint(ctx: agents.JobContext):
    session = create_session()

    agent = Assistant(session,agent_logger)

    await session.start(
        room=ctx.room,
        agent=agent,
        room_input_options=get_room_options(),
    )

    await ctx.connect()

    # handle speech emmiters
    speech_handler(session)

    # handle disconnect
    ctx.room.on(
            "participant_disconnected",
            lambda p: asyncio.create_task(handle_participant_disconnected(session, ctx, p)),
        )
    
if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
