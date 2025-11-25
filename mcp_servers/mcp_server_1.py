import math
import sys
from PIL import Image as PILImage

from mcp.server import FastMCP
from mcp.server.fastmcp.prompts import base

from models import AddInput, AddOutput, SubtractInput, SubtractOutput, MultiplyInput, MultiplyOutput, DivideInput, \
    DivideOutput, PowerInput, PowerOutput, CbrtInput, CbrtOutput, FactorialInput, FactorialOutput, RemainderInput, \
    RemainderOutput, SinInput, SinOutput, CosInput, CosOutput, TanInput, TanOutput, MineInput, MineOutput, \
    CreateThumbnailInput, ImageOutput, StringsToIntsInput, StringsToIntsOutput, ExpSumInput, ExpSumOutput, \
    FibonacciInput, FibonacciOutput

mcp = FastMCP("Calculator")


@mcp.tool()
def add(input: AddInput) -> AddOutput:
    print("Tool Called: add(AddInput) -> AddOutput")
    return AddOutput(result=input.a + input.b)


@mcp.tool()
def subtract(input: SubtractInput) -> SubtractOutput:
    """Subtract one number from another. """
    print("CALLED: subtract(SubtractInput) -> SubtractOutput")
    return SubtractOutput(result=input.a - input.b)


@mcp.tool()
def multiply(input: MultiplyInput) -> MultiplyOutput:
    """Multiply two integers. """
    print("CALLED: multiply(MultiplyInput) -> MultiplyOutput")
    return MultiplyOutput(result=input.a * input.b)


@mcp.tool()
def divide(input: DivideInput) -> DivideOutput:
    """Divide one number by another. """
    print("CALLED: divide(DivideInput) -> DivideOutput")
    return DivideOutput(result=input.a / input.b)


@mcp.tool()
def power(input: PowerInput) -> PowerOutput:
    """Compute a raised to the power of b. """
    print("CALLED: power(PowerInput) -> PowerOutput")
    return PowerOutput(result=input.a ** input.b)


@mcp.tool()
def cbrt(input: CbrtInput) -> CbrtOutput:
    """Compute the cube root of a number. """
    print("CALLED: cbrt(CbrtInput) -> CbrtOutput")
    return CbrtOutput(result=input.a ** (1 / 3))


@mcp.tool()
def factorial(input: FactorialInput) -> FactorialOutput:
    """Compute the factorial of a number. """
    print("CALLED: factorial(FactorialInput) -> FactorialOutput")
    return FactorialOutput(result=math.factorial(input.a))


@mcp.tool()
def remainder(input: RemainderInput) -> RemainderOutput:
    """Compute the remainder of a divided by b. """
    print("CALLED: remainder(RemainderInput) -> RemainderOutput")
    return RemainderOutput(result=input.a % input.b)


@mcp.tool()
def sin(input: SinInput) -> SinOutput:
    """Compute sine of an angle in radians. """
    print("CALLED: sin(SinInput) -> SinOutput")
    return SinOutput(result=math.sin(input.a))


@mcp.tool()
def cos(input: CosInput) -> CosOutput:
    """Compute cosine of an angle in radians. """
    print("CALLED: cos(CosInput) -> CosOutput")
    return CosOutput(result=math.cos(input.a))


@mcp.tool()
def tan(input: TanInput) -> TanOutput:
    """Compute tangent of an angle in radians. """
    print("CALLED: tan(TanInput) -> TanOutput")
    return TanOutput(result=math.tan(input.a))


@mcp.tool()
def mine(input: MineInput) -> MineOutput:
    """Special mining tool. """
    print("CALLED: mine(MineInput) -> MineOutput")
    return MineOutput(result=input.a - input.b - input.b)


@mcp.tool()
def create_thumbnail(input: CreateThumbnailInput) -> ImageOutput:
    """Create a 100x100 thumbnail from image. """
    print("CALLED: create_thumbnail(CreateThumbnailInput) -> ImageOutput")
    img = PILImage.open(input.image_path)
    img.thumbnail((100, 100))
    return ImageOutput(data=img.tobytes(), format="png")


@mcp.tool()
def strings_to_chars_to_int(input: StringsToIntsInput) -> StringsToIntsOutput:
    """Convert characters to ASCII values. """
    print("CALLED: strings_to_chars_to_int(StringsToIntsInput) -> StringsToIntsOutput")
    ascii_values = [ord(char) for char in input.string]
    return StringsToIntsOutput(ascii_values=ascii_values)


@mcp.tool()
def int_list_to_exponential_sum(input: ExpSumInput) -> ExpSumOutput:
    """Sum exponentials of int list. """
    print("CALLED: int_list_to_exponential_sum(ExpSumInput) -> ExpSumOutput")
    result = sum(math.exp(i) for i in input.numbers)
    return ExpSumOutput(result=result)


@mcp.tool()
def fibonacci_numbers(input: FibonacciInput) -> FibonacciOutput:
    """Generate first n Fibonacci numbers. """
    print("CALLED: fibonacci_numbers(FibonacciInput) -> FibonacciOutput")
    n = input.n
    if n <= 0:
        return FibonacciOutput(result=[])
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return FibonacciOutput(result=fib_sequence[:n])


# ------------------- Resources -------------------

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting. """
    print("CALLED: get_greeting(name: str) -> str")
    return f"Hello, {name}!"


# ------------------- Prompts -------------------

@mcp.prompt()
def review_code(code: str) -> str:
    """Ask to review a code snippet. """
    return f"Please review this code:\n\n{code}"


@mcp.prompt()
def debug_error(error: str) -> list:
    """Help debug an error. """
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]


def mcp_log(level: str, filename: str, message: str) -> None:
    sys.stderr.write(f"{level}: {filename}: {message}\n")
    sys.stderr.flush()


if __name__ == '__main__':
    mcp_log("INFO", "mcp_server_1.py", "Starting mcp_server_1 server...")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()
    else:
        mcp.run(transport="stdio")
        mcp_log("INFO", "mcp_server_1.py", "Shutting down mcp_server_1 server")
