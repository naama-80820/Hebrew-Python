import sys
import ply.lex as lex
import ply.yacc as yacc
from lexing.lexer import lexer, tokens
from parsing.parser import parser
from semantic.semantic_analyzer import SemanticAnalyzer
from code_gen.code_generator import generate_code

input_file=r'C:\Users\מאירה\Documents\נעמה\תכנות\פרויקט\עברית - פיתון\input_code.txt'


# פונקציה לקריאת קובץ
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# הפונקציה הראשית
def main(input_file):

    # קריאת הקלט מהקובץ טקסט
    input_code = read_file(input_file)

    # הפעלת הלקסר
    lexer.input(input_code)
    # for token in lexer:
    #     print(token)

    # ניתוח סמנטי
    result = parser.parse(input_code)
    print("Parsed AST:", result)

    # ניתוח סמנטי
    analyzer = SemanticAnalyzer()
    for stmt in result:
        analyzer.visit(stmt)

    # יצירת קוד פייתון
    python_code = "\n".join(generate_code(stmt) for stmt in result if stmt != '\n')
    print("Generated Python code:", python_code)

    # הרצת הקוד הנוצר
    local_vars = {}
    exec(python_code, {}, local_vars)

if __name__ == "__main__":
    main(input_file)
