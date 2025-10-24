# libraries
from fastmcp import FastMCP # pyright: ignore[reportMissingImports]

mcp = FastMCP(name="Calculator")
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b
@mcp.tool(name="add_numbers", description="Adds two numbers together.", tags=["math", "addition"])
def add_numbers(x: float, y: float) -> float:
    """Adds two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return x + y
@mcp.tool(
    name = "subtract_numbers",
    description = "Subtracts the second number from the first number.",
    tags = ["math", "subtraction"]
)
def subtract_numbers(x: float, y: float) -> float:
    """Subtracts the second number from the first number.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The result of the subtraction.
    """
    return x - y
@mcp.tool(
    name = "divide_numbers",
    description = "Divides the first number by the second number.",
    tags = ["math", "division"]
)
def divide_numbers(x: float, y: float) -> float:
    """Divides the first number by the second number.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The result of the division.
    """
    if y == 0:
        return 0
    return x / y
if __name__ == "__main__":
    mcp.run() #STDIO by default