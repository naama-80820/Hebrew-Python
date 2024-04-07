import ply.lex as lex

# Reserved keywords
reserved_words = {
    "פונקציה": "DEF",
    "הדפס": "PRINT",
    "אם": "IF",
    "אחרת": "ELSE",
    "עבור": "FOR",
    "בתוך": "IN",
    "בזמן": "WHILE",
    "המשך": "CONTINUE",
    "שבירה": "BREAK",
    "החזר": "RETURN",
    "כלום": "NONE",
    "לא": "NOT",
}

# Define tokens list
tokens = [
    # Single character
    "LEFT_PAREN",
    "RIGHT_PAREN",
    "LEFT_BRACE",
    "RIGHT_BRACE",
    "LEFT_BRACKET",
    "RIGHT_BRACKET",
    "COMMA",
    "DOT",
    "MINUS",
    "PLUS",
    "SEMICOLON",
    "SLASH",
    "STAR",
    "COLON",
    "QUESTION",
 #   "COMMENT",
    # One or two characters
    "BANG",
    "BANG_EQUAL",
    "EQUAL",
    "EQUAL_EQUAL",
    "GREATER",
    "GREATER_EQUAL",
    "LESS",
    "LESS_EQUAL",
    "ARROW",
    # Literals
    "IDENTIFIER",
    "STRING",
    "NUMBER",
    # Additional tokens

] + list(reserved_words.values())

# Define individual token rules
t_LEFT_PAREN = r"\("
t_RIGHT_PAREN = r"\)"
t_LEFT_BRACE = r"\{"
t_RIGHT_BRACE = r"\}"
t_LEFT_BRACKET = r"\["
t_RIGHT_BRACKET = r"\]"
t_COMMA = r"\,"
t_DOT = r"\."
t_PLUS = r"\+"
t_MINUS = r"\-"
t_SEMICOLON = r"\;"
t_SLASH = r"\/"
t_STAR = r"\*"
t_COLON = r"\:"
t_QUESTION = r"\?"
#t_COMMENT = r"\#"

t_BANG = r"\!"
t_BANG_EQUAL = r"\!\="
t_EQUAL = r"\="
t_EQUAL_EQUAL = r"\=\="
t_GREATER = r"\>"
t_GREATER_EQUAL = r"\>\="
t_LESS = r"\<"
t_LESS_EQUAL = r"\<\="
t_ARROW = r"\-\>"

#הערה
def t_COMMENT(t):
    r"\#.*"
    pass  # Ignore comments, do not return any token

#מזההים
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value[0].isdigit():  # Check if the identifier starts with a digit
        print("Invalid identifier: Identifier cannot start with a digit")
        t.lexer.skip(1)  # Skip the invalid character
        return None
    elif t.value.isdigit():  # Check if the identifier contains only digits
        print("Invalid identifier: Identifier cannot contain only digits")
        t.lexer.skip(1)  # Skip the invalid character
        return None
    else:
        return t

# מילים שמורות
def t_KEYWORD(t):
    r'[א-ת]+'
    t.type = reserved_words.get(t.value, 'KEYWORD')
    return t





# Define other token rules (number, string, identifier)
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)# Function to handle regular identifiers


def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.lexer.lineno += t.value.count("\n")
    return t

# Match reserved keywords


# Define ignored characters and error handling
t_ignore = " \t\f\r"
t_ignore_comment = r"\/\/[^\n]*"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
