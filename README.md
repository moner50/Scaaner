# Compiler Design

This project presents a simple compiler built in Python, implementing both the scanner (lexical analyzer) and a Recursive Descent Parser phases of the compilation process. These phases tokenize input code and parse it to ensure it adheres to the grammar rules of a programming language.

## Overview
The goal of this project is to provide a foundational understanding of compiler design principles, focusing on lexical analysis and parsing. The scanner reads source code and converts it into a series of tokens, while the parser checks the token sequence against grammar rules, ensuring syntactic correctness and generating a parse tree.

## Lexical Analysis
Lexical analysis, also known as lexing or tokenization, is the first phase of the compiler. It scans the raw source code and converts it into a sequence of tokens, which represent the smallest units of meaning in the code. This phase is essential as it lays the groundwork for parsing and other subsequent steps in the compilation process.

### Token Types
The scanner handles various types of tokens in the code, including:

- **Keywords**: Reserved words like `if`, `else`, `for`, and `while` that have specific meanings in the programming language.
- **Identifiers**: Names used for variables, functions, or classes.
- **Numeric Constants**: Numbers used within the code, including integers and floating-point numbers.
- **Operators**: Symbols that represent arithmetic or logical operations, such as `+`, `-`, `*`, and `/`.
- **Special Characters**: Symbols like parentheses `(`, `)`, braces `{`, `}`, commas `,`, and semicolons `;` that help structure the code.
- **String Literals**: Text surrounded by quotation marks `" "` or `' '`.

Each token type plays a critical role in understanding the structure of the code and ensuring it adheres to the syntax of the language.

## Recursive Descent Parsing
Recursive Descent Parsing is a top-down parsing technique where each non-terminal in the grammar is associated with a function. This project implements a Recursive Descent Parser to validate input strings against a specified grammar and generate a parse tree.

### Features
- **Grammar Input**: Users can define custom grammars interactively.
- **String Parsing**: The parser checks if the given input string can be derived from the grammar.
- **Parse Tree Generation**: Constructs a parse tree using Graphviz for visualization.
- **Error Handling**: Ensures input adheres to grammar rules and flags incorrect strings.

### Usage
1. **Define a Grammar**:
   - Start the program and input the number of non-terminals.
   - Define the production rules for each non-terminal.
2. **Check a String**:
   - Input the string to check if it can be derived from the grammar.
   - If valid, a parse tree is generated and saved as `parser_tree.png`.
3. **Interactive Menu**:
   - Allows switching between grammars, testing new strings, and exiting the program.

### Example Workflow
- Define Grammar:
  ```
  S -> aSb
  s -> bAc
  A -> bS
  a->a
  
  ```
- Input String: `"abbbaccb"`
- Output: Accepted with a parse tree generated.
![photo_2024-12-19_14-23-06](https://github.com/user-attachments/assets/f03be0f7-8069-43ba-b856-4f14c2e46316)


## Features
- **Lexical Analysis**: Scans input code to generate tokens.
- **Parsing**: Validates token sequences against grammar rules.
- **Parse Tree Visualization**: Generates graphical representations of derivations.
- **Error Detection**: Handles invalid inputs and unsupported grammar constructs.

## Usage Instructions
### Scanner
1. Place your code in a text file (e.g., `code.txt`) within the project directory.
2. Open `scanner.py` and modify the `filePath` variable to reference your code file.
3. Run `scanner.py` to analyze your code and retrieve tokens.

### Parser
1. Run the parser program.
2. Follow the interactive prompts to define a grammar and test strings.
3. View the parse tree in `parser_tree.png` if the string is accepted.

We hope you enjoy exploring the foundational steps of compiler design through these phases. Happy coding!

## Team Members

- **Moner Mohamad Moner Tantawi**
- **Kareem Eldeen Ahmed**
- **Karim Maher Abdelrahim Abdelatti**
- **A'laa Amin Abdulaziz Elgezery**
- **Habiba Abo Khalil Hadaad**

