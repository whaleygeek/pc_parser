# tests.py  26/01/2016  D.J.Whale

import unittest
import pcode

#----- TEST SYNTAX ------------------------------------------------------------

class TestSyntax(unittest.TestCase):
    IMPORTS = "from io import *\nfrom array import *\n"

    def test_output(self):
        SRC = \
"""OUTPUT "hello"
"""

        EXPECTED = self.IMPORTS + \
"""print("hello")
"""

        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)


#----- TEST ARRAYS ------------------------------------------------------------
#class TestArrays(unittest.TestCase)
#    pass

#----- TEST IO ----------------------------------------------------------------
#class TestIO(unittest.TestCase):
#    pass

#----- TEST RUNTIME -----------------------------------------------------------
#class TestRuntime(unittest.TestCase):
#    pass


if __name__ == "__main__":
    unittest.main()

