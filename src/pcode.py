# pcode.py  17/01/2016  D.J.Whale

import sys


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


#----- CONFIGURABLE EMITTER ---------------------------------------------------

def emit(msg):
    """Configurable emit handler"""
    # Change this to send output to anywhere else
    print(msg)


#----- BUILD PARSER -----------------------------------------------------------

# Build the lexer
from pcode_lexer import *
import ply.lex as lex
lex.lex()


# Build the back-end generator
#TODO: parse command line args to get name of backend generator
# import the module by name
# python pcode.py lang=c      cgen
# python pcode.py lang=py     pygen
# python pcode.py lang=java   javagen
# python pcode.py lang=php    phpgen
# python pcode.py lang=bash   bashgen
# python pcode.py lang=lua    luagen
# python pcode.py lang=ruby   rubygen
# python pcode.py lang=sql    sqlgen  # i.e. sql procedures and functions
# python pcode.py lang=cpp    cppgen  # cplusplus

import pygen
#import cgen

# Build the parser
from pcode_parser import * # this is the generated parser

import ply.yacc as yacc
y = yacc.yacc()


#----- RUN --------------------------------------------------------------------

buffer = ""

def test(src, mockio=False):
    """Run the src through the parser, capture the generated output and return it"""
    global buffer

    def bufemit(msg):
        global buffer
        buffer += msg
        buffer += '\n'

    global emit
    emit = bufemit

    if mockio:
        mock_translate(src)
    else:
        translate(src)
    b = buffer
    buffer = ""
    return b

def mock_translate(src):
    """A version of translate that mocks a few things, like IO"""
    generator = pygen.MockGenerator(emit=emit)
    #generator = cgen.MockGenerator(emit=emit)
    ###TODO: switchable back end switches here
    set_backend(generator)

    y.parse(src)
    y.restart()

def translate(src):
    generator = pygen.Generator(emit=emit)
    #generator = cgen.Generator(emit=emit) # TESTING
    #generator = cgen.Generator(emit=emit)
    ###TODO: switchable back end switches here
    set_backend(generator)

    y.parse(src)
    y.restart()

def interactive():
    """interactive mode from terminal"""

    PROMPT = "pcode> "
    while True:
        try:
            s = raw_input(PROMPT)
        except EOFError:
            break
        if not s: continue
        translate(s)

def batch():
    """Batch mode from stdin"""

    # Read whole of stdin into a string
    s = ""
    while True:
        line = sys.stdin.read()
        if line != "":
            s += line
        else:
            break

    # Now parse and generate
    translate(s)


#----- MAIN -------------------------------------------------------------------

if __name__ == "__main__":
    if sys.stdin.isatty():
        interactive()
    else:
        batch()

# END
