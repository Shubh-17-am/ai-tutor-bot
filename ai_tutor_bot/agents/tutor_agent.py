from ai_tutor_bot.agents import math_agent, physics_agent
from ai_tutor_bot.utils import classify_intent

def handle_query(query: str):
    intent = classify_intent(query)
    if intent == "math":
        return math_agent.answer(query)
    return physics_agent.answer(query)