from strands import Agent
from strands_tools import shell


agent = Agent(tools=[shell])

agent("What can i Do for you?")