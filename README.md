# Greeter

A simple Python command-line program that generates customizable greeting messages.

## Description

This program demonstrates basic argument parsing in Python using `argparse`. It creates personalized greetings with configurable messages, repetition counts, and text formatting options.

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

Clone this repository:
```bash
git clone https://github.com/jisaacs85/simple-commandline
cd simple-commandline
```

No additional installation required - the script uses only Python's standard library.

## Usage

Basic usage:
```bash
python main.py --name Alice
```

**Arguments:**

| Argument | Short | Type | Required | Default | Description |
|----------|-------|------|----------|---------|-------------|
| `--name` | `-n` | string | Yes | - | Name of the person to greet |
| `--greeting` | `-g` | string | No | "Hi" | Custom greeting message |
| `--count` | `-c` | integer | No | 1 | Number of times to repeat the greeting |
| `--uppercase` | `-u` | flag | No | False | Convert output to uppercase |

**Examples:**

Simple greeting:
```bash
python main.py --name Alice
# Output: 1. Hi, Alice!
```

Custom greeting:
```bash
python main.py --name Bob --greeting Hello
# Output: 1. Hello, Bob!
```

Multiple repetitions:
```bash
python main.py --name Charlie --count 3
# Output:
# 1. Hi, Charlie!
# 2. Hi, Charlie!
# 3. Hi, Charlie!
```

Uppercase output:
```bash
python main.py --name Diana --uppercase
# Output: 1. HI, DIANA!
```

Combined options:
```bash
python main.py -n Eve -g "Good morning" -c 2 -u
# Output:
# 1. GOOD MORNING, EVE!
# 2. GOOD MORNING, EVE!
```

## Help

To view all available options:
```bash
python main.py --help
```

## License

None

## Contributing

None
