import logging
from strands import Agent

# TODO: Add debug logging to see what your agent is thinking

logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# TODO: Create the agent with the following system prompt: "You are a game master for a Dungeon & Dragon game"

agent = Agent(
    system_prompt="You are a game master for a Dungeon & Dragon game"
)

# TODO: Invoke your agent with a basic query such as "Hi, I am an adventurer ready for adventure!"
print("Invoking the agent...\n")
result = agent("Hi, I am an adventurer ready for adventure!")

