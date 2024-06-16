from semantic.my_ast import Num, BinOp, Print, Str, VarAssign, Var, If, Else, While, For,List

def generate_code(node):
    if isinstance(node, Num):
        return str(node.value)
    elif isinstance(node, Str):
        return f'"{node.value}"'
    elif isinstance(node, Var):
        return node.name
    elif isinstance(node, VarAssign):
        return f"{node.name} = {generate_code(node.value)}"
    elif isinstance(node, BinOp):
        return f"{generate_code(node.left)} {node.op} {generate_code(node.right)}"
    elif isinstance(node, Print):
        return f"print({generate_code(node.value)})"
    elif isinstance(node, If):
        code = f"if {generate_code(node.condition)}:\n"
        for stmt in node.then_body:
            code += f"    {generate_code(stmt)}\n"
        if node.else_body:
            code += "else:\n"
            for stmt in node.else_body.body:
                code += f"    {generate_code(stmt)}\n"
        return code
    elif isinstance(node, While):
        code = f"while {generate_code(node.condition)}:\n"
        for stmt in node.body:
            code += f"    {generate_code(stmt)}\n"
        return code
    elif isinstance(node, For):
        code = f"for {generate_code(node.variable)} in {generate_code(node.iterable)}:\n"
        for stmt in node.body:
            code += f"    {generate_code(stmt)}\n"
        return code
    elif isinstance(node, List):
        return f"[{', '.join(generate_code(element) for element in node.elements)}]"
    return ""

