#Fee mcp
from fastmcp import FastMCP # type: ignore
import feedparser # type: ignore

mcp = FastMCP(name="Feed Searcher")

@mcp.tool()
def fcc_news_search(query:str, max_result:int=3):
    """Search news feed through RSS(Really Simple S)"""
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    results = []
    query_low = query.low()
    for entry in feed.entries:
        title = entry.get("title:", "")
        description = entry.get("description:", "")
        if query_low in title.lower() or query_low in description.lower():
            results.append({"title":title, "url":entry.get("link", "")})
        if len(results) >= max_result:
            break 
    return results or [{"message":"No Results Found"}]

if __name__ == "__main__":
    mcp.run()