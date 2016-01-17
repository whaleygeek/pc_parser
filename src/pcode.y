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
%token XOR

%token ID NUMBER STRING

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
//      if_statement
//    | while_statement
//    | case_statement
//    | for_statement
//    | repeat_statement
//    | function_def_statement
//    | return_statement
//    | proc_def_statement
//    | proc_call_statement
//    | writeline_statement
     output_statement
//    | var_assignment_statement
//    | array_assignment_statement
//    | array2d_assignment_statement
//    | array_initialiser_statement
    ;

//if_statement:
//      IF bexpr THEN statements ENDIF
//    | IF bexpr THEN statements ELSE statements ENDIF
//    ;

//while_statement:
//    WHILE bexpr statements ENDWHILE
//    ;

//case_option:
//    expr COLON statements
//    ;

//case_options:
//      case_option
//    | case_options case_option
//    ;

//case_statement:
//    CASE expr OF
//    case_options
//    ELSE statements
//    ENDCASE

//for_statement:
//    FOR var ASSIGN iexpr1 TO iexpr2
//    statements
//    ENDFOR

//repeat_statement:
//    REPEAT
//    statements
//    UNTIL bexpr

//funproc_def_params:
//      /* empty */
//    | expr
//    | funproc_def_params COMMA expr
//    ;

//function_def_statement:
//    FUNCTION ID LPAREN funproc_def_params RPAREN
//    statements
//    ENDFUNCTION
//    ;

//return_statement:
//    RETURN expr

//proc_def_statement:
//    PROCEDURE ID LPAREN funproc_def_params RPAREN
//    statements
//    ENDPROCEDURE
//    ;

//fnproc_call_params:
//      /* empty */
//    | expr
//    | fnproc_call_params COMMA expr
//    ;

//proc_call_statement:
//    ID LPAREN fnproc_call_params RPAREN
//    ;

//fn_call_expr:
//    ID LPAREN fnproc_call_params RPAREN
//    ;

//file:
//    texpr
//    ;

//readline_expr:
//    READLINE LPAREN file COMMA iexpr RPAREN
//    ;

//writeline_statement:
//    WRITELINE LPAREN file COMMA iexpr COMMA expr RPAREN
//    ;

output_statement:
    OUTPUT texpr
    ;

//var_assignment_statement:
//    ID ASSIGN expr
//    ;

//array_assignment_statement:
//    ID LSQUARE iexpr RSQUARE ASSIGN expr
//    ;

//array2d_assignment_statement:
//    ID LSQUARE iexpr1 RSQUARE LSQUARE iexpr2 RSQUARE ASSIGN expr
//    ;

//initialiser_expr:
//      /* empty */
//    | expr
//    | initialiser_expr COMMA expr
//    ;

//array_initialiser_statement:
//    ID ASSIGN LSQUARE initialiser_expr RSQUARE
//    ;

//expr:
//      iexpr
//    | bexpr
//    | texpr
//    | fn_call_expr
//    | readline_expr
//    | USERINPUT
//    ;

//iexpr:
//      LPAREN iexpr RPAREN
//    | NUMBER
//    | LEN LPAREN ID RPAREN
//    | iexpr
//    | iexpr PLUS iexpr
//    | iexpr MINUS iexpr
//    | iexpr TIMES iexpr
//    | iexpr DIVIDE iexpr
//    | iexpr MOD iexpr
//    | MINUS iexpr
//    | PLUS iexpr
//    ;

texpr:
      STRING
      {
        $0 = $1;
      }
//    | ID
//    | LPAREN texpr RPAREN
//    | texpr PLUS texpr
    ;

//bexpr:
//      TRUE
//    | FALSE
//    | NOT bexpr
//    | LPAREN bexpr RPAREN
//    | iexpr EQUAL iexpr
//    | iexpr NOTEQUAL iexpr
//    | iexpr LESEQUAL iexpr
//    | iexpr GREATEREQUAL iexpr
//    | iexpr GREATER iexpr
//    | iexpr LESS iexpr
//    | bexpr AND bexpr
//    | bexpr OR bexpr
//    | bexpr XOR bexpr
//    ;

%%

