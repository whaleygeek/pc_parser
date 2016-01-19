class Cells():
    def __init__(self):
        self.cells = []

    def check(self, index):
        l = len(self.cells)
        if index > l:
            missing = 1+(index - l)
            print("creating %d items" % missing)
            self.cells.extend([0 for i in range(missing)])

    def __setitem__(self, index, value):
        self.check(index)
        self.cells[index] = value

    def __getitem__(self, index):
        print("getitem:%d" % index)
        self.check(index)
        return self.cells[index]

    def __repr__(self):
        return str(self.cells)

#TODO: helper for readline
#TODO: helper for writeline

def test():
    a = Cells()
    a[20] = "Fred"
    print(a[20])
    print(a)

if __name__ == "__main__":
    test()
