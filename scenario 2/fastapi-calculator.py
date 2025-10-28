# HTTP Calculator API
from fastapi import FastAPI # type: ignore
from fastapi_mcp import FastApiMCP # type: ignore #

# 1. FastAPI app
app = FastAPI(title="Calculator")

@app.post("/multiply")
def multiply_numbers(a: float, b: float):
    """
    Multiply two numbers and return the result.
    """
    result = a * b
    return {"result": result}

@app.post("/add")
def add_numbers(a: float, b: float):
    """
    Add two numbers and return the result.
    """
    result = a + b
    return {"result": result}

@app.post("/subtract")
def subtract_numbers(a: float, b: float):
    """
    Subtract two numbers and return the result.
    """
    result = a - b
    return {"result": result}

@app.post("/divide")
def divide_numbers(a: float, b: float):
    """
    Divide two numbers and return the result.
    """
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    result = a / b
    return {"result": result}

# converting to mcp
mcp = FastApiMCP(app, name= "calcautlator Mcp")
mcp.mount_http()


if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="localHost", port=8002)
mcp.run()
