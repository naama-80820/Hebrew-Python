# Parsing rules

import ply.yacc as yacc
from lexing import lexer

tokens = lexer.tokens

# Function to identifiers
def p_statement_regular_identifier(p):
    '''
    statement : IDENTIFIER
    '''
    p[0]=("IDENTIFIER", p[1])

# Function to reserved words
def p_statement_reserved_word(p):
    '''
    statement : RESERVED_WORD
    '''
    p[0]=(reserved_words[p[1]], p[1])

# Function
def p_function_declaration(p):
    'function_declaration : DEF IDENTIFIER LEFT_PAREN parameter_list RIGHT_PAREN COLON statement'
    p[0]=FunctionDeclarationNode(p[2], p[4], p[7])


# Parsing rules for loop constructs
# הֶסבֵּר:
# - `p_for_loop`: כלל זה מטפל בניתוח של לולאות `for`. הוא כולל חלופות עבור איטרטורים בודדים וכפולים כאחד. גוף הלולאה מוקף בסוגרים `{}`.
# - `p_while_loop`: כלל זה מטפל בניתוח של לולאות `while`. גוף הלולאה מוקף בסוגרים `{}`.
# - `p_iterable`: כלל זה מטפל בסוגים שונים של איטרבלים שניתן להשתמש בהם בלולאות `for`, כולל ביטויים, טווחים ואוספים (למשל, רשימות).
# - `p_range`: כלל זה מטפל בניתוח של ביטויי טווח המשמשים בלולאות `for`. זה מאפשר סעיפי 'BY' אופציונליים כדי לציין את גודל הצעד.
# - `p_collection`: כלל זה מטפל בניתוח מילולי אוסף, כגון רשימות, המשמשים בלולאות `for`.
# - `p_items`: כלל זה מטפל בניתוח של פריטים מופרדים בפסיק בתוך אוסף מילולי.
def p_for_loop(p):
    """
    for_loop : FOR IDENTIFIER IN iterable LEFT_BRACE stmt_list RIGHT_BRACE
            | FOR IDENTIFIER COMMA IDENTIFIER IN iterable LEFT_BRACE stmt_list RIGHT_BRACE
    """
    if len(p) == 8:
        p[0] = ForLoop(variable=p[2], iterable=p[4], body=p[6])
    else:
        p[0] = ForLoop(iterator1=p[2], iterator2=p[4], iterable=p[6], body=p[8])


def p_while_loop(p):
    """
    while_loop : WHILE condition LEFT_BRACE stmt_list RIGHT_BRACE
    """
    p[0] = WhileLoop(condition=p[2], body=p[4])


def p_iterable(p):
    """
    iterable : expression
             | range
             | collection
    """
    p[0] = p[1]



def p_range(p):
    """
    range : expression TO expression
          | expression TO expression BY expression
    """
    if len(p) == 4:
        p[0] = Range(start=p[1], stop=p[3], step=1)
    else:
        p[0] = Range(start=p[1], stop=p[3], step=p[5])


def p_collection(p):
    """
    collection : '[' items ']'
    """
    p[0] = p[2]


def p_items(p):
    """
    items : expression
          | items COMMA expression
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


# Build the parser
parser = yacc.yacc()

# Test the parser with an example input
input_code = '''
print(1 + 2 * 3)
'''
parser.parse(input_code)

