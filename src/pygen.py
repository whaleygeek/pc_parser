# pygen.py  17/01/2016  D.J.Whale
#
# Generator for pcode.py that generates python from each of the actions.


#TODO: Add in all parameter signatures
#TODO: Add in all debug bodies
#TODO: Add in p[0] assignment values

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
        p[0]="Array1assign"
        #self.out(p[0])

    def array2assign(self, p, i_id, i_index1expr, i_index2expr, i_valueexpr):
        p[0]="Array2assign"
        #self.out(p[0])

    def arrayinit(self, p, i_id, i_initialiser):
        p[0]="Arrayinit"
        #self.out(p[0])

    def READLINE(self, p, i_file, i_expr):
        p[0]="Readline"
        #self.out(p[0])

    def WRITELINE(self, p, i_file, i_expr1, i_expr2):
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
        #self.out(p[0])
        expr = p[i_expr]
        print("while %s:" % expr)
        #TODO increment indent

    def ENDWHILE(self, p):
        pass # TODO decrement indent
        print("#endwhile")

    def REPEAT(self, p, i_statements, i_expr):
        ##TODO use embed to pass header only
        p[0]="Repeat"
        #self.out(p[0])

    def FOR(self, p, i_id, i_from, i_to, i_statements):
        ##TODO use embed to pass header only
        p[0]="For"
        #self.out(p[0])

    def caseoption(self, p, i_expr, i_statements):
        ##TODO use embed to pass header only
        p[0]="Caseoption"
        #self.out(p[0])

    def CASE(self, p, i_expr, i_options, i_elsestatements):
        ##TODO use embed to pass header only
        p[0]="Case"
        #self.out(p[0])

    def defparams(self, p, i_params, i_id):
        p[0]="Defparams"
        #self.out(p[0])

    def FUNCTION(self, p, i_id, i_params, i_statements):
        ##TODO use an embed to pass header only
        p[0]="Function"
        #self.out(p[0])
        id = p[i_id]
        params = p[i_params]
        statements = p[i_statements]
        print("def %s(%s):\n\t%s" % (id, params, statements))

    def RETURN(self, p, i_expr):
        p[0]="Return"
        #self.out(p[0])

    def PROCEDURE(self, p, i_id, i_params, i_statements):
        ##TODO use an embed to pass header only
        p[0]="Procedure"
        #self.out(p[0])
        id = p[i_id]
        params = p[i_params]
        statements = p[i_statements]
        print("def %s(%s):\n\t%s" % (id, params, statements))

    def callparams(self, p, i_params, i_expr):
        p[0]="Callparams"
        #self.out(p[0])

    def proccall(self, p, i_id, i_params):
        p[0]="Proccall"
        #self.out(p[0])
        id = p[i_id]
        params = p[i_params]
        print("%s(%s)" % (id, params))

    def fncall(self, p, i_id, i_params):
        p[0]="Fncall"
        #self.out(p[0])

    def number(self, p):
        p[0]="Number"
        #self.out(p[0])

    def id(self, p):
        p[0]="Id"
        #self.out(p[0])

    def string(self, p):
        p[0]="String"
        #self.out(p[0])

    def USERINPUT(self, p):
        p[0]="Userinput"
        #self.out(p[0])

    def LEN(self, p, i_id):
        p[0]="Len"
        #self.out(p[0])

    def plus(self, p, i_left, i_right):
        #p[0]="Add"
        #self.out(p[0])
        left = p[i_left]
        right = p[i_right]
        r = "%s + %s" % (left, right)
        p[0] = r

    def minus(self, p, i_left, i_right):
        p[0]="Sub"
        #self.out(p[0])

    def times(self, p, i_left, i_right):
        p[0]="Times"
        #self.out(p[0])

    def divide(self, p, i_left, i_right):
        p[0]="Divide"
        #self.out(p[0])

    def mod(self, p, i_left, i_right):
        p[0]="Mod"
        #self.out(p[0])

    def uminus(self, p, i_expr):
        p[0]="Uminus"
        #self.out(p[0])

    def uplus(self, p, i_expr):
        p[0]="Uplus"
        #self.out(p[0])

    def NOT(self, p, i_expr):
        p[0]="Not"
        #self.out(p[0])

    def equal(self, p, i_left, i_right):
        p[0]="Equal"
        #self.out(p[0])
        left = p[i_left]
        right = p[i_right]
        print("%s == %s" % (left, right))

    def notequal(self, p, i_left, i_right):
        p[0]="Notequal"
        #self.out(p[0])

    def lessequal(self, p, i_left, i_right):
        p[0]="Lessequal"
        #self.out(p[0])

    def greaterequal(self, p, i_left, i_right):
        p[0]="Greaterequal"
        #self.out(p[0])

    def greater(self, p, i_left, i_right):
        p[0]="Greater"
        #self.out(p[0])

    def less(self, p, i_left, i_right):
        left = p[i_left]
        right = p[i_right]
        r = "%s < %s" % (left, right)
        p[0]=r
        #self.out(p[0])

    def AND(self, p, i_left, i_right):
        p[0]="And"
        #self.out(p[0])

    def OR(self, p, i_left, i_right):
        p[0]="Or"
        #self.out(p[0])

    def XOR(self, p, i_left, i_right):
        p[0]="Xor"
        #self.out(p[0])

    def concat(self, p, i_one, i_two):
        ##TODO not sure what to do with this, perhaps make p[0] a list with two items??
        #merge any lists inside one and two into a single list?
        #p[0]="Concat"
        #self.out(p[0])
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
