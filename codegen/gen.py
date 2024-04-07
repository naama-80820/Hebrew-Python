# codegen.py

from ast import *

def generate_code(node):
    if isinstance(node, ProgramNode):
        # Generate code for each statement in the program
        code = ""
        for statement in node.statements:
            code += generate_code(statement) + "\n"
        return code
    elif isinstance(node, VariableDeclarationNode):
        return f"{node.identifier} = {generate_code(node.expression)}"
    elif isinstance(node, FunctionDeclarationNode):
        parameters = ", ".join(node.parameters)
        body_code = generate_code(node.body)
        return f"def {node.identifier}({parameters}):\n{indent(body_code)}"
    elif isinstance(node, BinaryOperationNode):
        left = generate_code(node.left)
        right = generate_code(node.right)
        operator = {
            TokenType.PLUS: '+',
            TokenType.MINUS: '-',
            TokenType.STAR: '*',
            TokenType.SLASH: '/',
            TokenType.EQUAL_EQUAL: '==',
            # Add more operators as needed
        }.get(node.operator)
        return f"({left} {operator} {right})"
    elif isinstance(node, NumberNode):
        return str(node.value)
    elif isinstance(node, IdentifierNode):
        return node.name
    elif isinstance(node, PrintStatementNode):
        expression_code = generate_code(node.expression)
        return f"print({expression_code})"
    elif isinstance(node, BlockNode):
        # Generate code for a block of statements
        code = ""
        for statement in node.statements:
            code += generate_code(statement) + "\n"
        return code
    elif isinstance(node, AssignmentNode):
        return f"{node.identifier} = {generate_code(node.expression)}"
    elif isinstance(node, UnaryOperationNode):
        operand_code = generate_code(node.operand)
        operator = {
            TokenType.MINUS: '-',
            TokenType.PLUS: '+',
            # Add more unary operators as needed
        }.get(node.operator)
        return f"{operator}{operand_code}"
    elif isinstance(node, FunctionCallNode):
        arguments_code = ", ".join(generate_code(arg) for arg in node.arguments)
        return f"{node.name}({arguments_code})"
    else:
        raise RuntimeError(f"Unknown AST node type: {type(node)}")

def indent(code, num_spaces=4):
    lines = code.split('\n')
    indented_code = ""
    for line in lines:
        indented_code += " " * num_spaces + line + "\n"
    return indented_code.strip()

# Example usage:
# ast = ...  # Your AST instance
# python_code = generate_code(ast)
# print(python_code)
