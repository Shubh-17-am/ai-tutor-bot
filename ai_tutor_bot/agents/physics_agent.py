from ai_tutor_bot.tools.constants import lookup_constant
from ai_tutor_bot.utils import query_gemini

def answer(query: str):
    const_response = lookup_constant(query)
    if const_response != "Constant not found":
        return const_response
    return query_gemini(query)