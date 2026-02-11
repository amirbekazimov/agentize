import json
import os
from typing import Optional

from pydantic import BaseModel, Field


class ToolDefinition:
    def __init__(self, name, description, input_schema, function) -> None:
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.function = function

    def __str__(self) -> str:
        return self.name


def read_file(input_data):
    input_dict = json.loads(input_data)
    path = input_dict["path"]

    try:
        with open(path, "r") as file:
            content = file.read()
        return content, None
    except Exception as e:
        return "", str(e)


def list_files(input_data):
    input_dict = json.loads(input_data) if input_data else {}
    base_path = input_dict.get("path", ".")

    try:
        results = []

        for root, _, file_names in os.walk(base_path):
            if base_path == ".":
                relative_dir = "."
            else:
                relative_dir = os.path.relpath(root, base_path)

            if relative_dir != ".":
                results.append(f"{relative_dir}/")

            for filename in file_names:
                if relative_dir == ".":
                    results.append(filename)
                else:
                    results.append(os.path.join(relative_dir, filename))

            return json.dumps(results), None

    except Exception as e:
        return "", str(e)


class ReadFileInput(BaseModel):
    path: str = Field(
        description="The relative path of a file in the working directory."
    )


class ListFilesInput(BaseModel):
    path: Optional[str] = Field(
        description="Optional relative path to list files from. Defaults to current directory if not provided.",
        default=None,
    )


read_file_definition = ToolDefinition(
    name="read_file",
    description="Read the contents of a given relative file path. Use this when you want to see what's inside a file. Do not use this with directory names.",
    input_schema=ReadFileInput.model_json_schema(),
    function=read_file,
)

list_files_definition = ToolDefinition(
    name="list_files",
    description="List files and directories at a given path. If no path is provided, lists files in the current directory.",
    input_schema=ListFilesInput.model_json_schema(),
    function=list_files,
)
