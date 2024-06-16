import ply.lex as lex

reserved_words = {
    'הדפס': 'PRINT',
    'אם': 'IF',
    'אחרת': 'ELSE',
    'בעוד': 'WHILE',
    'עבור': 'FOR',
    'ב': 'IN',
}

tokens = [
    "LEFT_PAREN",
    "RIGHT_PAREN",
    "LEFT_BRACKET",
    "RIGHT_BRACKET",
    "COMMA",
    "MINUS",
    "PLUS",
    "SLASH",
    "STAR",
    "COLON",
    "EQUAL",
    'EQUAL_EQUAL',
    'NOT_EQUAL',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    "NUMBER",
    "FLOAT",
    "STRING",
    "VARIABLE",
    "NEWLINE",
] + list(reserved_words.values())

# Regular expression rules for simple tokens
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_COMMA = r','
t_MINUS = r'-'
t_PLUS = r'\+'
t_SLASH = r'/'
t_STAR = r'\*'
t_COLON = r':'
t_EQUAL = r'='
t_EQUAL_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='

def t_RESERVED_WORDS(t):
    r'(הדפס|אם|אחרת|בעוד|עבור|ב)'
    t.type = reserved_words.get(t.value, 'RESERVED_WORDS')
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_VARIABLE(t):
    r'[א-ת_]+[א-ת0-9_]*'
    t.type = reserved_words.get(t.value, 'VARIABLE')
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
