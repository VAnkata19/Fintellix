from datetime import datetime

from langchain.tools import tool


@tool
def get_current_date() -> str:
    """Get today's current date.
    
    Use this tool to find out what today's date is. This is useful when you need
    to search for recent news or information and want to know the current date
    to provide context-aware responses.
    
    Returns:
        str: The current date in a human-readable format (e.g., "Thursday, January 22, 2026").
    """

    today = datetime.now()
    print(f"Getting today's date: {today.strftime('%A, %B %d, %Y')}")
    return today.strftime("%A, %B %d, %Y")
