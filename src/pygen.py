# pygen.py  17/01/2016  D.J.Whale
#
# Generator for pcode.py that generates python from each of the actions.

class Generator():
    def __init__(self):
        self.vars = {}

    def strcat(self, first, second):
        print("strcat:%s %s" % (first, second))
        return first + second

    def var_assign(self, var, value):
        print("varassign:%s %s" % (var, value))
        name = var.name
        self.vars[name] = value

    def output(self, msg):
        if type(msg) == str:
            print(msg)
        else: # assume instance for now
            name = msg.name
            value = self.vars[name]
            print(value)

#----- TEST -------------------------------------------------------------------

def test():
    generator = Generator()
    # TODO call various methods with p parameters, to test output

if __name__ == "__main__":
    test()

# END
