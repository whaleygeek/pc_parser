# pygen.py  17/01/2016  D.J.Whale
#
# Generator for pcode.py that generates python from each of the actions.

class Generator():
    def strcat(self, p):
        print("strcat:%s %s" % (p[1], p[3]))
        p[0] = p[1] + p[3]

    def output(self, p):
        print("output:%s" % p[2])

#----- TEST -------------------------------------------------------------------

def test():
    generator = Generator()
    # TODO call various methods with p parameters, to test output

if __name__ == "__main__":
    test()

# END
