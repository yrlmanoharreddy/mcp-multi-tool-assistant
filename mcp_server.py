import requests
from mcp.server.fastmcp import FastMCP
from tools.weather import get_weather

mcp = FastMCP("Collge MCP Server")

@mcp.tool()
def add(a: int, b:int):
    """Add two numbers"""
    return a+b

@mcp.tool()
def get_student(student_id: int)->dict:
    url = f"http://127.0.0.1:8000/student/{student_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

@mcp.tool()
def weather(city: str)->dict:
    """Retrive current weather"""
    return get_weather(city)

if __name__ == "__main__":
    mcp.run(transport="stdio")