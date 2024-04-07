# Hebrew transpiler for Python

##introduction

"Hebrew - Python" is a transpiler that converts code written in an invented programming language in Hebrew, into the original python language. The main idea is to make it easier to write code for people who have difficulty in English, and to make the world of programming more accessible to everyone. Python is considered an elite and programmer-friendly language. And so I decided to make it available in the Hebrew language as well, in order to provide Hebrew-speaking programmers with an accessible and familiar programming environment.
The main goal is to translate programming elements from Hebrew to Python, with a specific emphasis on variables, conditions, loops and functions. Advanced language features such as object-oriented programming or exception handling - are not handled to maintain focus and efficiency.

## So, how does it work?
Lexical Analyzer - the Hebrew code is analyzed, the lexer breaks it down into a sequence of small units - tokens.
Syntax Analyzer - The syntactic analyzer takes the sequence of tokens, and checks whether it is
Write in a legal form, to build an Abstract Syntax Tree (AST), which provides a structured representation of the code syntax.
Semantic Analyzer - verifies code integrity to ensure conformance to language rules.
Creating Python code - using AST, Python code is created in parallel with the syntax of the Hebrew code


## Technologies in use

- **PLY (Python Lex-Yacc)**: PLY is used to implement the lexer and parser components of the translator, and provides powerful lexical and syntactic analysis capabilities.
- **Python**: The project is implemented in Python, leveraging its expressive syntax and powerful standard library to facilitate code translation.

## Usage

To use the Hebrew to Python translator, follow these steps:

1. Provide input code written in an invented Hebrew-like syntax.
2. Run the translator script.
3. Get the corresponding Python code as output.
