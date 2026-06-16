"""
prompt_server.py — An MCP server that exposes a PROMPT (not a tool).

A prompt is a reusable, parameterized message template. The server builds
the text; the client fetches it and sends it to the model. Nothing here
runs an LLM or computes anything.
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Explainer")


@mcp.prompt()
def explain_concept(topic: str = "the client-server model",
                    audience: str = "a beginner") -> str:
    """Build a prompt asking the model to explain a computing concept clearly."""
    return (
        f"Explain {topic} to {audience}.\n"
        "Use one simple real-world analogy, keep it under 150 words, "
        "and finish with a single sentence on why it matters for MCP."
    )


if __name__ == "__main__":
    mcp.run()  # stdio
