import ply.lex as lex
import ply.yacc as yacc

# Define the list of Hebrew keywords and their English translations
keywords = {
    'הדפס': 'print',
    'אם': 'if',
    'אחרת': 'else',
    # Add more keywords as needed
}

# Define the tokens for the lexer
tokens = [
    'PRINT',
    'STRING',
]

# Token rules
t_PRINT = r'הדפס'
t_STRING = r'"[^"]*"'

# Lexer rules
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parser rules
def p_statement_print(p):
    'statement : PRINT STRING'
    # p[0] = 'print(' + p[2] + ')'
    p[0] = p[2]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc()

# Test program
program = '''
הדפס("שלום נעמה!")
'''

# Lex and parse the program
lexer.input(program)


result = parser.parse(program)
print(result)