from crewai import Agent

# Create a CrewAI Agent that uses your local LLM through Ollama
agent = Agent(
    name="my_ollama_agent",
    llm={
        "type": "ollama",
        "base_url": "$BASE_URL",
        "model_name": "$MODEL_NAME"
    }
)