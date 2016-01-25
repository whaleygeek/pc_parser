# pygen.py  17/01/2016  D.J.Whale
#
# Generator for pcode.py that generates python from each of the actions.

import sys

class ParserException(Exception):
    pass


class Generator():
    def __init__(self):
        self.indentlev   = 0
        self.nest_stack  = []
        self.case_stack  = []
        self.procfn      = 0

        self.global_vars = []
        self.local_vars  = None

        self.out("from io import *")
        self.out("from array import *")

    #----- EMITTER FUNCTIONS --------------------------------------------------

    def indent(self):
        self.indentlev += 4

    def outdent(self):
        self.indentlev -= 4

    def out(self, msg):
        print((" " * self.indentlev) + msg)


    #----- HELPERS ------------------------------------------------------------

    def now_local(self):
        """Call this when entering local scope, i.e. a fn or proc"""
        self.local_vars = []

    def now_global(self):
        """Call this when returnign to global scope, i.e. returning from a fn or proc"""
        self.local_vars = None

    def var_exists(self, name):
        """Does this variable exist?"""
        if self.local_vars != None:
            if name in self.local_vars: return True

        if name in self.global_vars: return True
        return False

    def create_var(self, name):
        """Create a variable in the correct scope"""
        if self.local_vars != None:
            self.local_vars.append(name)
        else:
            self.global_vars.append(name)


    def copy(self, p, i_item):
        item = p[i_item]
        r = item
        p[0] = r

    def empty(self, p):
        p[0] = ""

    def comma(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        try:
            r = left + ", " + right
        except TypeError:
            r = str(left) + ", " + str(right)
        p[0] = r

    def concat(self, p, i_one, i_two):
        one = p[i_one]
        two = p[i_two]
        try:
            both = one + two
        except TypeError:
            both = str(one) + str(two)
        p[0] = both

    def statement(self, p):
        if len(self.nest_stack) != 0:
            # Increment counter of statements at this nest level
            self.nest_stack[-1] += 1


    #----- GENERATE OUTPUT ON THE FLY -----------------------------------------

    def OUTPUT(self, p, i_expr):
        expr = p[i_expr]
        self.out("print(%s)" % str(expr))

    def assign(self, p, i_id, i_expr):
        id = p[i_id]
        expr = p[i_expr]
        self.out("%s = %s" % (id, expr))

    def array1assign(self, p, i_id, i_indexexpr, i_valueexpr):
        """Write to a 1D array"""
        id = p[i_id]
        indexexpr = p[i_indexexpr]
        valueexpr = p[i_valueexpr]
        if not self.var_exists(id):
            # construct an array object before we write to it
            self.create_var(id)
            self.out("%s = Array()" % id)

        self.out("%s[%s] = %s" % (id, indexexpr, valueexpr))

    def array2assign(self, p, i_id, i_index1expr, i_index2expr, i_valueexpr):
        """Write to a 2D array"""
        id = p[i_id]
        index1expr = p[i_index1expr]
        index2expr = p[i_index2expr]
        valueexpr  = p[i_valueexpr]

        if not self.var_exists(id):
            # construct a 2D array object before we write to it
            self.create_var(id)
            self.out("%s = Array2D()" % id)

        self.out("%s[%s][%s] = %s" % (id, index1expr, index2expr, valueexpr))

    def arrayinit(self, p, i_id, i_initialiser):
        """Initialise a 1D array"""
        id = p[i_id]
        initialiser = p[i_initialiser]

        if not self.var_exists(id):
            # construct a 1D array object before we write to it
            self.create_var(id)
            self.out("%s = Array()" % id)

        self.out("%s = [%s]" % (id, initialiser))

    def READLINE(self, p, i_file, i_expr):
        file = p[i_file]
        expr = p[i_expr]
        p[0] = "readline(%s, %s)" % (file, expr)
        #TODO runtime support required

    def WRITELINE(self, p, i_file, i_expr1, i_expr2):
        file = p[i_file]
        expr1 = p[i_expr1]
        expr2 = p[i_expr2]
        self.out("writeline(%s, %s, %s)" % (file, expr1, expr2))
        #TODO runtime support required

    def IF(self, p, i_expr):
        expr = p[i_expr]
        self.out("if %s:" % expr)
        self.indent()
        self.nest_stack.append(0) # count of statements in IF

    def ELSE(self, p):
        c = self.nest_stack.pop()
        if c == 0: # no statements in THEN
            self.out("pass")
        self.outdent()
        self.out("else:")
        self.indent()
        self.nest_stack.append(0) # count of statements in ELSE

    def ENDIF(self, p):
        c = self.nest_stack.pop()
        if c == 0: # no statements in preceeding THEN or ELSE
            self.out("pass")
        self.outdent()
        #self.out("")

    def WHILE(self, p, i_expr):
        expr = p[i_expr]
        self.out("while %s:" % expr)
        self.indent()
        self.nest_stack.append(0) # count of statements in this while

    def ENDWHILE(self, p):
        c = self.nest_stack.pop()
        if c == 0: # There were no statements in this while loop
            self.out("pass")
        self.outdent()
        #self.out("")

    def REPEAT(self, p):
        self.out("while True:")
        self.indent()

    def UNTIL(self, p, i_expr):
        expr = p[i_expr]
        self.out("if %s: break" % expr)
        self.outdent()
        #self.out("")

    def FOR(self, p, i_id, i_from, i_to):
        id = p[i_id]
        f = p[i_from]
        t = p[i_to]
        self.out("for %s in range(%s, %s):" % (id, f, t))
        self.nest_stack.append(0) # counter of statements in this FOR loop
        self.indent()

    def ENDFOR(self, p):
        c = self.nest_stack.pop()
        if c == 0: # There were no statements in this for loop
            self.out("pass")
        self.outdent()
        #self.out("")

    def CASE(self, p, i_expr):
        expr = p[i_expr]
        self.case_stack.append([0, expr])

    def WHEN(self, p, i_expr):
        expr = p[i_expr]
        info = self.case_stack[-1]
        count, check = info

        if count == 0:
            self.out("if %s == %s:" % (check, expr))
        else:
            self.out("elif %s == %s:" % (check, expr))
        self.indent()
        (self.case_stack[-1])[0] += 1

    def ENDWHEN(self, p):
        self.outdent()
        #self.out("")

    def CASEELSE(self, p):
        self.out("else:")
        self.indent()

    def ENDCASEELSE(self, p):
        self.outdent()

    def ENDCASE(self, p):
        self.case_stack.pop()

    def defparams(self, p, i_params, i_id):
        params = p[i_params]
        id = p[i_id]
        r = params + ", " + id
        p[0] = id

    def FUNCTION(self, p, i_id, i_params):
        if self.procfn != 0:
            raise RuntimeError("Nested procedure/function not allowed")

        id = p[i_id]
        params = p[i_params]
        self.out("def %s(%s):" % (id, params))
        self.indent()
        self.nest_stack.append(0) # count of statements in function
        self.procfn += 1
        self.now_local()

    def RETURN(self, p, i_expr):
        expr = p[i_expr]
        self.out("return %s" % str(expr))

    def ENDFUNCTION(self, p):
        c = self.nest_stack.pop()
        if c == 0:
            self.out("pass")
        self.outdent()
        self.procfn -= 1
        self.now_global()

    def PROCEDURE(self, p, i_id, i_params):
        if self.procfn != 0:
            raise RuntimeError("Nested procedure/function not allowed")

        id = p[i_id]
        params = p[i_params]
        self.out("def %s(%s):" % (id, params))
        self.indent()
        self.procfn += 1
        self.nest_stack.append(0) # count of statements in function
        self.now_local()

    def ENDPROCEDURE(self, p):
        c = self.nest_stack.pop()
        if c == 0:
            self.out("pass")
        self.outdent()
        self.procfn -= 1
        self.now_global()

    def callparams(self, p, i_params, i_expr):
        params = p[i_params]
        expr = p[i_expr]
        r = params + ", " + expr
        p[0] = r

    def proccall(self, p, i_id, i_params):
        id = p[i_id]
        params = p[i_params]
        self.out("%s(%s)" % (id, params))

    def fncall(self, p, i_id, i_params):
        id = p[i_id]
        params = p[i_params]
        r = "%s(%s)" % (id, params)
        p[0] = r

    def bracket(self, p, i_expr):
        expr = p[i_expr]
        r = "(" + expr + ")"
        p[0] = r

    def boolean(self, p, value):
        r = value
        p[0] = r


    #---- PASSED ON THE PARSE STACK -------------------------------------------

    def number(self, p, i_number):
        number = p[i_number]
        p[0]=str(number)

    def id(self, p, i_id):
        id = p[i_id]
        p[0]=id

    def string(self, p, i_string):
        string = p[i_string]
        p[0]=string

    def USERINPUT(self, p):
        p[0]="raw_input()"

    def LEN(self, p, i_id):
        id = p[i_id]
        r = "len(%s)" % id
        p[0] = r

    def plus(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "+" + str(right)
        p[0] = r

    def minus(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "-" + str(right)
        p[0] = r

    def times(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "*" + str(right)
        p[0] = r

    def divide(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "/" + str(right)
        p[0] = r

    def MOD(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "%" + str(right)
        p[0] = r

    def uminus(self, p, i_expr):
        expr = p[i_expr]
        r = "-" + str(expr)
        p[0] = r

    def uplus(self, p, i_expr):
        expr = p[i_expr]
        r = expr
        p[0] = r

    def NOT(self, p, i_expr):
        expr = p[i_expr]
        r = "! " + str(expr)
        p[0] = r

    def equal(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "==" + str(right)
        p[0] = r

    def notequal(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "!=" + str(right)
        p[0] = r

    def lessequal(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "<=" + str(right)
        p[0] = r

    def greaterequal(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + ">=" + str(right)
        p[0] = r

    def greater(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + ">" + str(right)
        p[0] = r

    def less(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "<" + str(right)
        p[0] = r

    def AND(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " and " + str(right)
        p[0] = r

    def OR(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " or " + str(right)
        p[0] = r

    def XOR(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + "^" + str(right)
        p[0] = r

    def array1dexpr(self, p, i_id, i_expr):
        """Read a 1D array"""
        id   = p[i_id]
        expr = p[i_expr]
        if not self.var_exists(id):
            raise ParserException("Read from an array that does not exist")
        r = "%s[%s]" % (id, expr)
        p[0] = r

    def array2dexpr(self, p, i_id, i_expr1, i_expr2):
        """Read a 2D array"""
        id   = p[i_id]
        expr1 = p[i_expr1]
        expr2 = p[i_expr2]
        if not self.var_exists(id):
            raise ParserException("Read from an array that does not exist")
        r = "%s[%s][%s]" % (id, expr1, expr2)
        p[0] = r




#----- TEST -------------------------------------------------------------------

def test():
    generator = Generator()
    # TODO call various methods with p parameters, to test output

if __name__ == "__main__":
    test()

# END
