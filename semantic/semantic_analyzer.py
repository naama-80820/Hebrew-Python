from semantic.my_ast import Num, BinOp, Print, Str, VarAssign, Var, If, Else, While, For, List

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def visit(self, node):
        if isinstance(node, Num):
            return "number"
        elif isinstance(node, Str):
            return "string"
        elif isinstance(node, Var):
            if node.name in self.symbol_table:
                return self.symbol_table[node.name]
            else:
                raise Exception(f"Undefined variable '{node.name}'")
        elif isinstance(node, VarAssign):
            var_type = self.visit(node.value)
            self.symbol_table[node.name] = var_type
            return var_type
        elif isinstance(node, BinOp):
            left_type = self.visit(node.left)
            right_type = self.visit(node.right)
            if left_type != right_type:
                raise Exception(f"Type mismatch: {left_type} and {right_type}")
            return left_type
        elif isinstance(node, Print):
            return self.visit(node.value)
        elif isinstance(node, If):
            condition_type = self.visit(node.condition)
            if condition_type != "number":
                raise Exception(f"If condition must be a number, got {condition_type}")
            for stmt in node.then_body:
                self.visit(stmt)
            if node.else_body:
                for stmt in node.else_body:
                    self.visit(stmt)
            return None
        elif isinstance(node, While):
            condition_type = self.visit(node.condition)
            if condition_type != "number":
                raise Exception(f"While condition must be a number, got {condition_type}")
            for stmt in node.body:
                self.visit(stmt)
            return None
        elif isinstance(node, For):
            iterable_type = self.visit(node.iterable)
            if iterable_type != "number":  # Assuming we only deal with lists of numbers
                raise Exception(f"For loop iterable must be a list of numbers, got {iterable_type}")
            for stmt in node.body:
                self.visit(stmt)
            return None
        elif isinstance(node, List):
            element_types = set(self.visit(element) for element in node.elements)
            if len(element_types) > 1:
                raise Exception(f"List elements must be of the same type, got {element_types}")
            return "number"  # Assuming we only deal with lists of numbers
        else:
            raise Exception(f"Unknown node type {type(node)}")

