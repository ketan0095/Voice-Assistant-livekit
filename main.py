import asyncio
from livekit.agents import WorkerOptions, AgentInfo
from agent import create_agent, MyWorker
from config import settings

async def main():
    agent = create_agent()

    info = AgentInfo(
        id=settings.AGENT_ID,
        name=settings.AGENT_NAME,
    )

    opts = WorkerOptions(
        api_key=settings.LIVEKIT_API_KEY,
        secret_key=settings.LIVEKIT_API_SECRET,
        url=settings.LIVEKIT_URL,
        agent_info=info,
        room=settings.ROOM,
    )

    worker = MyWorker.create(agent=agent, options=opts)
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
