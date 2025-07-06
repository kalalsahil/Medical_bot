def get_prompt(context: str, question: str):
    prompt = f"""
    You are a helpful medical assistant.\n
    Patient Context:\n {context}\n\n
    Based on the documents and patient data, answer the question.\n
    Question: {question}\n\n
    Answer:
    """
    
    return prompt