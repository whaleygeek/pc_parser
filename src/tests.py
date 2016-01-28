# tests.py  26/01/2016  D.J.Whale

import unittest
import pcode

#----- TEST SYNTAX ------------------------------------------------------------

class x:#TestSyntax(unittest.TestCase):
    IMPORTS = "from io import *\nfrom array import *"

    #--------------------------------------------------------------------------
    def test_emptyproc(self):
        SRC = \
"""
PROCEDURE test_emptyproc()
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_emptyproc():
    pass
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_emptyfn(self):
        SRC = \
"""
FUNCTION test_emptyfn()
ENDFUNCTION
"""
        EXPECTED = self.IMPORTS + \
"""
def test_emptyfn():
    pass
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_output(self):
        SRC = \
"""
PROCEDURE test_output()
    OUTPUT "hello"
    a <- "me"
    OUTPUT a
    OUTPUT 1
    OUTPUT "a" + "b"
    c <- a + a + a
    OUTPUT a
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_output():
    print("hello")
    a = "me"
    print(a)
    print(1)
    print("a"+"b")
    c = a+a+a
    print(a)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_assign(self):
        SRC = \
"""
PROCEDURE test_assign()
    a <- 1
    b <- 2
    c <- "var"
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_assign():
    a = 1
    b = 2
    c = "var"
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_array1d_assign(self):
        SRC = \
"""
PROCEDURE test_array1d_assign()
    a[0] <- 1
    a[1] <- 2
    b <- 10
    a[b] <- 10
    a[b+1] <- 10
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_array1d_assign():
    a = Array()
    a[0] = 1
    a[1] = 2
    b = 10
    a[b] = 10
    a[b+1] = 10
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_array2d_assign(self):
        SRC = \
"""
PROCEDURE test_array2d_assign()
    a[0][0] <- 1
    a[1][1] <- 2
    x <- 10
    y <- 20
    a[x][y] <- x + y
    a[x+1][y+1] <- x + y * 2
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_array2d_assign():
    a = Array2D()
    a[0][0] = 1
    a[1][1] = 2
    x = 10
    y = 20
    a[x][y] = x+y
    a[x+1][y+1] = x+y*2
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_array_init(self):
        SRC = \
"""
PROCEDURE test_array_init()
    a <- [1,2,3,4]
    b <- 10
    c <- 20
    d <- [b,c,b,c,b+1,c+10]
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_array_init():
    a = Array(1, 2, 3, 4)
    b = 10
    c = 20
    d = Array(b, c, b, c, b+1, c+10)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_array_read(self):
        SRC = \
"""
PROCEDURE test_array_read()
    a <- [1,2,3,4]
    OUTPUT a[0]
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_array_read():
    a = Array(1, 2, 3, 4)
    print(a[0])
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_array2d_read(self):
        SRC = \
"""
PROCEDURE test_array2d_read()
    a[0][0] <- 0
    a[0][1] <- 1
    a[1][0] <- 10
    a[1][1] <- 1
    OUTPUT a[1][1]
    x <- 1
    y <- 0
    OUTPUT a[x*2+1][y-2*3]
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_array2d_read():
    a = Array2D()
    a[0][0] = 0
    a[0][1] = 1
    a[1][0] = 10
    a[1][1] = 1
    print(a[1][1])
    x = 1
    y = 0
    print(a[x*2+1][y-2*3])
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_if(self):
        SRC = \
"""
PROCEDURE test_if()
    a <- 1
    IF a = 1 THEN
        OUTPUT "one"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_if():
    a = 1
    if a==1:
        print("one")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_if_else(self):
        SRC = \
