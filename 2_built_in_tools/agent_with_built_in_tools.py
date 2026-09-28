from strands import Agent
# TODO: Import the current_time built-in tool
from strands_tools import current_time

agent = Agent(
    tools=[
        # TODO: Add the current_time tool to your agent
        current_time
    ]
)

result = agent("What time is it?")

print(result)

