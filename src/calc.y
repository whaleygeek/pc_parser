%token NAME NUMBER EQUALS LPAREN RPAREN

%left PLUS MINUS
%left TIMES DIVIDE
%left UMINUS


%start statement

%%

statement : NAME EQUALS expression
    | expression
    ;

expression : NUMBER
    | NAME
    | MINUS expression %prec UMINUS
    | LPAREN expression RPAREN
    | expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    ;

%%


