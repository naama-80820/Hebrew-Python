from parsing import parser
class ASTNode:
    pass

class BinaryOperationNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class UnaryOperationNode(ASTNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name

class AssignmentNode(ASTNode):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

class PrintStatementNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class FunctionDeclarationNode(ASTNode):
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

class FunctionCallNode(ASTNode):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

class BlockNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements
