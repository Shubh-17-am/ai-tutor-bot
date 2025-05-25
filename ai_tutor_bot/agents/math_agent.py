from ai_tutor_bot.tools.calculator import calculate
from ai_tutor_bot.utils import query_gemini

def answer(query: str):
    if any(op in query for op in "+-*/"):
        return calculate(query)
    return query_gemini(query)