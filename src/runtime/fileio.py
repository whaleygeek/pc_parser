# fileio.py  19/01/2016  D.J.Whale

# simplest possible implementation. Only really works well
# for small files. Poor efficiency on large files.

import os

class FileIOException(Exception):
    pass

def readline(filename, lineno):
    if type(lineno) != int:
        raise FileIOException("Line number must be an integer")

    if lineno < 1:
        raise FileIOException("Cannot read line number less than 1: %d" % lineno)

    lineno -= 1 # file offsets lines from zero

    f = open(filename) #TODO: What if file does not exist?
    lines = f.readlines()
    f.close()
    if lineno >= len(lines):
        raise FileIOException("Attempt to read a line that does not exist in file: wanted:%d max:%d" % (lineno, len(lines)-1))

    return lines[lineno-1]

def writeline(filename, lineno, data):
    # read all lines in
    f = open(filename, "w+")
    lines = f.readlines()
    f.close()

    # modify in-memory copy first, so that the line exists
    lineno -= 1
    if lineno >= len(lines):
        # pad out extra lines as blanks
        for i in range(1+lineno-len(lines)):
            lines.append("\n")
    lines[lineno] = data + '\n'

    # now create a brand new file and write all the lines out
    os.remove(filename)
    f = open(filename, "w")
    f.writelines(lines)
    f.close()


# END