"""
PROCEDURE test_if_else()
    a <- 1
    IF a = 1 THEN
        OUTPUT "one"
    ELSE
        OUTPUT "not one"
    ENDIF

    b <- 2
    IF a = 1 THEN
        IF b = 1 THEN
            OUTPUT "one one"
        ELSE
            OUTPUT "one notone"
        ENDIF
    ELSE
        IF b = 1 THEN
            OUTPUT "notone one"
        ELSE
            OUTPUT "notone notone"
        ENDIF
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_if_else():
    a = 1
    if a==1:
        print("one")
    else:
        print("not one")
    b = 2
    if a==1:
        if b==1:
            print("one one")
        else:
            print("one notone")
    else:
        if b==1:
            print("notone one")
        else:
            print("notone notone")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_empty_if_else(self):
        SRC = \
"""
PROCEDURE test_empty_if_else()
    a <- 1
    IF a = 1 THEN
    ENDIF

    IF a = 1 THEN
    ELSE
    ENDIF

    IF a = 1 THEN
        IF a = 2 THEN
        ELSE
        ENDIF
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_empty_if_else():
    a = 1
    if a==1:
        pass
    if a==1:
        pass
    else:
        pass
    if a==1:
        if a==2:
            pass
        else:
            pass
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_empty_everything(self):
        SRC = \
"""
PROCEDURE test_empty_everything()
    # nested if/while/for is a challenging test case
    # It's probably ok the way it is implemented.
    FOR a <- 1 TO 10
        IF a > 1 THEN
            WHILE a < 10
            ENDWHILE
        ELSE
        ENDIF
    ENDFOR
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_empty_everything():
    for a in range(1, 10):
        if a>1:
            while a<10:
                pass
        else:
            pass
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_while(self):
        SRC = \
"""
PROCEDURE test_while()
    a <- 0
    WHILE a < 10
        OUTPUT "hello"
        a <- a + 1
    ENDWHILE
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_while():
    a = 0
    while a<10:
        print("hello")
        a = a+1
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_empty_while(self):
        SRC = \
"""
PROCEDURE test_empty_while()
    WHILE TRUE
    ENDWHILE

    WHILE TRUE
        WHILE TRUE
        ENDWHILE
    ENDWHILE
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_empty_while():
    while True:
        pass
    while True:
        while True:
            pass
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_repeat(self):
        SRC = \
"""
PROCEDURE test_repeat()
    a <- 0
    REPEAT
        OUTPUT a
        a <- a + 1
    UNTIL a > 10
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_repeat():
    a = 0
    while True:
        print(a)
        a = a+1
        if a>10: break
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_for(self):
        SRC = \
"""
PROCEDURE test_for()
    FOR i <- 1 TO 10
        OUTPUT i
    ENDFOR
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_for():
    for i in range(1, 10):
        print(i)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_empty_for(self):
        SRC = \
"""
PROCEDURE test_empty_for()
    FOR a <- 1 TO 10
    ENDFOR

    FOR b <- 1 TO 10
        FOR c <- 1 TO 10
        ENDFOR
    ENDFOR
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_empty_for():
    for a in range(1, 10):
        pass
    for b in range(1, 10):
        for c in range(1, 10):
            pass
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_func_noparams(self):
        SRC = \
"""
FUNCTION test_func_noparams()
    RETURN 1
ENDFUNCTION
"""
        EXPECTED = self.IMPORTS + \
"""
def test_func_noparams():
    return 1
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_func_params(self):
        SRC = \
"""
FUNCTION test_func_params(a,b,c)
    RETURN a
ENDFUNCTION
"""
        EXPECTED = self.IMPORTS + \
"""
def test_func_params(a, b, c):
    return a
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_case(self):
        SRC = \
