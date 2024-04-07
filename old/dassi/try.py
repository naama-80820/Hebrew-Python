import ply.lex as lex
import ply.yacc as yacc

# Define the list of Hebrew keywords and their English translations
keywords = {
    'הדפס': 'print',
    'אם': 'if',
    'אחרת': 'else',
    'עבור': 'for',
    'בתוך': 'in',
    'תנאי': 'condition',
    'משתנה':'avr',
}

# Define the tokens for the lexer
tokens = [
    'PRINT',
    'IF',
    'ELSE',
    'FOR',
    'IN',
    'CONDITION',
    'STRING',
    'VAR',
]

# Token rules
t_PRINT = r'הדפס'
t_VAR = r'משתנה'
t_IF = r'אם'
t_ELSE = r'אחרת'
t_FOR = r'עבור'
t_IN = r'בתוך'
t_CONDITION = r'תנאי'
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
    p[0] = 'print(' + p[2] + ')'

def p_statement_if(p):
    'statement : IF condition'
    p[0] = 'if ' + p[2] + ':'

def p_statement_if_else(p):
    'statement : IF condition ELSE'
    p[0] = 'if ' + p[2] + ':'
    p[0] += '\n\t# Code for the if block'
    p[0] += '\nelse:'
    p[0] += '\n\t# Code for the else block'

# def p_statement_for(p):
#     'statement : FOR ID IN ID'
#     p[0] = 'for ' + p[2] + ' in ' + p[4] + ':'

def p_condition(p):
    'condition : CONDITION'
    p[0] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc()

# Test program
program = '''
הדפס("התחלת התוכנית")

עבור משתנה בתוך רשימה:
    אם משתנה == 3:
        הדפס("המשתנה הוא 3")
    אחרת:
        הדפס("המשתנה אינו 3")

הדפס("סיום התוכנית")
'''

print("lexer:")
# Lex and parse the program
lexer.input(program)
for token in lexer:
    print(token)
print("----")

print("parser:")
result = parser.parse(program)
print(result)
print("-----")