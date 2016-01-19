class Cells():
    def __init__(self):
        self.cells = []

    def __setitem__(self, index, value):
        l = len(self.cells)
        if index > l:
            missing = 1+(index - l)
            self.cells.extend([0 for i in range(missing)])
        self.cells[index] = value

    def __getitem__(self, index):
        if index > len(self.cells):
            return 0 # lazy construction
        return self.cells[index]

    def __len__(self):
        return len(self.cells)

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
