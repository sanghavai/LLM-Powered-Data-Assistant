from langchain.llms import Ollama

def get_mistral_llm():
    return Ollama(model="mistral")
