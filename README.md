# 🤖 Gemini Agent

A toy AI coding agent powered by Google's Gemini API. It uses function calling to interact with your local filesystem — reading files, writing files, listing directories, and running Python scripts — all driven by natural language prompts.

## What It Does

You give it a prompt, and it figures out what to do. The agent operates in a loop: it reads your request, decides which tool(s) to call, inspects the results, and keeps going until it has an answer. It's scoped to a sandboxed working directory (`calculator/`) so it can't go poking around your entire system.

### Available Tools

| Tool | Description |
|---|---|
| `get_files_info` | Lists files and directories with sizes |
| `get_file_content` | Reads file contents (up to 10k chars) |
| `run_python_file` | Executes a Python file and captures output |
| `write_file` | Creates or overwrites files |

## Project Structure

```
gemini-agent/
├── main.py              # Entry point — handles CLI args and the agent loop
├── prompt.py            # System prompt for the AI agent
├── call_function.py     # Maps function calls from the model to actual functions
├── config.py            # Constants (MAX_CHARS, WORKING_DIR)
├── tests.py             # Quick manual tests
├── functions/           # Tool implementations
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── run_python.py
│   └── write_file.py
└── calculator/          # Sample project the agent operates on
    ├── main.py
    └── pkg/
```

## Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- A Gemini API key

### Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/gemini-agent.git
   cd gemini-agent
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```
   Or with pip:
   ```bash
   pip install google-genai==1.12.1 python-dotenv==1.1.0
   ```

3. **Add your API key**

   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### Usage

```bash
python main.py "your prompt here"
```

With verbose output (shows token counts and function call details):
```bash
python main.py "your prompt here" --verbose
```

### Example

```bash
python main.py "Run the calculator with the expression 3 + 5 and tell me the result"
```

The agent will:
1. List files in the `calculator/` directory
2. Read the relevant source files to understand the project
3. Execute `calculator/main.py` with the right arguments
4. Report the result back to you

## How It Works

1. Your prompt is sent to `gemma-4-31b-it` via the Gemini API with a set of tool declarations
2. The model responds with either a text answer or one or more function calls
3. Function calls are executed locally, and results are fed back to the model
4. This loop continues (up to 20 iterations) until the model produces a final text response

## Notes

- This is a **toy project** — it's meant for learning and experimentation, not production use
- The agent is sandboxed to the `calculator/` directory by default
- File reads are capped at 10,000 characters
- Python script execution has a 30-second timeout

## License

Do whatever you want with it. 🤷
