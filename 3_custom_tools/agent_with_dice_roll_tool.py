import logging
from strands import Agent
# TODO: Import tool from strands to use the @tool decorator

from strands import tool

#  Enable debug logging so you can SEE the tool being used
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# TODO: Add the decorator to transform your function into a tool
@tool
def roll_dice(faces: int = 6) -> int:

    # TODO: Modify the docstring with information about arguments and return value
    """
    🎲 Roll a dice with a specified number of faces.
    Use this tool whenever you need to simulate rolling a die for D&D checks, 
    ability scores, or damage.
    
    Args:
        faces: The number of faces on the dice (default is 6). For example, pass 20 for a d20.
        
    Returns:
        The result of the dice roll as an integer.
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)



dice_master = Agent(
    # TODO: Add the tool to the agent
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

# Test your dice master's abilities
dice_master("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")

