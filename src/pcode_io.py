# pcode_io.py  19/01/2016  D.J.Whale

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

# END
