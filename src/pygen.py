# pygen.py  17/01/2016  D.J.Whale
#
# Generator for pcode.py that generates python from each of the actions.


#TODO: Add in all parameter signatures
#TODO: Add in all debug bodies
#TODO: Add in p[0] assignment values

class Generator():
    def __init__(self):
        pass

    def OUTPUT(self, p):
        #print("output %s" % msg)
        print("Output")

    def assign(self, p):
        #print("assign %s %s" % (var, value))
        print("VarAssign")

    def array1assign(self, p):
        #print("assign array1 %s %s" % (index, value))
        print("Array1Assign")

    def array2assign(self, p):
        #print("assign array2 %s %s %s" % (index1, index2, value))
        print("Array2Assign")

    def arrayinit(self, p):
        pass # TODO
        print("ArrayInit")

    def READLINE(self, p):
        #print("READLINE %s %s" % (fileid, expr))
        print("ReadLine")

    def WRITELINE(self, p):
        #print("WRITELINE %s %s %s" % (fileid, expr1, expr2))
        print("WriteLine")

    def IF(self, p):
        #print("IF %s %s" % (expr, statements1))
        print("If")

    def IFELSE(self, p):
        #print("IF %s %s %s" % (expr, statements1, statements2))
        print("IfElse")

    def WHILE(self, p):
        #print("WHILE %s %s" % (expr, statements))
        print("While")

    def REPEAT(self, p):
        #print("REPEAT %s %s" % (statements, expr))
        print("Repeat")

    def FOR(self, p):
        #print("FOR %s %s %s %s" % (var, fromexpr, toexpr, statements))
        print("For")

    def WHILE(self, p):
        #print("WHILE %s %s" % (expr, statements))
        print("While")

    def caseoption(self, p):
        print("CaseOption")

    def CASE(self, p):
        #print("CASE %s %s %s" % (var, options, otherwise))
        print("Case")

    def defparams(self, p):
        print("DefParams")

    def FUNCTION(self, p):
        print("function")

    def RETURN(self, p):
        #expr = p[expridx]
        #print("RETURN %s" % expr)
        #p[0] = "Return"
        print("Return")

    def PROCEDURE(self, p):
        print("Procedure")

    def callparams(self, p):
        print("CallParams")

    def proccall(self, p):
        print("ProcCall")

    def fncall(self, p):
        print("FnCall")

    def number(self, p):
        print("Number")

    def id(self, p):
        print("Id")

    def string(self, p):
        print("String")

    def USERINPUT(self, p):
        #print("USERINPUT")
        print("UserInput")

    def LEN(self, p):
        #print("LEN")
        print("Len")

    def plus(self, p):
        #print("ADD %s %s" % (left, right))
        print("Add")

    def minus(self, p):
        #print("SUB %s %s" % (left, right))
        print("Sub")

    def times(self, p):
        #print("MULT %s %s" % (left, right))
        print("Times")

    def divide(self, p):
        #print("DIV %s %s" % (left, right))
        print("Divide")

    def mod(self, p):
        #print("MOD %s %s" % (left, right))
        print("Mod")

    def uminus(self, p):
        #print("NEG %s" % left)
        print("Uminus")

    def uplus(self, p):
        #print("POS %s" % left)
        print("Uplus")

    def NOT(self, p):
        #print("NOT %s" % expr)
        print("Not")

    def equal(self, p):
        #print("EQUAL %s %s" % (left, right))
        print("Equal")

    def notequal(self, p):
        #print("NOTEQUAL %s %s" % (left, right))
        print("NotEqual")

    def lessequal(self, p):
        #print("LESSEQUAL %s %s" % (left, right))
        print("LessEqual")

    def greaterequal(self, p):
        #print("GREATEREQUAL %s %s" % (left, right))
        print("GreaterEqual")

    def greater(self, p):
        #print("GREATER %s %s" % (left, right))
        print("Greater")

    def less(self, p):
        #print("LESS %s %s" % (left, right))
        print("Less")

    def AND(self, p):
        #print("AND %s %s" % (left, right))
        print("And")

    def OR(self, p):
        #print("OR %s %s" % (left, right))
        print("Or")

    def XOR(self, p):
        #print("XOR %s %s" % (left, right))
        print("Xor")

    def concat(self, p, *args):
        #print("TODO: concat:%s" % str(args))
        #TODO concat is done in backend rather than .y actions
        #so that we have full control over how it works,
        #as some concats might modify internal structures.
        print("Concat")



#----- TEST -------------------------------------------------------------------

def test():
    generator = Generator()
    # TODO call various methods with p parameters, to test output

if __name__ == "__main__":
    test()

# END
