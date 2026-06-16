"""
server.py — A minimal MCP server exposing a single tool.

It does not know or care which LLM calls it.
Run it directly to test, or let the client launch it.
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


# Python decorator to expose a function as an MCP tool with automatic schema inference.
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


if __name__ == "__main__":
    mcp.run()  # communicates over stdio by default
