# pygen.py  17/01/2016  D.J.Whale
#
# Generator for pcode.py that generates python from each of the actions.


#TODO: Add in all parameter signatures
#TODO: Add in all debug bodies
#TODO: Add in p[0] assignment values

class Generator():
    def __init__(self):
        pass

    def OUTPUT(self, p, *args):
        #print("output %s" % msg)
        p[0]="Output"
        print(p[0])

    def assign(self, p, *args):
        #print("assign %s %s" % (var, value))
        p[0]="Varassign"
        print(p[0])

    def array1assign(self, p, *args):
        #print("assign array1 %s %s" % (index, value))
        p[0]="Array1assign"
        print(p[0])

    def array2assign(self, p, *args):
        #print("assign array2 %s %s %s" % (index1, index2, value))
        p[0]="Array2assign"
        print(p[0])

    def arrayinit(self, p, *args):
        p[0]="Arrayinit"
        print(p[0])

    def READLINE(self, p, *args):
        #print("READLINE %s %s" % (fileid, expr))
        p[0]="Readline"
        print(p[0])

    def WRITELINE(self, p, *args):
        #print("WRITELINE %s %s %s" % (fileid, expr1, expr2))
        p[0]="Writeline"
        print(p[0])

    def IF(self, p, *args):
        #print("IF %s %s" % (expr, statements1))
        p[0]="If"
        print(p[0])

    def IFELSE(self, p, *args):
        #print("IF %s %s %s" % (expr, statements1, statements2))
        p[0]="Ifelse"
        print(p[0])

    def WHILE(self, p, *args):
        #print("WHILE %s %s" % (expr, statements))
        p[0]="While"
        print(p[0])

    def REPEAT(self, p, *args):
        #print("REPEAT %s %s" % (statements, expr))
        p[0]="Repeat"
        print(p[0])

    def FOR(self, p, *args):
        #print("FOR %s %s %s %s" % (var, fromexpr, toexpr, statements))
        p[0]="For"
        print(p[0])

    def WHILE(self, p, *args):
        #print("WHILE %s %s" % (expr, statements))
        p[0]="While"
        print(p[0])

    def caseoption(self, p, *args):
        p[0]="Caseoption"
        print(p[0])

    def CASE(self, p, *args):
        #print("CASE %s %s %s" % (var, options, otherwise))
        p[0]="Case"
        print(p[0])

    def defparams(self, p, *args):
        p[0]="Defparams"
        print(p[0])

    def FUNCTION(self, p, *args):
        p[0]="Function"
        print(p[0])

    def RETURN(self, p, *args):
        #expr = p[expridx]
        #print("RETURN %s" % expr)
        p[0]="Return"
        print(p[0])

    def PROCEDURE(self, p, *args):
        p[0]="Procedure"
        print(p[0])

    def callparams(self, p, *args):
        p[0]="Callparams"
        print(p[0])

    def proccall(self, p, *args):
        p[0]="Proccall"
        print(p[0])

    def fncall(self, p, *args):
        p[0]="Fncall"
        print(p[0])

    def number(self, p, *args):
        p[0]="Number"
        print(p[0])

    def id(self, p, *args):
        p[0]="Id"
        print(p[0])

    def string(self, p, *args):
        p[0]="String"
        print(p[0])

    def USERINPUT(self, p, *args):
        #print("USERINPUT")
        p[0]="Userinput"
        print(p[0])

    def LEN(self, p, *args):
        #print("LEN")
        p[0]="Len"
        print(p[0])

    def plus(self, p, *args):
        #print("ADD %s %s" % (left, right))
        p[0]="Add"
        print(p[0])

    def minus(self, p, *args):
        #print("SUB %s %s" % (left, right))
        p[0]="Sub"
        print(p[0])

    def times(self, p, *args):
        #print("MULT %s %s" % (left, right))
        p[0]="Times"
        print(p[0])

    def divide(self, p, *args):
        #print("DIV %s %s" % (left, right))
        p[0]="Divide"
        print(p[0])

    def mod(self, p, *args):
        #print("MOD %s %s" % (left, right))
        p[0]="Mod"
        print(p[0])

    def uminus(self, p, *args):
        #print("NEG %s" % left)
        p[0]="Uminus"
        print(p[0])

    def uplus(self, p, *args):
        #print("POS %s" % left)
        p[0]="Uplus"
        print(p[0])

    def NOT(self, p, *args):
        #print("NOT %s" % expr)
        p[0]="Not"
        print(p[0])

    def equal(self, p, *args):
        #print("EQUAL %s %s" % (left, right))
        p[0]="Equal"
        print(p[0])

    def notequal(self, p, *args):
        #print("NOTEQUAL %s %s" % (left, right))
        p[0]="Notequal"
        print(p[0])

    def lessequal(self, p, *args):
        #print("LESSEQUAL %s %s" % (left, right))
        p[0]="Lessequal"
        print(p[0])

    def greaterequal(self, p, *args):
        #print("GREATEREQUAL %s %s" % (left, right))
        p[0]="Greaterequal"
        print(p[0])

    def greater(self, p, *args):
        #print("GREATER %s %s" % (left, right))
        p[0]="Greater"
        print(p[0])

    def less(self, p, *args):
        #print("LESS %s %s" % (left, right))
        p[0]="Less"
        print(p[0])

    def AND(self, p, *args):
        #print("AND %s %s" % (left, right))
        p[0]="And"
        print(p[0])

    def OR(self, p, *args):
        #print("OR %s %s" % (left, right))
        p[0]="Or"
        print(p[0])

    def XOR(self, p, *args):
        #print("XOR %s %s" % (left, right))
        p[0]="Xor"
        print(p[0])

    def concat(self, p, *args):
        #print("TODO: concat:%s" % str(args))
        #TODO concat is done in backend rather than .y actions
        #so that we have full control over how it works,
        #as some concats might modify internal structures.
        p[0]="Concat"
        print(p[0])



#----- TEST -------------------------------------------------------------------

def test():
    generator = Generator()
    # TODO call various methods with p parameters, to test output

if __name__ == "__main__":
    test()

# END
