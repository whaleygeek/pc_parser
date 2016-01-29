# base.py  29/01/2016  D.J.Whale
#
# Provide simple base independent literals and conversions

# n = base_hex("A3")
# n = base_hex("DEADBEEF")

def hex(s):
    """Convert s as a hex string into a number.
    Supports 1,2,3,4 byte numbers."""
    pass

# a = base_hex_array("A01237EC12120D0A")

def hex_array(s):
    """Convert s as a hex string into an array initialiser.
    This probably just needs to be a list of numbers, and make sure
    that the array initialiser will work with any expression which
    is a list."""
    pass

# OUTPUT to_hexstr(42)
# OUTPUT to_hexstr(32767, 4)

def to_hexstr(n, bytes=1):
    """convert n into a hex string, honoring the bytes as the max width.
    Note that varargs by default are supported, so this should work."""
    pass

# END