"""
PROCEDURE test_case()
    a <- 1
    b <- 10
    c <- 1
    CASE a OF
    WHEN 1:
        OUTPUT "one"
    WHEN 2:
        OUTPUT "two"
    WHEN 3:
        OUTPUT "three"
        OUTPUT "lots"
    ELSE #TODO: ELSE is mandatory in grammar at the moment
        OUTPUT "something else"
        OUTPUT "dont know what"
    ENDCASE

    # nested case
    CASE a OF
    WHEN 1:
        CASE b OF
        WHEN 10:
            OUTPUT 10
        WHEN 20:
            OUTPUT 20
        ELSE
            OUTPUT 0
        ENDCASE
    WHEN 2:
        CASE c OF
        WHEN 10:
            OUTPUT 10
        WHEN 20:
            OUTPUT 20
        ELSE
            OUTPUT 0
        ENDCASE
    ELSE
        OUTPUT(99)
    ENDCASE
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_case():
    a = 1
    b = 10
    c = 1
    if a == 1:
        print("one")
    elif a == 2:
        print("two")
    elif a == 3:
        print("three")
        print("lots")
    else:
        print("something else")
        print("dont know what")
    if a == 1:
        if b == 10:
            print(10)
        elif b == 20:
            print(20)
        else:
            print(0)
    elif a == 2:
        if c == 10:
            print(10)
        elif c == 20:
            print(20)
        else:
            print(0)
    else:
        print((99))
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_true_false(self):
        SRC = \
"""
PROCEDURE test_true_false()
    a <- TRUE
    b <- FALSE
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_true_false():
    a = True
    b = False
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_number(self):
        SRC = \
"""
PROCEDURE test_number()
    a <- 1
    b <- 1234
    c <- 9999
    d <- 65535
    e <- 4000000000
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_number():
    a = 1
    b = 1234
    c = 9999
    d = 65535
    e = 4000000000
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_id(self):
        SRC = \
"""
PROCEDURE test_id()
    a <- 1
    fred <- 2
    var2 <- 3
    var_with_underscores <- 4
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_id():
    a = 1
    fred = 2
    var2 = 3
    var_with_underscores = 4
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_string(self):
        SRC = \
"""
PROCEDURE test_string()
    a <- "hello world"
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_string():
    a = "hello world"
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_brackets(self):
        SRC = \
"""
PROCEDURE test_brackets()
    a <- (1*2+(3+(4-5)))
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_brackets():
    a = (1*2+(3+(4-5)))
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_len(self):
        SRC = \
"""
PROCEDURE test_len()
    a <- "hello"
    b <- LEN(a)
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_len():
    a = "hello"
    b = len(a)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_plus(self):
        SRC = \
"""
PROCEDURE test_plus()
    a <- 1 + 2
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_plus():
    a = 1+2
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_minus(self):
        SRC = \
"""
PROCEDURE test_minus()
    a <- 1 - 2
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_minus():
    a = 1-2
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_times(self):
        SRC = \
"""
PROCEDURE test_times()
    a <- 1 * 2
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_times():
    a = 1*2
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_divide(self):
        SRC = \
"""
PROCEDURE test_divide()
    a <- 1 / 2
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_divide():
    a = 1/2
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_mod(self):
        SRC = \
"""
PROCEDURE test_mod()
    a <- 1 MOD 2
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_mod():
    a = 1%2
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_uminus(self):
        SRC = \
"""
PROCEDURE test_uminus()
    a <- -1
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_uminus():
    a = -1
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_uplus(self):
        SRC = \
"""
PROCEDURE test_uplus()
    a <- +1
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_uplus():
    a = 1
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_equal(self):
        SRC = \
"""
PROCEDURE test_equal()
    a <- 1
    IF a = 1 THEN
        OUTPUT "yes"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_equal():
    a = 1
    if a==1:
        print("yes")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_notequal(self):
        SRC = \
"""
PROCEDURE test_notequal()
    a <- 1
    IF a <> 1 THEN
        OUTPUT "yes"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_notequal():
    a = 1
    if a!=1:
        print("yes")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_less(self):
        SRC = \
"""
PROCEDURE test_less()
    a <- 1
    IF a < 1 THEN
        OUTPUT "yes"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_less():
    a = 1
    if a<1:
        print("yes")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_greater(self):
        SRC = \
"""
PROCEDURE test_greater()
    a <- 1
    IF a > 1 THEN
        OUTPUT "yes"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_greater():
    a = 1
    if a>1:
        print("yes")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_lessequal(self):
        SRC = \
