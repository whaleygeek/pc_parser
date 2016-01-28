# __main__.py  28/01/2016  D.J.Whale
#
# bootstrap for the zip file

from pcode import *
import sys

if sys.stdin.isatty():
    interactive()
else:
    batch()

# END