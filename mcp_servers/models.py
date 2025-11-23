from pydantic import BaseModel


class AddInput(BaseModel):
    a: int
    b: int


class AddOutput(BaseModel):
    result: int


class FilePathInput(BaseModel):
    file_path: str


class MarkdownOutput(BaseModel):
    markdown: str
