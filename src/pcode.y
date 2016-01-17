/* pcode.y  17/01/2016  D.J.Whale */

%token PLUS MINUS TIMES DIVIDE
%token EQUAL NOTEQUAL LESS LESSEQUAL GREATER
%token GREATEREQUAL ASSIGN LPAREN RPAREN LSQUARE
%token RSQUARE COMMA COLON

%token IF THEN ELSE ENDIF WHILE
%token ENDWHILE CASE OF ENDCASE FOR
%token TO ENDFOR REPEAT UNTIL FUNCTION
%token ENDFUNCTION RETURN PROCEDURE ENDPROCEDURE READLINE
%token WRITELINE OUTPUT USERINPUT LEN MOD
%token NOT FALSE TRUE AND OR
%token XOR RETURN

%token NAME NUMBER STRLIT

%start program


%%

program:
    statements
    ;

statements:
      /* empty */
    | statement
    | statements statement
    ;

statement:
      if-statement
    | while-statement
    | case-statement
    | for-statement
    | repeat-statement
    | function-def-statement
    | return-statement
    | proc-def-statement
    | proc-call-statement
    | writeline-statement
    | output-statement
    | var-assignment-statement
    | array-assignment-statement
    | array2d-assignment-statement
    | array-initialiser-statement
    ;

if-statement:
      IF bexpr THEN statements ENDIF
    | IF bexpr THEN statements ELSE statements ENDIF
    ;

while-statement:
    WHILE bexpr statements ENDWHILE
    ;

case-option:
    expr COLON statements
    ;

case-options:
      case-option
    | case-options case-option
    ;

case-statement:
    CASE expr OF case-options
    ELSE statements ENDCASE

for-statement:
    FOR var ASSIGN iexpr1 TO iexpr2
    statements
    ENDFOR

repeat-statement:
    REPEAT
    statements
    UNTIL bexpr

funproc-def-params:
      /* empty */
    | expr
    | funproc-def-params COMMA expr
    ;

function-def-statement:
    FUNCTION NAME LPAREN funproc-def-params RPAREN
    statements
    ENDFUNCTION
    ;

return-statement:
    RETURN expr

proc-def-statement:
    PROCEDURE NAME LPAREN funproc-def-params RPAREN
    statements
    ENDPROCEDURE
    ;

fnproc-call-params:
      /* empty */
    | expr
    | fnproc-call-params COMMA expr
    ;

proc-call-statement:
    NAME LPAREN fnproc-call-params RPAREN
    ;

fn-call-expr:
    NAME LPAREN fnproc-call-params RPAREN
    ;

file:
    texpr
    ;

readline-expr:
    READLINE LPAREN file COMMA iexpr RPAREN
    ;

writeline-statement:
    WRITELINE LPAREN file COMMA iexpr COMMA expr RPAREN
    ;

output-statement:
    OUTPUT texpr
    ;

var-assignment-statement:
    NAME ASSIGN expr
    ;

array-assignment-statement:
    NAME LSQUARE iexpr RSQUARE ASSIGN expr
    ;

array2d-assignment-statement:
    NAME LSQUARE iexpr1 RSQUARE LSQUARE iexpr2 RSQUARE ASSIGN expr
    ;

initialiser-expr:
      /* empty */
    | expr
    | initialiser-expr COMMA expr
    ;

array-initialiser-statement:
    NAME ASSIGN LSQUARE initialiser-expr RSQUARE
    ;

expr:
      iexpr
    | bexpr
    | texpr
    | fn-call-expr
    | readline-expr
    | USERINPUT
    ;

iexpr:
      LPAREN iexpr RPAREN
    | NUMBER
    | LEN LPAREN NAME RPAREN
    | iexpr
    | iexpr PLUS iexpr
    | iexpr MINUS iexpr
    | iexpr TIMES iexpr
    | iexpr DIVIDE iexpr
    | iexpr MOD iexpr
    | MINUS iexpr
    | PLUS iexpr
    ;

texpr:
      STRLIT
    | NAME
    | LPAREN texpr RPAREN
    | texpr PLUS texpr
    ;

bexpr:
      TRUE
    | FALSE
    | NOT bexpr
    | LPAREN bexpr RPAREN
    | iexpr EQUAL iexpr
    | iexpr NOTEQUAL iexpr
    | iexpr LESEQUAL iexpr
    | iexpr GREATEREQUAL iexpr
    | iexpr GREATER iexpr
    | iexpr LESS iexpr
    | bexpr AND bexpr
    | bexpr OR bexpr
    | bexpr XOR bexpr
    ;

%%