"""
PROCEDURE test_lessequal()
    a <- 1
    IF a <= 1 THEN
        OUTPUT "yes"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_lessequal():
    a = 1
    if a<=1:
        print("yes")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_greaterequal(self):
        SRC = \
"""
PROCEDURE test_greaterequal()
    a <- 1
    IF a >= 1 THEN
        OUTPUT "yes"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_greaterequal():
    a = 1
    if a>=1:
        print("yes")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_and(self):
        SRC = \
"""
PROCEDURE test_and()
    a <- 1
    b <- 2
    IF a = 1 AND b = 1 THEN
        OUTPUT "both of them are one"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_and():
    a = 1
    b = 2
    if a==1 and b==1:
        print("both of them are one")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_or(self):
        SRC = \
"""
PROCEDURE test_or()
    a <- 1
    b <- 2
    IF a = 1 OR b = 1 THEN
        OUTPUT "one of them is one"
    ENDIF
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_or():
    a = 1
    b = 2
    if a==1 or b==1:
        print("one of them is one")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_xor(self):
        SRC = \
"""
PROCEDURE test_xor()
    a <- 1
    b <- 2
    c <- a XOR b
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_xor():
    a = 1
    b = 2
    c = a^b
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_readline(self):
        SRC = \
"""
PROCEDURE test_readline()
    FOR n <- 1 TO 10
        a <- READLINE("words.txt", n)
        OUTPUT a
    ENDFOR
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_readline():
    for n in range(1, 10):
        a = readline("words.txt", n)
        print(a)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_writeline(self):
        SRC = \
"""
PROCEDURE test_writeline()
    FOR n <- 1 TO 10
        WRITELINE("test.txt", n, "some data")
    ENDFOR
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_writeline():
    for n in range(1, 10):
        writeline("test.txt", n, "some data")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_fncall_noparams(self):
        SRC = \
"""
FUNCTION fn0()
    RETURN 1
ENDFUNCTION

PROCEDURE test_fncall_noparams()
    a <- fn0()
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def fn0():
    return 1
def test_fncall_noparams():
    a = fn0()
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fncall_1param(self):
        SRC = \
"""
FUNCTION fn1(a)
    RETURN a+1
ENDFUNCTION

PROCEDURE test_fncall_1param()
    a <- fn1(10)
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def fn1(a):
    return a+1
def test_fncall_1param():
    a = fn1(10)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fncall_2params(self):
        SRC = \
"""
FUNCTION fn2(a, b)
    RETURN a+b
ENDFUNCTION

PROCEDURE test_fncall_2params()
    a <- fn2(10, 20)
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def fn2(a, b):
    return a+b
def test_fncall_2params():
    a = fn2(10, 20)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_proccall_1param(self):
        SRC = \
"""
PROCEDURE proc1(a)
    OUTPUT a
ENDPROCEDURE

PROCEDURE test_proccall_1param()
    proc1(10)
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def proc1(a):
    print(a)
def test_proccall_1param():
    proc1(10)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_proccall_2params(self):
        SRC = \
"""
PROCEDURE proc2(a, b)
    OUTPUT a+b
ENDPROCEDURE

PROCEDURE test_proccall_2params()
    proc2(10 ,20)
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def proc2(a, b):
    print(a+b)
def test_proccall_2params():
    proc2(10, 20)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fnproc_global_array(self):
        SRC = \
"""
x[1] <- 1
y[2] <- 2
z <- [1,2,3]

FUNCTION test_fn_global_array()
    OUTPUT x[1]
    OUTPUT y[2]
    OUTPUT z[3]
ENDFUNCTION

PROCEDURE test_proc_global_array()
    OUTPUT x[1]
    OUTPUT y[2]
    OUTPUT z[3]
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
x = Array()
x[1] = 1
y = Array()
y[2] = 2
z = Array(1, 2, 3)
def test_fn_global_array():
    print(x[1])
    print(y[2])
    print(z[3])
def test_proc_global_array():
    print(x[1])
    print(y[2])
    print(z[3])
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fn_bubble_arrayGH(self):
        SRC = \
"""
FUNCTION test_fn_bubble_arrayGH()
    g[1] <- 1
    h[1][2] <- 12
