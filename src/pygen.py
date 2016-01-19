# pygen.py  17/01/2016  D.J.Whale
#
# Generator for pcode.py that generates python from each of the actions.

class Generator():
    def __init__(self):
        pass

    def out(self, msg):
        import sys
        sys.stdout.write(msg + " ")

    def OUTPUT(self, p, i_expr):
        p[0]="Output"
        expr = p[i_expr]
        print("print(%s)" % str(expr))

    def assign(self, p, i_id, i_expr):
        p[0]="Varassign"
        #self.out(p[0])
        id = p[i_id]
        expr = p[i_expr]
        print("%s = %s" % (id, expr))

    def array1assign(self, p, i_id, i_indexexpr, i_valueexpr):
        id = p[i_id]
        indexexpr = p[i_indexexpr]
        valueexpr = p[i_valueexpr]
        p[0]="Array1assign"
        #self.out(p[0])

    def array2assign(self, p, i_id, i_index1expr, i_index2expr, i_valueexpr):
        id = p[i_id]
        index1expr = p[i_index1expr]
        index2expr = p[i_index2expr]
        valueexpr  = p[i_valueexpr]
        p[0]="Array2assign"
        #self.out(p[0])

    def arrayinit(self, p, i_id, i_initialiser):
        id = p[i_id]
        initialiser = p[i_initialiser]
        p[0]="Arrayinit"
        #self.out(p[0])

    def READLINE(self, p, i_file, i_expr):
        file = p[i_file]
        expr = p[i_expr]
        p[0]="Readline"
        #self.out(p[0])

    def WRITELINE(self, p, i_file, i_expr1, i_expr2):
        file = p[i_file]
        expr1 = p[i_expr1]
        expr2 = p[i_expr2]
        p[0]="Writeline"
        #self.out(p[0])

    def IF(self, p, i_expr):
        p[0]="If"
        #self.out(p[0])
        expr = p[i_expr]
        print("if %s:" % expr)

    def ELSE(self, p):
        p[0]="Ifelse"
        print("else:")

    def WHILE(self, p, i_expr):
        p[0]="While"
        expr = p[i_expr]
        print("while %s:" % expr)
        #TODO increment indent

    def ENDWHILE(self, p):
        pass # TODO decrement indent
        print("#endwhile")

    def UNTIL(self, p, i_expr):
        expr = p[i_expr]
        p[0]="Until"

    def FOR(self, p, i_id, i_from, i_to):
        id = p[i_id]
        f = p[i_from]
        t = p[i_to]
        p[0]="For"

    def caseoption(self, p, i_expr):
        expr = p[i_expr]
        p[0]="Caseoption"

    def CASE(self, p, i_expr):
        expr = p[i_expr]
        p[0]="Case"

    def defparams(self, p, i_params, i_id):
        params = p[i_params]
        id = p[i_id]
        p[0]="Defparams"

    def FUNCTION(self, p, i_id, i_params):
        p[0]="Function"
        id = p[i_id]
        params = p[i_params]
        print("def %s(%s):\n" % (id, params))

    def RETURN(self, p, i_expr):
        expr = p[i_expr]
        p[0]="Return"

    def PROCEDURE(self, p, i_id, i_params):
        id = p[i_id]
        params = p[i_params]
        p[0]="Procedure"
        params = p[i_params]
        print("def %s(%s):\n" % (id, params))

    def callparams(self, p, i_params, i_expr):
        params = p[i_params]
        expr = p[i_expr]
        p[0]="Callparams"

    def proccall(self, p, i_id, i_params):
        p[0]="Proccall"
        id = p[i_id]
        params = p[i_params]
        print("%s(%s)" % (id, params))

    def fncall(self, p, i_id, i_params):
        id = p[i_id]
        params = p[i_params]
        p[0]="Fncall"

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
        r = str(left) + " + " + str(right)
        p[0] = r

    def minus(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " - " + str(right)
        p[0] = r

    def times(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " * " + str(right)
        p[0] = r

    def divide(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " / " + str(right)
        p[0] = r

    def mod(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " % " + str(right)
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
        r = str(left) + " == " + str(right)
        p[0] = r

    def notequal(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " != " + str(right)
        p[0] = r

    def lessequal(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " <= " + str(right)
        p[0] = r

    def greaterequal(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " >= " + str(right)
        p[0] = r

    def greater(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " > " + str(right)
        p[0] = r

    def less(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = str(left) + " < " + str(right)
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

    def concat(self, p, i_one, i_two):
        one = p[i_one]
        two = p[i_two]
        both = one + two
        p[0] = both



#----- TEST -------------------------------------------------------------------

def test():
    generator = Generator()
    # TODO call various methods with p parameters, to test output

if __name__ == "__main__":
    test()

# END
