"""
prompt_client.py — Fetch a PROMPT from the MCP server, fill in its
arguments, and run it through your local model (qwen3:0.6b).

Run:
    python prompt_client.py prompt_server.py
"""
import asyncio
import sys

from ollama import AsyncClient
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

MODEL = "qwen3:0.6b"


async def main(server_script: str):
    ollama = AsyncClient()
    params = StdioServerParameters(command="python", args=[server_script])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. Discover what prompts the server offers.
            listed = await session.list_prompts()
            print("Available prompts:", [p.name for p in listed.prompts])

            # 2. Ask the server to render a prompt with our chosen arguments.
            result = await session.get_prompt(
                "explain_concept",
                {"topic": "the client-server model", "audience": "a 12-year-old"},
            )

            # 3. Turn the server's prompt messages into chat messages.
            messages = [
                {"role": m.role, "content": m.content.text}
                for m in result.messages
                if m.content.type == "text"
            ]
            print("\nPrompt sent to the model:\n", messages[0]["content"])

            # 4. Send it to the local model and print the explanation.
            resp = await ollama.chat(model=MODEL, messages=messages, think=False)
            print("\n--- Model's explanation ---\n")
            print(resp.message.content)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
