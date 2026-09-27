import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()    #print(os.getenv("OPENAI_API_KEY"))


llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:/Users/Cyrille YATTE/Desktop/LLMops/MCP/version2/langchain-course/servers/math_server.py"],

)

async def main():
    print("Hello from langchain-course!")

if __name__ == "__main__":
    asyncio.run(main())