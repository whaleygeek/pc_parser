/* pcode.y  17/01/2016  D.J.Whale */

%token ASSIGN LPAREN RPAREN LSQUARE WHEN
%token RSQUARE COMMA COLON

%token IF THEN ELSE ENDIF WHILE
%token ENDWHILE CASE OF ENDCASE FOR
%token TO ENDFOR REPEAT UNTIL FUNCTION
%token ENDFUNCTION RETURN PROCEDURE ENDPROCEDURE READLINE
%token WRITELINE OUTPUT USERINPUT LEN
%token NOT FALSE TRUE

%token ID NUMBER STRING

%left OR
%left AND
%left XOR
%left EQUAL NOTEQUAL
%left LESS GREATER LESSEQUAL GREATEREQUAL
%left PLUS MINUS
%left TIMES DIVIDE MOD
%left UNARY

%start program

%%

program:
    statements
    ;

statements:
    /* empty */
    | statements statement
    ;

statement:
    output_statement
    | var_assignment_statement
    | array_assignment_statement
    | if_statement
    | while_statement
    | repeat_statement
    | for_statement
    | proc_def_statement
    | proc_call_statement
    | function_def_statement
    | return_statement
    | writeline_statement
    | array2d_assignment_statement
    | array_initialiser_statement
    | case_statement
    ;

output_statement:
    OUTPUT expr
    ;

var_assignment_statement:
    ID ASSIGN expr
    ;

array_assignment_statement:
    ID LSQUARE expr RSQUARE ASSIGN expr
    ;

array2d_assignment_statement:
    ID LSQUARE expr RSQUARE LSQUARE expr RSQUARE ASSIGN expr
    ;

initialiser_expr:
    /* empty */
    | expr
    | initialiser_expr COMMA expr
    ;

array_initialiser_statement:
    ID ASSIGN LSQUARE initialiser_expr RSQUARE
    ;

file:
    expr
    ;

readline_expr:
    READLINE LPAREN file COMMA expr RPAREN
    ;

writeline_statement:
    WRITELINE LPAREN file COMMA expr COMMA expr RPAREN
    ;

if_statement:
    IF expr THEN statements ENDIF
    | IF expr THEN statements ELSE statements ENDIF
    ;

while_statement:
    WHILE expr statements ENDWHILE
    ;

repeat_statement:
    REPEAT
    statements
    UNTIL expr
    ;

for_statement:
    FOR ID ASSIGN expr TO expr
    statements
    ENDFOR
    ;

case_option:
    WHEN expr COLON statements // <-- 'WHEN' added to resolve grammar ambiguity
    ;

case_options:
    /* empty */
    | case_options case_option
    ;

case_statement:
    CASE expr OF
    case_options
    ELSE
    statements
    ENDCASE
    ;

fnproc_def_params:
    /* empty */
    | ID
    | fnproc_def_params COMMA ID
    ;

function_def_statement:
    FUNCTION ID LPAREN fnproc_def_params RPAREN
    statements
    ENDFUNCTION
    ;

return_statement:
    RETURN expr
    ;

proc_def_statement:
    PROCEDURE ID LPAREN fnproc_def_params RPAREN
    statements
    ENDPROCEDURE
    ;

fnproc_call_params:
    /* empty */
    | expr
    | fnproc_call_params COMMA expr
    ;

proc_call_statement:
    ID LPAREN fnproc_call_params RPAREN
    ;

fn_call_expr:
    ID LPAREN fnproc_call_params RPAREN
    ;

expr:
    TRUE
    | FALSE
    | NUMBER
    | ID
    | STRING
    | LPAREN expr RPAREN
    | USERINPUT
    | LEN LPAREN ID RPAREN
    | expr PLUS expr
    | expr MINUS expr
    | expr TIMES expr
    | expr DIVIDE expr
    | expr MOD expr
    | MINUS expr %prec UNARY
    | PLUS expr
    | NOT expr %prec UNARY
    | expr EQUAL expr
    | expr NOTEQUAL expr
    | expr LESSEQUAL expr
    | expr GREATEREQUAL expr
    | expr GREATER expr
    | expr LESS expr
    | expr AND expr
    | expr OR expr
    | expr XOR expr
    | readline_expr
    | fn_call_expr
    ;


%%

backend = None
def set_backend(b):
    global backend
    backend = b
