import ply.yacc as yacc
from lexing.lexer import lexer, tokens
from semantic.my_ast import Num, BinOp, Print, Str, VarAssign, Var, If, Else, While, For, List
from code_gen.code_generator import generate_code

precedence = (
    ("right", "EQUAL"),
    ('left', 'PLUS', 'MINUS', 'STAR', 'SLASH'),
    ('left', 'GREATER', 'LESS', 'EQUAL_EQUAL', 'NOT_EQUAL', 'GREATER_EQUAL', 'LESS_EQUAL'),
)

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''
    statement : assignment
              | print_statement
              | if_statement
              | while_statement
              | for_statement
              | NEWLINE
    '''
    p[0] = p[1]

def p_while_statement(p):
    '''
    while_statement : WHILE expression COLON statements
    '''
    p[0] = While(p[2], p[4])

def p_for_statement(p):
    '''
    for_statement : FOR VARIABLE IN expression COLON statements
    '''
    p[0] = For(Var(p[2]), p[4], p[6])

def p_print_statement(p):
    '''
    print_statement : PRINT LEFT_PAREN expression RIGHT_PAREN
    '''
    p[0] = Print(p[3])

def p_assignment(p):
    '''
    assignment : VARIABLE EQUAL expression
               | VARIABLE EQUAL STRING
               | VARIABLE EQUAL NUMBER
    '''
    if isinstance(p[3], (int, float)):
        p[0] = VarAssign(p[1], Num(p[3]))
    elif isinstance(p[3], str) and p[3].isdigit():
        p[0] = VarAssign(p[1], Num(int(p[3])))
    elif isinstance(p[3], str):
        p[0] = VarAssign(p[1], Str(p[3]))
    else:
        p[0] = VarAssign(p[1], p[3])

def p_expression(p):
    '''
    expression : term
               | expression PLUS term
               | expression MINUS term
               | expression STAR term
               | expression SLASH term
               | expression GREATER term
               | expression LESS term
               | expression EQUAL_EQUAL term
               | expression NOT_EQUAL term
               | expression GREATER_EQUAL term
               | expression LESS_EQUAL term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinOp(p[1], p[2], p[3])

def p_term(p):
    '''
    term : NUMBER
         | STRING
         | VARIABLE
         | FLOAT
         | list
    '''
    if p.slice[1].type == 'NUMBER' or p.slice[1].type == 'FLOAT':
        p[0] = Num(p[1])
    elif p.slice[1].type == 'STRING':
        p[0] = Str(p[1])
    elif p.slice[1].type == 'VARIABLE':
        p[0] = Var(p[1])
    elif p.slice[1].type == 'list':
        p[0] = p[1]
    else:
        p[0] = p[1]

def p_list(p):
    '''
    list : LEFT_BRACKET elements RIGHT_BRACKET
    '''
    p[0] = List(p[2])

def p_elements(p):
    '''
    elements : expression
             | elements COMMA expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_if_statement(p):
    '''
    if_statement : IF expression COLON statements else_statement
    '''
    p[0] = If(p[2], p[4], p[5])

def p_else_statement(p):
    '''
    else_statement :
                  | ELSE COLON statements
    '''
    if len(p) == 4:
        p[0] = Else(p[3])
    else:
        p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}'")
    else:
        print("Syntax error at EOF")

def p_variable_assignment(p):
    '''
    variable_assignment : VARIABLE EQUAL expression
    '''
    p[0] = VarAssign(p[1], p[3])

def p_variable(p):
    '''
    variable : VARIABLE
    '''
    p[0] = Var(p[1])

def p_expression_var(p):
    '''
    expression : variable
    '''
    p[0] = p[1]

parser = yacc.yacc()

# # דוגמאות קוד לבדיקה
# input_code1 = '''
# הדפס("----------------")
# הדפס("שלום עולם!!")
# '''
# input_code2 = '''
# נעמה = 30-20
# מיכל = 2*5
# הדפס("----------------")
# הדפס(נעמה*מיכל)
# '''
# input_code3 = '''
# נעמה=10*10
# מיכל=200/2
#
# אם נעמה + מיכל >=100 :
# הדפס("----------------")
#     הדפס ("נעמה ומיכל")
# אחרת:
# הדפס("----------------")
#     הדפס ("קטנטת מ100")
# '''
# input_code4 = '''
# נעמה = 1
# בעוד נעמה < 50 :
# הדפס(נעמה)
# נעמה = נעמה + 1
# '''
#
# input_code5 = '''
# עבור משתנה ב [1, 2, 3, 4, 5]:
#     הדפס( משתנה)
# '''
