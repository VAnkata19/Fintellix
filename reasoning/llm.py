from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from search import search_web
from stock import get_stock_info
from date_utils import get_current_date

# System instructions for the AI agent
SYSTEM_PROMPT = """You are an expert stock market analyst AI assistant. Your job is to help users analyze stocks and make informed investment decisions.

You have access to the following tools:
1. get_current_date - Use this FIRST to get today's date so you know the current date when searching for information.
2. search_web - Use this to search the internet for news, articles, and information about stocks, companies, and market trends.
3. get_stock_info - Use this to fetch the latest End of Day (EOD) stock price data for a given stock symbol.

When analyzing a stock, you should:
1. First get the current date using get_current_date
2. Fetch the current stock price data using get_stock_info
3. Search for recent news and developments about the company
4. Consider market trends and industry factors
5. Provide a balanced analysis with both bullish and bearish perspectives
6. Always remind users that this is not financial advice and they should do their own research

Be concise, factual, and helpful. Cite your sources when providing information from web searches."""

# Set up the language model and tools
#---------------------------------------------------
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
tools = [get_current_date, search_web, get_stock_info]
#---------------------------------------------------
# Create the agent
agent = create_agent(model=llm, tools=tools)
#---------------------------------------------------


# Runs the agent with a given query
def run_agent(query: str) -> str:
    """Run the agent with a given query.
    
    Args:
        query (str): The user's question or request.
        
    Returns:
        str: The agent's response.
    """
    result = agent.invoke({
        "messages": [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=query)
        ]
    })
    return result["messages"][-1].content
