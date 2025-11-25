from typing import List

from pydantic import BaseModel, Field


class AddInput(BaseModel):
    a: int
    b: int


class AddOutput(BaseModel):
    result: int


class FilePathInput(BaseModel):
    file_path: str


class MarkdownOutput(BaseModel):
    markdown: str


class SearchInput(BaseModel):
    query: str
    max_results: int = Field(default=10, description="Maximum number of results to return")


class SearchDocumentsInput(BaseModel):
    query: str


class PythonCodeOutput(BaseModel):
    result: str


class UrlInput(BaseModel):
    url: str


class SubtractInput(BaseModel):
    a: int
    b: int


class SubtractOutput(BaseModel):
    result: int


class MultiplyInput(BaseModel):
    a: int
    b: int


class MultiplyOutput(BaseModel):
    result: int


class SqrtInput(BaseModel):
    a: int
    b: int


class SqrtOutput(BaseModel):
    result: int


class DivideInput(BaseModel):
    a: int
    b: int


class DivideOutput(BaseModel):
    result: float


class PowerInput(BaseModel):
    a: int
    b: int


class PowerOutput(BaseModel):
    result: int


class CbrtInput(BaseModel):
    a: int


class CbrtOutput(BaseModel):
    result: float


class FactorialInput(BaseModel):
    a: int


class FactorialOutput(BaseModel):
    result: int


class RemainderInput(BaseModel):
    a: int
    b: int


class RemainderOutput(BaseModel):
    result: int


class SinInput(BaseModel):
    a: int


class SinOutput(BaseModel):
    result: float


class CosInput(BaseModel):
    a: int


class CosOutput(BaseModel):
    result: float


class TanInput(BaseModel):
    a: int


class TanOutput(BaseModel):
    result: float


class MineInput(BaseModel):
    a: int
    b: int


class MineOutput(BaseModel):
    result: int


# --- String & List Tools ---

class StringsToIntsInput(BaseModel):
    string: str


class StringsToIntsOutput(BaseModel):
    ascii_values: List[int]


class ExpSumInput(BaseModel):
    numbers: List[int]


class ExpSumOutput(BaseModel):
    result: float


class FibonacciInput(BaseModel):
    n: int


class FibonacciOutput(BaseModel):
    result: List[int]


# --- Image Tools ---

class CreateThumbnailInput(BaseModel):
    image_path: str


class ImageOutput(BaseModel):
    data: bytes
    format: str
