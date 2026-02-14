# Agentize

A lightweight CLI coding agent powered by Claude AI. It can read, write, and edit files in your project through natural conversation.

## Features

- **File Operations** — Read, create, and edit files seamlessly
- **Directory Navigation** — Explore and list project structure
- **Conversational Interface** — Natural language commands
- **Tool Chaining** — Agent automatically chains multiple operations
- **Error Handling** — Graceful error recovery and feedback

## Installation

### Prerequisites

- Python 3.10+
- Anthropic API key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/agentize.git
cd agentize
```

2. Install dependencies:
```bash
pip install anthropic termcolor pydantic
```

3. Set your API key:
```bash
export ANTHROPIC_API_KEY="your-api-key"
```

## Usage

Start the agent:
```bash
python main.py
```

### Example Commands

```
You: list all files in this project
You: read main.py
You: create a python script that sorts a list
You: add input validation to sum_of_digits.py
You: refactor the error handling in tools.py
```

### Example Session

```
Chat with Claude (Ctrl+C or Ctrl+D to quit)
You: create a hello world script
tool: edit_file({"path": "hello.py", "old_str": "", "new_str": "print('Hello, World!')"})
Claude: I've created hello.py with a simple Hello World program.
```

## Tools

| Tool | Description |
|------|-------------|
| `read_file` | Read contents of a file |
| `list_files` | List files in directory |
| `edit_file` | Create or edit a file |

## Project Structure

```
agentize/
├── main.py           # Agent core and conversation loop
├── tools.py          # Tool definitions and implementations
├── sum_of_digits.py  # Example: created by this agent
└── README.md         # You're reading it
```

## Examples Created by This Agent

The following were generated entirely by this agent:

| File | Description |
|------|-------------|
| `README.md` | This documentation |
| `sum_of_digits.py` | Number sum calculator |
| `snake_game.py` | Classic snake game |

## License

MIT

---

> **🤖 This README was written by an AI agent!**

*Built with [Anthropic Claude](https://anthropic.com)*
