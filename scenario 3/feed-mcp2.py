#  Feed with secret message
from fastmcp import FastMCP # type:ignore
import feedparser # type:ignore

mcp = FastMCP(name = "Feed with Secret message")

@mcp.tool()
