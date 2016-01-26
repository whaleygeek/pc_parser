# pcode_io.py  19/01/2016  D.J.Whale

# simplest possible implementation. Only really works well
# for small files. Poor efficiency on large files.

class FileIOException(Exception):
    pass

def readline(filename, lineno):
    if type(lineno) != int:
        raise FileIOException("Line number must be an integer")

    if lineno < 1:
        raise FileIOException("Cannot read line number less than 1: %d" % lineno)

    lineno -= 1 # file offsets lines from zero

    f = open(filename)
    lines = f.readlines()
    f.close()
    if lineno >= len(lines):
        raise FileIOException("Attempt to read a line that does not exist in file: wanted:%d max:%d" % (lineno, len(lines)-1))

    return lines[lineno-1]

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
