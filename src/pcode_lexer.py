# pcode_lexer.py  17/01/2016  D.J.Whale

keywords = (
'IF',           'THEN',         'ELSE',         'ENDIF',        'WHILE',
'ENDWHILE',     'CASE',         'OF',           'ENDCASE',      'FOR',
'TO',           'ENDFOR',       'REPEAT',       'UNTIL',        'FUNCTION',
'ENDFUNCTION',  'RETURN',       'PROCEDURE',    'ENDPROCEDURE', 'READLINE',
'WRITELINE',    'OUTPUT',       'USERINPUT',    'LEN',          'MOD',
'NOT',          'FALSE',        'TRUE',         'AND',          'OR',
'XOR', 'WHEN'
)

tokens = keywords + (
'PLUS',         'MINUS',        'TIMES',        'DIVIDE',
'EQUAL',        'NOTEQUAL',     'LESS',         'LESSEQUAL',    'GREATER',
'GREATEREQUAL', 'ASSIGN',       'LPAREN',       'RPAREN',       'LSQUARE',
'RSQUARE',      'COMMA',        'COLON',        'COMMENT',

'ID',           'NUMBER',       'STRING'
)

# token definitions

t_PLUS          = r'\+'
t_MINUS         = r'\-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
t_EQUAL         = r'='
t_NOTEQUAL      = r'<>'
t_LESS          = r'<'
t_LESSEQUAL     = r'<='
t_GREATER       = r'>'
t_GREATEREQUAL  = r'>='
t_ASSIGN        = r'<-'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_LSQUARE       = r'\['
t_RSQUARE       = r'\]'
t_COMMA         = r'\,'
t_COLON         = r':'

def t_comment(t):
    r"[ ]*\043[^\n]*"  # \043 is '#'
    pass

def t_STRING(t):
    r'\".*?\"'
    #t.value = t.value[1:-1] # remove quotes
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    else:
        class Identifier():
            def __init__(self, name):
                self.name = name
            def __repr__(self):
                return self.name

        t.value = Identifier(t.value)
    return t

#def t_COMMENT(t):
#    r'#.*'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# END




