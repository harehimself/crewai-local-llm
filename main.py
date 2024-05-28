from agents import agent

# Define a task for your agent
task = {
    "type": "generate_text",
    "params": {
        "prompt": "Write a short poem about a cat exploring a magical forest."
    }
}

# Execute the task
agent.execute(task)
# Get the task result
result = agent.get_task_result(task)
print(result)