# pcode_lexer.py  17/01/2016  D.J.Whale

"""
whitespace 0 or more: [space, tab, newline]

# comment strips to next newline

" " STRLIT??
"""

# token list
tokens = (
'NAME',         'NUMBER',

'IF',           'THEN',         'ELSE',         'ENDIF',        'WHILE',
'ENDWHILE',     'CASE',         'OF',           'ENDCASE',      'FOR',
'TO',           'ENDFOR',       'REPEAT',       'UNTIL',        'FUNCTION',
'ENDFUNCTION',  'RETURN',       'PROCEDURE',    'ENDPROCEDURE', 'READLINE',
'WRITELINE',    'OUTPUT',       'USERINPUT',    'LEN',          'MOD',
'NOT',          'FALSE',        'TRUE',         'AND',          'OR',
'XOR',          'PLUS',         'MINUS',        'TIMES',        'DIVIDE',
'EQUAL',        'NOTEQUAL',     'LESS',         'LESSEQUAL',    'GREATER',
'GREATEREQUAL', 'ASSIGN',       'LPAREN',       'RPAREN',       'LSQUARE',
'RSQUARE',      'COMMA',        'COLON',        'QUOTE',        'RETURN',
'TRUE',         'FALSE',        'NAME'
)

# literals list
# NOTE: yply generator generates invalid code if you use ')' at the end of a line
# TODO: probably just worth fixing this, we could then use literals for 'IF' etc
#   which makes the code much shorter. Could fix and test this in the calculator
#   example first.

#literals = ['=','+','-','*','/', '(',')']


# token definitions

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#t_EQUALS    = r'='
#t_LPAREN    = r'\('
#t_RPAREN    = r'\)'
#t_PLUS      = r'\+'
#t_MINUS     = r'\-'
#t_TIMES     = r'\*'
#t_DIVIDE    = r'/'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# END




