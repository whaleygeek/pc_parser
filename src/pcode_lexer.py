# pcode_lexer.py  17/01/2016  D.J.Whale

# token list
tokens = (
'PLUS',         'MINUS',        'TIMES',        'DIVIDE',
'EQUAL',        'NOTEQUAL',     'LESS',         'LESSEQUAL',    'GREATER',
'GREATEREQUAL', 'ASSIGN',       'LPAREN',       'RPAREN',       'LSQUARE',
'RSQUARE',      'COMMA',        'COLON',

'IF',           'THEN',         'ELSE',         'ENDIF',        'WHILE',
'ENDWHILE',     'CASE',         'OF',           'ENDCASE',      'FOR',
'TO',           'ENDFOR',       'REPEAT',       'UNTIL',        'FUNCTION',
'ENDFUNCTION',  'RETURN',       'PROCEDURE',    'ENDPROCEDURE', 'READLINE',
'WRITELINE',    'OUTPUT',       'USERINPUT',    'LEN',          'MOD',
'NOT',          'FALSE',        'TRUE',         'AND',          'OR',
'XOR',          'RETURN',

'NAME',         'NUMBER',       'STRLIT'
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
t_COMMA         = r','
t_COLON         = r':'

t_IF            = r'IF'
t_THEN          = r'THEN'
t_ELSE          = r'ELSE'
t_ENDIF         = r'ENDIF'
t_WHILE         = r'WHILE'
t_ENDWHILE      = r'ENDWHILE'
t_CASE          = r'CASE'
t_OF            = r'OF'
t_ENDCASE       = r'ENDCASE'
t_FOR           = r'FOR'
t_TO            = r'TO'
t_ENDFOR        = r'ENDFOR'
t_REPEAT        = r'REPEAT'
t_UNTIL         = r'UNTIL'
t_FUNCTION      = r'FUNCTION'
t_ENDFUNCTION   = r'ENDFUNCTION'
t_RETURN        = r'RETURN'
t_PROCEDURE     = r'PROCEDURE'
t_ENDPROCEDURE  = r'ENDPROCEDURE'
t_READLINE      = r'READLINE'
t_WRITELINE     = r'WRITELINE'
t_OUTPUT        = r'OUTPUT'
t_USERINPUT     = r'USERINPUT'
t_LEN           = r'LEN'
t_MOD           = r'MOD'
t_NOT           = r'NOT'
t_FALSE         = r'FALSE'
t_TRUE          = r'TRUE'
t_AND           = r'AND'
t_OR            = r'OR'
t_XOR           = r'XOR'
t_RETURN        = r'RETURN'

t_NAME          = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_STRLIT        = r'\"[^\"]*\"'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_comment(t):
    r'#[^\n]*\n$'
    print("comment:%s" % str(t))

# END




