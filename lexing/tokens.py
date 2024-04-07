from ply.lex import TOKEN
class TokenType:
    # Single character
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    LEFT_BRACE = "LEFT_BRACE"
    RIGHT_BRACE = "RIGHT_BRACE"
    LEFT_BRACKET = "LEFT_BRACKET"
    RIGHT_BRACKET = "RIGHT_BRACKET"
    COMMA = "COMMA"
    DOT = "DOT"
    MINUS = "MINUS"
    PLUS = "PLUS"
    SEMICOLON = "SEMICOLON"
    SLASH = "SLASH"
    STAR = "STAR"
    COLON = "COLON"
    QUESTION = "QUESTION"
    COMMENT = "COMMENT"
    # One or two characters
    BANG = "BANG"
    BANG_EQUAL = "BANG_EQUAL"
    EQUAL = "EQUAL"
    EQUAL_EQUAL = "EQUAL_EQUAL"
    GREATER = "GREATER"
    GREATER_EQUAL = "GREATER_EQUAL"
    LESS = "LESS"
    LESS_EQUAL = "LESS_EQUAL"
    ARROW = "ARROW"

    # Literals
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"

    # Keywords

    DEF = "פונקציה"
    PRINT ="הדפס"
    FALSE="שקר"
    TRUE="אמת"
    NONE="כלום"
    AND=  "וגם"
    ASSERT="לא  עכשיו"
    AWAIT="חכה"
    BREAK= "שבור"
    CLASS="מחלקה"
    CONTINUE=  "המשך"
    ELIF="אליפ"
    ELSE="אחרת"
    EXCEPT="חוץ"
    FOR="לולאה"
    FROM= "מ"
    GLOBAL= "גלובלי"
    IF="אם"
    IMPORT="יבא"
    IN="בתוך"
    IS="לא יודעת"
    LAMBDA="למבדה"
    NONLOCAL="לא מקומי"
    NOT="לא"
    OR="או"
    PASS="לעבור"
    RAISE= "להצביע "
    RETURN="החזר "
    # EOF
    # EOF = "EOF"


class Token:
    def __init__(self, type: TokenType, lex: str, literal: object, line: int) -> None:
        self.type = type
        self.lexeme = lex
        self.literal = literal
        self.line = line

    def __repr__(self) -> str:
        return f"{self.lexeme}"