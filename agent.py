from strands import Agent
from strands_tools import http_request

SYSTEM_PROMPT = "You are a helpful agent, and you can use APIS that don't require auth, you give outputs in a few lines."
agent = Agent(
    system_prompt=SYSTEM_PROMPT, 
    tools=[http_request],
    # model="meta.llama3-8b-instruct-v1:0",
    # region="us-east-1"
    )

user_input = input("\nNevin:")

print("\nAgent:")
agent(user_input)