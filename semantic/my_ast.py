class Node:
    pass
class Num:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Num({self.value})"

class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Print(Node):
    def __init__(self, value):
        self.value = value

class Str(Node):
    def __init__(self, value):
        self.value = value

class VarAssign(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Var(Node):
    def __init__(self, name):
        self.name = name

class If(Node):
    def __init__(self, condition, then_body, else_body):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

class Else(Node):
    def __init__(self, body):
        self.body = body

class While(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class For(Node):
    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body

class List(Node):
    def __init__(self, elements):
        self.elements = elements
