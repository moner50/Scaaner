
# Compiler Design

This project presents a simple compiler built in Python, currently implementing only the scanner phase of the compilation process. The scanner, or lexical analyzer, tokenizes input code, breaking it down into meaningful symbols (tokens) for further analysis.

## Overview
The goal of this project is to provide a foundational understanding of compiler design principles, focusing on the initial stage of lexical analysis. The scanner reads source code and converts it into a series of tokens that represent basic language constructs such as identifiers, operators, numbers, and more.

This project offers developers valuable insights into the internal mechanisms of a compiler, especially regarding the tokenization process and foundational programming language structures.

## Lexical Analysis
Lexical analysis, also known as lexing or tokenization, is the first phase of the compiler. It scans the raw source code and converts it into a sequence of tokens, which represent the smallest units of meaning in the code. This phase is essential as it lays the groundwork for parsing and other subsequent steps in the compilation process.

## Token Types
The scanner handles various types of tokens in the code, including:

- **Keywords**: Reserved words like `if`, `else`, `for`, and `while` that have specific meanings in the programming language.
- **Identifiers**: Names used for variables, functions, or classes.
- **Numeric Constants**: Numbers used within the code, including integers and floating-point numbers.
- **Operators**: Symbols that represent arithmetic or logical operations, such as `+`, `-`, `*`, and `/`.
- **Special Characters**: Symbols like parentheses `(`, `)`, braces `{`, `}`, commas `,`, and semicolons `;` that help structure the code.
- **String Literals**: Text surrounded by quotation marks `" "` or `' '`.

Each token type plays a critical role in understanding the structure of the code and ensuring it adheres to the syntax of the language.

## Features
- **Lexical Analysis**: Scans input code to generate tokens
- **Support for Basic Tokens**: Identifies key elements like identifiers, numbers, and arithmetic operators
- **Error Detection**: Handles and flags unexpected characters or unsupported symbols

## Usage
1. Place your code in a text file (e.g., `code.txt`) within the project directory.
2. Open `scanner.py` and modify the `filePath` variable to reference your code file.
3. Run `scanner.py` to analyze your code and retrieve tokens.

We hope you enjoy exploring the foundational steps of compiler design through this Scanner phase. Happy coding!


## Team Members

- **Moner Mohamad Moner Tantawi**
- **kareem Eldeen Ahmed**
- **karim maher abdelrahim abdelatti**
- **A'laa  Amin Abdulaziz Elgezery**
- **Habiba Abo Khalil Hadaad**