ENDFUNCTION

g[1] <- 2
h[1][2] <- 1212
"""
        EXPECTED = self.IMPORTS + \
"""
def test_fn_bubble_arrayGH():
    g = Array()
    g[1] = 1
    h = Array2D()
    h[1][2] = 12
g = Array()
g[1] = 2
h = Array2D()
h[1][2] = 1212
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)


    #--------------------------------------------------------------------------
    def test_array_param(self):
        SRC = \
"""
FUNCTION test_array_param(a)
    OUTPUT a[0]
    OUTPUT a[1]
ENDFUNCTION

z <- [1,2,3,4]
test_array_param(z)
"""
        EXPECTED = self.IMPORTS + \
"""
def test_array_param(a):
    print(a[0])
    print(a[1])
z = Array(1, 2, 3, 4)
test_array_param(z)
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)


#----- TEST ARRAYS ------------------------------------------------------------

import arrays

class xx:#TestArrays(unittest.TestCase):

    def test_1d_create(self):
        a = arrays.Array()
        #expect no exception

    def test_1d_write_extend1(self):
        a = arrays.Array()
        a[0] = 99
        EXPECTED = "[99]"
        actual = str(a)
        self.assertEquals(EXPECTED, actual)

    def test_1d_write_existing(self):
        a = arrays.Array()
        a[0] = 99
        a[0] = 22
        EXPECTED = "[22]"
        actual = str(a)
        self.assertEquals(EXPECTED, actual)

    def test_1d_write_extendmany(self):
        a = arrays.Array()
        a[0] = 99
        a[5] = 22
        EXPECTED = "[99, 0, 0, 0, 0, 22]"
        actual = str(a)
        self.assertEquals(EXPECTED, actual)

    def test_1d_read_missing(self):
        a = arrays.Array()
        a[0]=99
        r = a[10]
        self.assertEquals(0, r)
        actual = str(a)
        self.assertEquals("[99]", actual)

    def test_1d_read_existing(self):
        a = arrays.Array()
        a[0]=99
        a[10]=1010
        actual = a[10]
        self.assertEquals(1010, actual)

    def test_1d_init(self):
        a = arrays.Array(10,9,8,7,6)
        EXPECTED = "[10, 9, 8, 7, 6]"
        self.assertEquals(EXPECTED, str(a))

    def test_2d_create(self):
        a = arrays.Array2D()
        # expect no exception

    def test_2d_write_extendxy1(self):
        a = arrays.Array2D()
        a[0][0] = 99
        self.assertEquals("[[99]]", str(a))

    def test_2d_write_extendx1(self):
        a = arrays.Array2D()
        a[0][0] = 99
        a[1][0] = 10
        self.assertEquals("[[99], [10]]", str(a))

    def test_2d_write_extendy1(self):
        a = arrays.Array2D()
        a[0][0] = 99
        a[0][1] = 10
        self.assertEquals("[[99, 10]]", str(a))

    def test_2d_write_existingxy(self):
        a = arrays.Array2D()
        a[0][0] = 99
        a[0][1] = 10

        a[0][0] = 1010
        a[0][1] = 2020
        self.assertEquals("[[1010, 2020]]", str(a))

    def test_2d_write_expandmanyx(self):
        a = arrays.Array2D()
        a[3][0] = 33
        self.assertEquals("[[], [], [], [33]]", str(a))

    def test_2d_write_expandmanyy(self):
        a = arrays.Array2D()
        a[0][3] = 33
        self.assertEquals("[[0, 0, 0, 33]]", str(a))

    def test_2d_read_missingx(self):
        a = arrays.Array2D()
        a[0][0] = 10
        r = a[3][0]
        self.assertEquals(0, r)

    def test_2d_read_missingy(self):
        a = arrays.Array2D()
        a[0][0] = 10
        r = a[0][3]
        self.assertEquals(0, r)

    def test_2d_read_existing(self):
        a = arrays.Array2D()
        a[3][3] = 33
        r = a[3][3]
        self.assertEquals(33, r)


#----- TEST IO ----------------------------------------------------------------

import fileio
import os

class xxx:#TestIO(unittest.TestCase):
    FILENAME = "testio.txt"
    locks = {}

    def remove_file(self, name):
        try:
            os.remove(name)
        except OSError:
            pass # ignore missing files

    def create_file_blank(self, name):
        if os.path.exists(name):
            os.remove(name)
        f = open(name, "w")
        f.close()

    def create_file_with(self, name, contents):
        if os.path.exists(name):
            os.remove(name)
        f = open(name, "w")
        f.write(contents)
        f.close()

    def lock_file(self, name):
        f = open(name, "w")
        self.locks[name] = f

    def unlock_file(self, name):
        f = self.locks[name]
        f.close()
        del self.locks[name]

    def file_exists(self, name):
        if os.path.exists(name) and os.path.isfile(name):
            return True
        return False

    def get_file_contents(self, name):
        f = open(name)
        l = f.read()
        f.close()
        return l


    def test_write_missing(self):
        """Should be possible to write to a file that does not exist"""
        self.remove_file(self.FILENAME)
        fileio.writeline(self.FILENAME, 1, "data")

        self.assertTrue(self.file_exists(self.FILENAME))
        self.assertEquals("data\n", self.get_file_contents(self.FILENAME))

    def test_write_present(self):
        """Should be possible to write to a file that does exist"""
        self.create_file_blank(self.FILENAME)
        fileio.writeline(self.FILENAME, 1, "data")

        self.assertEquals("data\n", self.get_file_contents(self.FILENAME))

    def test_write_locked(self):
        """Should not be possible to write to a locked file"""
        self.create_file_blank(self.FILENAME)
        self.lock_file(self.FILENAME)
        try:
            fileio.writeline(self.FILENAME, 1, "data")
            self.fail("Did not get expected exception")
        except:
            pass # print("expected exception")
        finally:
            self.unlock_file(self.FILENAME)

    def test_write_add1(self):
        """Should be possible to add a line to an existing file"""
        self.create_file_blank(self.FILENAME)
        fileio.writeline(self.FILENAME, 1, "data")

        self.assertEquals("data\n", self.get_file_contents(self.FILENAME))

    def test_write_expand_many(self):
        """Should be possible to write a line anywhere in an existing file"""
        self.create_file_blank(self.FILENAME)
        fileio.writeline(self.FILENAME, 10, "data")

        self.assertEquals("\n\n\n\n\n\n\n\n\ndata\n", self.get_file_contents(self.FILENAME))

    def test_write_expand_line(self):
        """Should be possible to expand an existing line in a file without damaging others"""
        self.create_file_blank(self.FILENAME)
        fileio.writeline(self.FILENAME, 1, "data")
        fileio.writeline(self.FILENAME, 2, "more data")
        fileio.writeline(self.FILENAME, 1, "longer data expanded")

        self.assertEquals("longer data expanded\nmore data\n", self.get_file_contents(self.FILENAME))

    def test_write_shrink_line(self):
        """Should be possible to shrink an existing line in a file without damaging others"""
        self.create_file_blank(self.FILENAME)
        fileio.writeline(self.FILENAME, 1, "data")
        fileio.writeline(self.FILENAME, 2, "more data")
        fileio.writeline(self.FILENAME, 1, "a")

        self.assertEquals("a\nmore data\n", self.get_file_contents(self.FILENAME))

    def test_read_missing(self):
        """If you read from a missing file, should get an exception"""
        self.remove_file(self.FILENAME)
        try:
            r = fileio.readline(self.FILENAME, 1)
            self.fail("Did not get expected exception")
        except fileio.FileIOException:
            pass # expected

    def test_read_present(self):
        """If you read a line from a present file, that is missing, should get an exception"""
        self.create_file_blank(self.FILENAME)
        try:
            r = fileio.readline(self.FILENAME, 1)
            self.fail("Did not get expected exception")
        except fileio.FileIOException:
            pass # expected

    def test_read_missing_line(self):
        """If you read a line from a file beyond it's end, should get an exception"""
        self.create_file_with(self.FILENAME, "one\n")
        try:
            r = fileio.readline(self.FILENAME, 2)
            self.fail("Did not get expected exception")
        except fileio.FileIOException:
            pass # expected

    def test_read_present_line(self):
        """If you read a line from a file where the file exists, should get correct data back"""
        self.create_file_with(self.FILENAME, "one\ntwo\nthree\nfour\n")
        r = fileio.readline(self.FILENAME, 3)
        self.assertEquals("three", r)


