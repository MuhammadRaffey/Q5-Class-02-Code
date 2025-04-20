from agents import Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled
from dotenv import load_dotenv,find_dotenv
import os
from agents.run import RunConfig
import asyncio
from openai import AsyncOpenAI

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
model = OpenAIChatCompletionsModel(
    model=MODEL,
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
)

set_tracing_disabled(disabled=True)

async def main():
    coder = Agent(
        name="Code Generator Assistant",
        instructions="You are a code generator assistant. You are given a prompt and you need to generate code based on it.",
        # model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )
    explainer = Agent(
        name="Code Explainer Assistant",
        instructions="You are a code explainer assistant. You are given a code snippet and you need to explain it in a way that is easy to understand.",
        # model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )
    teacher = Agent(
        name="Programming Teaching Assistant",
        instructions="You are a programming teaching assistant. Your goal is to help users with their programming-related questions in a clear, easy-to-understand way. You have access to two other agents: the Code Generator Assistant (for generating code) and the Code Explainer Assistant (for explaining code). If the user asks about booking, hand off the conversation to the booking agent. If the user asks about refunds, hand off to the refund agent. Always prioritize being helpful, accurate, and approachable.",

        handoffs=[coder, explainer],
        # model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )
    result = await Runner.run(
        teacher,
        "Tell me about recursion in programming, I need a code example with proper explanation.",run_config=config
    )
    # print(result.final_output)
    with open("Handoff result.md", "w") as f:
        f.write(result.final_output)
    print("Handoff result saved to Handoff result.md")

if __name__ == "__main__":
    asyncio.run(main())