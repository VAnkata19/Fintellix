from tavily import TavilyClient

tavily = TavilyClient()

def search_web(query: str) -> dict:
    """Tool that searches the internet.
    Args:
        query (str): The search query.
    Returns: 
        dict: The search results.
    """
    print(f"Searching for: '{query}'")
    return tavily.search(query=query, max_results=5,topic="news")