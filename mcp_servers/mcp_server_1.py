from mcp.server import FastMCP
from models import AddInput, AddOutput

mcp = FastMCP("Calculator")

@mcp.tool()
def add(input: AddInput) -> AddOutput:
    print("Tool Called: add(AddInput) -> AddOutput")
    return AddOutput(result=input.a + input.b)