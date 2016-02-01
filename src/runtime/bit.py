# bit.py  31/01/2015  D.J.Whale
#
# Add bit operations to pcode

def band(left, right):
    return left & right

def bor(left, right):
    return left | right

def bxor(left, right):
    return left ^ right

def bnot(value):
    return ~ value

def bshl(value, bits):
    return value << bits

def bshr(value, bits):
    return value >> bits

# END