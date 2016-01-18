# pygen.py  17/01/2016  D.J.Whale
#
# Generator for pcode.py that generates python from each of the actions.

class Generator():
    def __init__(self):
        pass

    def var_assign(self, var, value):
        print("assign %s %s" % (var, value))
        return "VarAssign"

    def array1assign(self, index, value):
        print("assign array1 %s %s" % (index, value))
        return "Array1Assign"

    def array2assign(self, index1, index2, value):
        print("assign array2 %s %s %s" % (index1, index2, value))
        return "Array2Assign"

    def iplus(self, left, right):
        print("ADD %s %s" % (left, right))
        return "Add"

    def iminus(self, left, right):
        print("SUB %s %s" % (left, right))
        return "Sub"

    def itimes(self, left, right):
        print("MULT %s %s" % (left, right))
        return "Mult"

    def idivide(self, left, right):
        print("DIV %s %s" % (left, right))
        return "Div"

    def imod(self, left, right):
        print("MOD %s %s" % (left, right))
        return "Mod"

    def iuminus(self, left):
        print("NEG %s" % left)
        return "Neg"

    def output(self, msg):
        print("output %s" % msg)
        return "Output"

    def IF(self, expr, statements1, statements2):
        print("IF %s %s %s" % (expr, statements1, statements2))
        return "If"

    def LEN(self, id):
        print("LEN %s" % id)
        return "Len"

    def USERINPUT(self):
        print("USERINPUT")
        return "UserInput"

    def NOT(self, expr):
        print("NOT %s" % expr)
        return "Not"

    def EQUAL(self, left, right):
        print("EQUAL %s %s" % (left, right))
        return "Equal"

    def NOTEQUAL(self, left, right):
        print("NOTEQUAL %s %s" % (left, right))
        return "NotEqual"

    def LESSEQUAL(self, left, right):
        print("LESSEQUAL %s %s" % (left, right))
        return "LessEqual"

    def GREATEREQUAL(self, left, right):
        print("GREATEREQUAL %s %s" % (left, right))
        return "GreaterEqual"

    def GREATER(self, left, right):
        print("GREATER %s %s" % (left, right))
        return "Greater"

    def LESS(self, left, right):
        print("LESS %s %s" % (left, right))
        return "Less"

    def AND(self, left, right):
        print("AND %s %s" % (left, right))
        return "And"

    def OR(self, left, right):
        print("OR %s %s" % (left, right))
        return "Or"

    def XOR(self, left, right):
        print("XOR %s %s" % (left, right))
        return "XOR"

    def READLINE(self, fileid, expr):
        print("READLINE %s %s" % (fileid, expr))
        return "ReadLine"

    def WRITELINE(self, fileid, expr1, expr2):
        print("WRITELINE %s %s %s" % (fileid, expr1, expr2))
        return "WriteLine"

    def WHILE(self, expr, statements):
        print("WHILE %s %s" % (expr, statements))
        return "While"

    def REPEATUNTIL(self, statements, expr):
        print("REPEATUNTIL %s %s" % (statements, expr))
        return "RepeatUntil"

    def FOR(self, var, fromexpr, toexpr, statements):
        print("FOR %s %s %s %s" % (var, fromexpr, toexpr, statements))
        return "For"

    def CASE(self, var, options, otherwise):
        print("CASE %s %s %s" % (var, options, otherwise))
        return "Case"


#----- TEST -------------------------------------------------------------------

def test():
    generator = Generator()
    # TODO call various methods with p parameters, to test output

if __name__ == "__main__":
    test()

# END
