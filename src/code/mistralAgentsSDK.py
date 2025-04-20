import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv,find_dotenv
import os

_=load_dotenv(find_dotenv())

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
if MISTRAL_API_KEY is None:
    raise ValueError("MISTRAL_API_KEY not found in environment variables.")

BASE_URL = "https://api.mistral.ai/v1"
MODEL = "mistral-large-latest"

client = AsyncOpenAI(
    api_key=MISTRAL_API_KEY,
    base_url=BASE_URL
)

set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Teaching Assistant",
        instructions="You are a teaching assistant. You are given a question and you need to answer it in a way that is easy to understand.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Tell me about recursion in programming.",
    )
    # print(result.final_output)
    with open("Mistral result.md", "w") as f:
        f.write(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())