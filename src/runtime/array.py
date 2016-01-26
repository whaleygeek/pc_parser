# pcode_array.py  19/01/2016  D.J.Whale
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


# END
