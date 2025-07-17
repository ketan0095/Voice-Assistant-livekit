"""Agent runner."""

import asyncio

from livekit import agents

from agent.agent import Assistant
from agent.session import create_session, get_room_options
from prompt_store.prompt_builder import build_context
from utils.handler import (
    handle_participant_disconnected,
    handle_shutdown,
    speech_handler,
)
from utils.logger import VirtualAssistantLogger
from utils.types import CallContext

agent_logger = VirtualAssistantLogger()


async def entrypoint(ctx: agents.JobContext):
    """Entrypoint for livekit agent."""
    # 1. Instantiate session
    session = create_session()

    # 2. Build Context TODO: Fetch this from DB
    call_context: CallContext = {
        "prompt": "",
        "org_info": {
            "agent_name": "John",
            "company_name": "MediLink Health",
            "agent_goal": "help users schedule, manage,appointments seamlessly",
            "trading_hours": "8 AM - 8 PM, Monday to Saturday",
            "address": "123 Health Blvd, Sydney, NSW 2000",
            "service_types": "General Practice, Physiotherapy, Pathology",
            "service_modalities": "in-person, telehealth, home visit",
        },
        "agent_details":{
            "agent_name":"ketan",
            "agent_settings":{
                "custom_msg":{
                "welcome_settings":{
                    "welcome_msg":"hello, how are you?",
                    "welcome_delay":2
                },
                "closing_settings":{
                    "closing_msg":"Thank you, have a good day.",
                    "closing_delay":1
                }
            },
            }
        }
    }
    call_context["prompt"] = build_context(call_context["org_info"])

    agent_logger.info("Updated prompt : " + str(call_context["prompt"]))

    # 3. Build Agent
    agent = Assistant(session, agent_logger, instructions=call_context["prompt"],
                      call_context=call_context)

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

    # 8. shutdown agent
    ctx.add_shutdown_callback(lambda: handle_shutdown(session, ctx))


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