#----- TEST RUNTIME -----------------------------------------------------------
#
# This is all about testing that the generated program for each aspect
# runs and generates the correct output
# and the variables have the correct final state.

class TestRuntime(unittest.TestCase):

    def pc2py(self, contents):
        """Turn pcode into python"""
        return pcode.test(contents)

    def runpy(self, name, contents):
        """Create and run a python file"""
        NAME = "t_run"
        f = open("%s.py" % name, "w")
        f.write(contents)
        f.close()

        import importlib
        m = importlib.import_module(name)
        return m # the module instance

    def runpc(self, name, contents):
        """Compile pcode into py and create and run it as a py file"""
        py = self.pc2py(contents)
        m = self.runpy(name, py)
        return m # the module instance

    def XXXXtest_hello_py(self):
        """It should be possible to run a python from source"""
        PYNAME = "t_hello"
        SRC = """print("## hello from python ##")\n"""
        self.runpy(PYNAME, SRC)

    def XXXXtest_hello_pc(self):
        """It should be possible to run pcode from source"""
        SRC = """OUTPUT "## hello from pcode ##"\n"""
        self.runpc("hello_pc", SRC)

    def XXXtest_varstate(self):
        """It should be possible to inspect final variable state"""
        SRC = "a <- 1\n"
        m = self.runpc("varstate_pc", SRC)
        self.assertEquals(1, m.a)

    def test_mockprint(self):
        """It should be possible to OUTPUT something and capture the result"""
        SRC = """OUTPUT "Hello"\n"""
        m = self.runpc("mockprint_pc", SRC)
        self.assertEquals("Hello", m.outbuf)

    def XXXtest_mockinput(self):
        """It should be possible to inject input data for USERINPUT"""
        SRC = """USERINPUT\n"""
        # This is harder because we have to inject input before module is imported
        # might have to import a mockio module and store state in that,
        # then inspect or inject.



# test we can run a hello world program
# i.e.
#   translate into python
#   store this in a file
#   necessary imports are there
#   can run it as a python task
#   can capture output
#   compare runtime output to expected
#   do we need to detect non terminating progs and timeout??

# output
# assignment
# arrays1d assign
# arrays2d assign
# arrays init
# arrays read
# arrays 2d read
# if
# if else
# nested if else
# while
# repeat
# for
# func noparams
# func 1param
# func 2params
# case
# nested case
# true false
# number
# id
# string
# brackets
# len
# plus
# minus
# times
# divide
# mod
# uminus
# uplus
# equal
# notequal
# less
# greater
# lessequal
# greaterequal
# and
# or
# xor
# readline
# writeline
# fncall_noparams
# fncall_1param
# fncall_2params
# proccall_1param
# proccall_2params
# fnproc global arrays
# fn bubble arrays


if __name__ == "__main__":
    unittest.main()
