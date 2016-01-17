/* pcode.y  17/01/2016  D.J.Whale */

%token IF THEN ELSE ENDIF WHILE ENDWHILE CASE OF ENDCASE FOR TO ENDFOR REPEAT UNTIL
%token FUNCTION ENDFUNCTION RETURN PROCEDURE ENDPROCEDURE
%token READLINE WRITELINE OUTPUT USERINPUT LEN
%token MOD NOT FALSE TRUE AND OR XOR
%token PLUS MINUS TIMES DIVIDE
%token EQUAL NOTEQUAL LESS LESSEQUAL GREATER GREATEREQUAL
%token ASSIGN
%token LPAREN RPAREN
%token LSQUARE RSQUARE
%token COMMA COLON QUOTE

%token RETURN
%token TRUE FALSE
%token NAME

%start program


%%

program:
      /* empty */
    | statements
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
    | procedure-def-statement
    | proc-call-statement
    | writeline-statement
    | output-statement
    | var-assignment-statement
    | array-assignment-statement
    | array2d-assignment-statement
    | array-initialiser-statement
    ;

# beware of dangling else problem

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

/* fname?? */

function-def-statement:
    FUNCTION fname LPAREN funproc-def-params RPAREN
    statements
    ENDFUNCTION
    ;

/*  beware of ambiguity of where return is and is-not allowed */

return-statement:
    RETURN expr

/* pname?? */

procedure-def-statement:
    PROCEDURE pname LPAREN funproc-def-params RPAREN
    statements
    ENDPROCEDURE
    ;

fnproc-call-params:
      /* empty */
    | expr
    | fnproc-call-params COMMA expr
    ;

/* beware of ambiguity between fn call and proc call */
proc-call-statement:
    pname LPAREN fnproc-call-params RPAREN
    ;

fn-call-statement:
    fname LPAREN fnproc-call-params RPAREN
    ;

/* file? */

readline-statement:
    READLINE LPAREN file COMMA iexpr RPAREN
    ;

writeline-statement:
    WRITELINE LPAREN file COMMA iexpr COMMA expr RPAREN
    ;

output-statement:
    OUTPUT texpr
    ;

/* varname? */

var-assignment-statement:
    varname ASSIGN expr
    ;

array-assignment-statement:
    varname LSQUARE iexpr RSQUARE ASSIGN expr
    ;

array2d-assignment-statement:
    varname LSQUARE iexpr1 RSQUARE LSQUARE iexpr2 RSQUARE ASSIGN expr
    ;

initialiser-expression:
      /* empty */
    | expr
    | initialiser-expression COMMA expr
    ;

array-initialiser-statement:
    varname ASSIGN LSQUARE initialiser-expr RSQUARE
    ;

/* can be any type of expression (iexpr, texpr, bexpr)
 * presumably type is stored along with the value
 */

expr:
      iexpr
    | bexpr
    | texpr
    | fn-call-statement
    | readline-statement
    ;

/* note, define precedence in the hierarchy of the grammar
 * note, unary minus
 * note, unary plus
 * var? name?
 */

iexpr:
      LPAREN iexpr RPAREN
    | NUMBER
    | LEN LPAREN var RPAREN
    | USERINPUT
    | iexpr
    | iexpr PLUS iexpr
    | iexpr MINUS iexpr
    | iexpr TIMES iexpr
    | iexpr DIVIDE iexpr
    | iexpr MOD iexpr
    | MINUS iexpr
    | PLUS iexpr
    ;

/* text? This might just be a STRLIT from lexer */

texpr:
    QUOTE text QUOTE
    ;

/* note, define precedence in the hierarchy of the grammar */

bexpr:
      TRUE
    | FALSE
    | LPAREN bexpr RPAREN
    | NOT bexpr
    | bexpr AND bexpr
    | bexpr OR bexpr
    | bexpr XOR bexpr
    | iexpr EQUAL iexpr
    | iexpr NOTEQUAL iexpr
    | iexpr LESEQUAL iexpr
    | iexpr GREATEREQUAL iexpr
    | iexpr GREATER iexpr
    | iexpr LESS iexpr
    ;

%%

