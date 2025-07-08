from livekit import agents
from agent import Assistant
from session import create_session, get_room_options

async def entrypoint(ctx: agents.JobContext):
    session = create_session()

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=get_room_options(),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )

if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
