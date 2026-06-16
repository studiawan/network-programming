"""
client.py — Connect your LOCAL Ollama model (qwen3:0.6b) to the tools
exposed by server.py. Nothing leaves your machine.

Prereqs (already done):
    ollama pull qwen3:0.6b
    pip install mcp ollama

Run:
    python client.py server.py
"""
import asyncio
import sys

from ollama import AsyncClient
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

MODEL = "qwen3:0.6b"  # the small tool-capable model you installed


async def main(server_script: str):
    ollama = AsyncClient()  # talks to http://localhost:11434 by default

    # 1. Launch server.py and connect to it over stdio.
    server_params = StdioServerParameters(command="python", args=[server_script])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 2. Discover the server's tools, convert to Ollama's schema.
            tool_list = await session.list_tools()
            tools = [
                {
                    "type": "function",
                    "function": {
                        "name": t.name,
                        "description": t.description,
                        "parameters": t.inputSchema,
                    },
                }
                for t in tool_list.tools
            ]

            messages = [{"role": "user", "content": "What is 17 plus 25?"}]

            # 3. Agentic loop: keep going until the model stops calling tools.
            while True:
                response = await ollama.chat(
                    model=MODEL,
                    messages=messages,
                    tools=tools,
                    think=False,  # qwen3 thinks by default; off = fast, direct tool calls
                    options={"temperature": 0.1},  # steadier tool calls
                )
                messages.append(response.message)

                calls = response.message.tool_calls
                if not calls:
                    print(response.message.content)
                    break

                # 4. Run each requested tool against the MCP server.
                for call in calls:
                    result = await session.call_tool(
                        call.function.name,
                        call.function.arguments,  # already a dict
                    )
                    text = "".join(
                        c.text for c in result.content if c.type == "text"
                    )
                    print(f"[tool] {call.function.name}({call.function.arguments}) -> {text}")
                    messages.append({
                        "role": "tool",
                        "tool_name": call.function.name,
                        "content": text,
                    })


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))