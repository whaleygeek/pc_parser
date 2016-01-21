# helpers.py  19/01/2016  D.J.Whale
#
# Destined to be a runtime support library for code that has been converted
# from AQA pseudocode into python.

class Array():
    def __init__(self, *args):
        self.data = []
        if len(args) != 0:
            for a in args:
                self.data.append(a)

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

# simplest possible implementation. Only really works well
# for small files.

def readline(filename, lineno):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines[lineno-1] # runtime error if does not exist

def writeline(filename, lineno, data):
    # read all lines in
    f = open(filename)
    lines = f.readlines()
    f.close()

    # modify in-memory copy first
    lineno -= 1
    if lineno >= len(lines):
        # pad out extra lines as blanks
        for i in range(1+lineno-len(lines)):
            lines.append("")
    lines[lineno] = data

    # now create a brand new file and write all the lines out
    f = open(filename, "w")
    f.writelines(lines)
    f.close()


def test_arrays():
    a = Array()
    a[20] = "Fred"
    print(a[20])
    print(a)

    b = Array2D()
    b[4][5]='45'
    print(b[4][5])
    print(b)

def test_files():
    pass

if __name__ == "__main__":
    test_arrays()
    # test_files()