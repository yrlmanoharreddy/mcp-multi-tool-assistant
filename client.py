import asyncio
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent
from mcp.shared.context import RequestContext

async def main():
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1
    )
    client = MultiServerMCPClient(
        {
            "college": {
                "command": "python",
                "args": ["mcp_server.py"],
                "transport": "stdio"
            }
        }
    )

    tools = await client.get_tools()
    print("Available tools")
    for tool in tools:
        print(f"- {tool.name}")

    agent = create_agent(
        model=llm,
        tools=tools
    )
    while True:
        question = input("\n You: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("GB")
            break
        if not question:
            continue

        try:
            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role" : "user",
                            "content": question
                        }
                    ]
                }
            )
            answer = response["messages"][-1].content
            print(f"AI Response: {answer}")
        except Exception as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    asyncio.run(main())