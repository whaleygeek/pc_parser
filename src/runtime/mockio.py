# mockio.py  28/01/2016  D.J.Whale
#
# Mocking input and output functions, primarily for unit testing.

outbuf = []
inbuf  = []

def output(msg):
    """Write a line of data to the mock output buffer"""
    global outbuf
    outbuf.append(str(msg))

def input(msg=None):
    """Read a line of data from the mock input buffer"""
    global inbuf

    if len(inbuf) == 0:
        raise RuntimeError("Nothing in fileio.inbuf to mock with")
    if msg != None:
        output(msg)
    return inbuf.pop()

# END

