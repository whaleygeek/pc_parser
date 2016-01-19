class Array():
    def __init__(self):
        self.data = []

    def __setitem__(self, index, value):
        l = len(self.data)
        if index >= l:
            missing = 1+(index-l)
            self.data.extend([0 for i in range(missing)])
        self.data[index] = value

    def __getitem__(self, index):
        if index >= len(self.data):
            return 0 # lazy construction
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)


class Array2D():
    def __init__(self):
        self.rows = []

    def __getitem__(self, index):
        l = len(self.rows)
        if index >= l:
            missing = 1+(index-l)
            self.rows.extend([Array() for i in range(missing)])
        return self.rows[index]

    def __repr__(self):
        return str(self.rows)


#TODO: helper for readline
#TODO: helper for writeline

def test():
    a = Array()
    a[20] = "Fred"
    print(a[20])
    print(a)

    b = Array2D()
    b[4][5]='45'
    print(b[4][5])
    print(b)

if __name__ == "__main__":
    test()
