"""Prompt building for agent."""

from prompt_store.master_prompt import VOICE_AGENT_PERSONA, MASTER_PROMPT_TEMPLATE
from prompt_store.global_rules import get_global_rules_text
from utils.types import CallContext

def build_persona(call_context: CallContext) -> str:
    """
    Construct a persona desc string for the voice agent using organization metadata.

    Args:
        org_info (dict): Dictionary containing org details & agent configuration.
    Returns:
        str: A formatted string representing the voice agent's persona.
    """

    org_info = call_context.get("org_info",{})
    agent_details =call_context.get("agent_details",{})

    return VOICE_AGENT_PERSONA.format(
        agent_name=agent_details.get("agent_name", "Assistant"),
        company_name=org_info.get("company_name", "Your Company"),
        agent_goal=org_info.get("agent_goal", "assist users with their queries"),
        trading_hours=org_info.get("trading_hours", "9 AM - 5 PM, Monday to Friday"),
        address=org_info.get("address", "Not Provided"),
        service_types=org_info.get("service_types", "General support"),
        service_modalities=org_info.get(
            "service_modalities", "in-person and telehealth"
        ),
    )


def build_prompt(
    call_context: CallContext,
    conversation_context: str,
) -> str:
    """
    Build the full master prompt for the voice assistant,
    including persona, rules, context, and user input.

    Args:
        org_info (dict): Metadata about the organization and agent (see build_persona).
        conversation_context (str): Recent conversation history for context.

    Returns:
        str: A fully assembled prompt string suitable for passing to an LLM.
    """
    persona = build_persona(CallContext[""])
    global_rules = get_global_rules_text()

    return MASTER_PROMPT_TEMPLATE.format(
        persona=persona,
        global_rules=global_rules,
        conversation_context=conversation_context.strip(),
    )


def build_context(call_context: CallContext) -> str:
    """
    Build a complete prompt using sample organization data and test conversation.

    Returns:
        str: A complete prompt string for the voice assistant.
    """

    conversation_context = (
        "User: I need to book a GP appointment\nAgent: Sure, I can help with that."
    )

    return build_prompt(call_context, conversation_context)
