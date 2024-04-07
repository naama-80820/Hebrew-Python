import ply.yacc as yacc
from lexing import lexer
from ast import *

tokens = lexer.tokens

# Parsing rules

# Define other token rules (number, string, identifier)
def t_NUMBER(t):
    r"\d+"
    t.value=int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.lexer.lineno+=t.value.count("\n")
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z_א-ת][a-zA-Z_0-9_א-ת]*"
    t.type = reserved.get(t.value, "IDENTIFIER")  # Check for reserved words
    return t

#סוגי משפטים
def p_statement(p):
    '''statement : expression_statement
                 | function_declaration
                 | print_statement
                 | if_statement
                 | for_loop
                 | while_loop
                 | continue_statement
                 | break_statement
                 | return_statement
                '''
    p[0] = p[1]
# | variable_declaration

# Parsing rules for reserved keywords
def p_function_declaration(p):
    'function_declaration : DEF IDENTIFIER LEFT_PAREN parameter_list RIGHT_PAREN COLON statement'
    p[0] = FunctionDeclarationNode(p[2], p[4], p[7])

def p_print_statement(p):
    'print_statement : PRINT LEFT_PAREN expression_statement RIGHT_PAREN '
    p[0] = PrintStatementNode(p[2])

def p_if_statement(p):
    'if_statement : IF expression COLON statement ELSE COLON statement'
    p[0] = IfStatementNode(p[2], p[4], p[7])

def p_for_loop(p):
    'for_loop : FOR IDENTIFIER IN expression_statement COLON statement'
    p[0] = ForLoopNode(p[2], p[4], p[6])

def p_while_loop(p):
    'while_loop : WHILE expression COLON statement'
    p[0] = WhileLoopNode(p[2], p[4])

def p_continue_statement(p):
    'continue_statement : CONTINUE'
    p[0] = ContinueStatementNode()

def p_break_statement(p):
    'break_statement : BREAK'
    p[0] = BreakStatementNode()

def p_return_statement(p):
    'return_statement : RETURN expression'
    p[0] = ReturnStatementNode(p[2])


# מגדיר את רשימת הפרמטרים שמועברים לפונקציה
def p_parameter_list(p):
    '''parameter_list : parameter_list
                      | parameter_list COMMA parameter
                      | NONE'''
    if len(p) == 4:
        p[0]=[p[1]] + p[3]
    elif len(p) == 2:
        if p[1] is None:
            p[0]=[]
        else:
            p[0]=[p[1]]

def p_parameter_list_single(p):
    'parameter_list : IDENTIFIER'
    p[0] = [p[1]]


#אופרטורים וסימנים
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression STAR expression
                  | expression SLASH expression



                  | NOT expression
                  | expression BANG_EQUAL expression
                  | expression EQUAL_EQUAL expression
                  | expression GREATER expression
                  | expression GREATER_EQUAL expression
                  | expression LESS expression
                  | expression LESS_EQUAL expression
                  | expression ARROW expression
                  | LEFT_PAREN expression RIGHT_PAREN
                  | LEFT_BRACE expression RIGHT_BRACE
                  | LEFT_BRACKET expression RIGHT_BRACKET
                  | expression COMMA expression
                  | expression DOT expression
                  | expression QUESTION expression
                  | expression COLON expression'''

# | expression MODULO expression
# | expression LEFT_SHIFT expression
# | expression RIGHT_SHIFT expression
# | primary_expression

def p_bitwise_or_expression(p):
    '''bitwise_or_expression : bitwise_xor_expression
                              | bitwise_or_expression '|' bitwise_xor_expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOperationNode(p[2], p[1], p[3])


def p_bitwise_xor_expression(p):
    '''bitwise_xor_expression : bitwise_and_expression
                               | bitwise_xor_expression '^' bitwise_and_expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOperationNode(p[2], p[1], p[3])


def p_bitwise_and_expression(p):
    '''bitwise_and_expression : comparison_expression
                               | bitwise_and_expression '&' comparison_expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOperationNode(p[2], p[1], p[3])


# def p_comparison_expression(p):
#     '''comparison_expression : shift_expression
#                               | comparison_expression comp_operator shift_expression'''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = BinaryOperationNode(p[2], p[1], p[3])
#


# def p_shift_expression(p):
#     '''shift_expression : additive_expression
#                         | shift_expression LEFT_SHIFT additive_expression
#                         | shift_expression RIGHT_SHIFT additive_expression'''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = BinaryOperationNode(p[2], p[1], p[3])
#
#
# def p_additive_expression(p):
#     '''additive_expression : multiplicative_expression
#                            | additive_expression PLUS multiplicative_expression
#                            | additive_expression MINUS multiplicative_expression'''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = BinaryOperationNode(p[2], p[1], p[3])


def p_multiplicative_expression(p):
    '''multiplicative_expression : unary_expression
                                  | multiplicative_expression TIMES unary_expression
                                  | multiplicative_expression DIVIDE unary_expression
                                  | multiplicative_expression MODULO unary_expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryOperationNode(p[2], p[1], p[3])

def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

# Test the parser with an example input
input_code = '''
print(1 + 2 * 3)
'''
parser.parse(input_code)
