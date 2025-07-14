from livekit import agents
from agent.agent import Assistant
from agent.session import create_session, get_room_options
from utils.handler import speech_handler,handle_participant_disconnected
from utils.logger import VirtualAssistantLogger
from prompt_store.prompt_builder import build_context
from utils.types import CallContext
import asyncio

agent_logger =VirtualAssistantLogger()

async def entrypoint(ctx: agents.JobContext):
    # 1. Instantiate session
    session = create_session()

    # 2. Build Context TODO: Fetch this from DB
    call_context :CallContext ={
       'prompt':"",
       "org_info":{
        "agent_name": "John",
        "company_name": "MediLink Health",
        "agent_goal": "help users schedule, manage,appointments seamlessly",
        "trading_hours": "8 AM – 8 PM, Monday to Saturday",
        "address": "123 Health Blvd, Sydney, NSW 2000",
        "service_types": "General Practice, Physiotherapy, Pathology",
        "service_modalities": "in-person, telehealth, home visit",
    }
    }
    call_context['prompt']= build_context(call_context["org_info"])

    agent_logger.info("Updated prompt : "+str(call_context['prompt']))


    # 3. Build Agent
    agent = Assistant(session,agent_logger,instructions=call_context['prompt'])

    # 4. Start session
    await session.start(
        room=ctx.room,
        agent=agent,
        room_input_options=get_room_options(),
    )

    # 5. Connect room
    await ctx.connect()

    # 6. handle speech emmiters
    speech_handler(session)

    # 7. handle disconnect
    ctx.room.on(
            "participant_disconnected",
            lambda p: asyncio.create_task(handle_participant_disconnected(session, ctx, p)),
        )

if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
