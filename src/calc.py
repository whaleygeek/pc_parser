# calc.py  17/01/2016  D.J.Whale

#----- ERROR HANDLERS ---------------------------------------------------------

def t_error(t):
    """Token error"""
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_error(p):
    """Parser error"""""
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


#----- RUN --------------------------------------------------------------------

# Build the lexer
#print("building lexer")
from calc_lexer import *

import ply.lex as lex
lex.lex()


# Build the parser
#print("building parser")
from calc_parser import * # this is the generated parser

import ply.yacc as yacc
yacc.yacc()


#print("running")

while True:
    try:
        s = raw_input('calc> ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)

# END
