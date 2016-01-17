# calc_lexer.py  17/01/2016  D.J.Whale

# token list
tokens = (
    'NAME','NUMBER', 'EQUALS', 'LPAREN', 'RPAREN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE'
    )

# yply generator generates invalid code if you use ')' at the end of a line
#literals = ['=','+','-','*','/', '(',')']


# token definitions

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_EQUALS    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# END
