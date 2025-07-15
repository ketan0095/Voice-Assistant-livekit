"""Agent handler."""

import json
from livekit.agents import AgentSession, MetricsCollectedEvent, UserStateChangedEvent
from livekit.agents import AgentStateChangedEvent, JobContext
from livekit import rtc
from utils.logger import VirtualAssistantLogger

logger = VirtualAssistantLogger()


def speech_handler(session: AgentSession):
    """Handle voice handler functions.
    Args:
        session (AgentSession): The current agent session managing the call.
    """

    @session.on("conversation_item_added")
    def on_conversation_item_added(item):
        # TODO: Save conversation history here
        logger.info(item)

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        # TODO: Save STT,LLM,TTS,EOU metrics here
        logger.info(ev)

    @session.on("function_tools_executed")
    def _on_function_tools_executed(ev):
        # TODO: get function execution details here
        logger.info(ev)


def handle_inactivity(session: AgentSession):
    """Handle inacticity for agent."""
    # TODO: Handle user inactivity here

    @session.on("user_state_changed")
    def on_user_state_changed(ev: UserStateChangedEvent):
        # TODO: Track user activity here
        logger.info(ev)

    @session.on("agent_state_changed")
    def on_agent_state_changed(ev: AgentStateChangedEvent):
        # TODO: Track assistant activity here
        logger.info(ev)


async def handle_participant_disconnected(
    session: AgentSession, ctx: JobContext, participant: rtc.RemoteParticipant
):
    """
    Handle cleanup and logging when a remote participant disconnects from the session.

    Args:
        session (AgentSession): The current agent session managing the call.
        ctx (JobContext): The context of the ongoing job or call.
        participant (rtc.RemoteParticipant): The participant who disconnected.

    This coroutine is triggered when a remote participant leaves the call,
    allowing for any necessary state updates or resource cleanup.
    """

    try:
        if participant.kind == rtc.ParticipantKind.PARTICIPANT_KIND_AGENT:
            logger.info("Agent %s disconnected" + participant.identity)
        elif participant.kind == rtc.ParticipantKind.PARTICIPANT_KIND_SIP:
            logger.info(f"SIP participant {participant.identity} disconnected")
        else:
            logger.info(
                f"Participant {participant.identity} disconnected ({participant.kind})"
            )

        if session:
            # handle session background tasks
            logger.info(ctx)

    except Exception as e:
        logger.error(f"Error during participant disconnect handler: {e}")


async def handle_shutdown(session: AgentSession, ctx: JobContext):
    """
    Perform cleanup tasks when the agent session is shutting down.

    Args:
        session (AgentSession): The current agent session being terminated.
        ctx (JobContext): The context of the running job or call.

    This coroutine handles any necessary finalization, such as logging session
    history and deleting associated resources like the communication room.
    """

    # Store session history
    logger.info("Session history:\n" + json.dumps(session.history.to_dict(), indent=2))
    # delete room
    await ctx.delete_room()
