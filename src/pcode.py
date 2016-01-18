# pcode.py  17/01/2016  D.J.Whale

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
from pcode_lexer import *

import ply.lex as lex
lex.lex()


# Build the parser
#print("building parser")
from pcode_parser import * # this is the generated parser

#TODO: parse command line args to get name of backend generator
# import the module by name
# call code in pcode_parser that sets it's emit instance.

import pygen
generator = pygen.Generator()
set_backend(generator)

import ply.yacc as yacc
yacc.yacc()

#print("running")

import sys

if sys.stdin.isatty():
    # interactive mode
    PROMPT = "pcode> "
    while True:
        #TODO should just read STDIN and pass whole lines to yacc.parse()
        #For now, let's use it interactively, to aid testing
        try:
            s = raw_input(PROMPT)
        except EOFError:
            break
        if not s: continue
        yacc.parse(s)
else:
    # file mode
    s = ""
    while True:
        line = sys.stdin.read()
        if line != "":
            s += line
        else:
            break

    yacc.parse(s)


# END
