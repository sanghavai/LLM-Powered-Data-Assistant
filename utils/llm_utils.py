from langchain.llms import Ollama

def get_deepseek_llm():
    
    try:
        return Ollama(model="deepseek-coder:6.7b")
    except Exception as e:
        raise RuntimeError("Failed to initialize the Deepseek-Coder LLM. Ensure Ollama is running and the model is available.") from e
