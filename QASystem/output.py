from QASystem.utils import query_engine, llm
from QASystem.prompts import get_prompt

def generate_response(question: str):
    response = query_engine.query(question)
    context = response.response.strip()
    prompt = get_prompt(context, question)
    answer = llm.complete(prompt)
    
    return answer.text