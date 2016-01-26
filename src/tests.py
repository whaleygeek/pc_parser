# tests.py  26/01/2016  D.J.Whale

import unittest
import pcode

#----- TEST SYNTAX ------------------------------------------------------------

class TestSyntax(unittest.TestCase):
    IMPORTS = "from io import *\nfrom array import *"

    #--------------------------------------------------------------------------
    def test_emptyproc(self):
        SRC = \
"""
PROCEDURE test_emptyproc()
ENDPROCEDURE
"""
        EXPECTED = self.IMPORTS + \
"""
def test_emptyproc():
    pass
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_emptyfn(self):
        SRC = \
"""
FUNCTION test_emptyfn()
ENDFUNCTION
"""

    #--------------------------------------------------------------------------
    def test_output(self):
        SRC = \
"""
OUTPUT "hello"
"""
        EXPECTED = self.IMPORTS + \
"""
print("hello")
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_assign(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)

    #--------------------------------------------------------------------------
    def test_array1d_assign(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_array2d_assign(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_array_init(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_array_read(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_array2d_read(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_if(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_if_else(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_empty_if_else(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_while(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_empty_while(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_repeat(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_for(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_empty_for(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_case(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_true_false(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_number(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_id(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_string(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_brackets(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_len(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_plus(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_minus(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_times(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_divide(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_mod(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_uminus(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_uplus(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_equal(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_lessequal(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_greaterequal(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_less(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_greater(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_notequal(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_and(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_or(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_xor(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_readline(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fncall_noparams(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fncall_1param(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fncall_2params(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_proccall_1param(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_proccall_2params(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fn_global_array(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fn_bubble_arrayGH(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
"""
        OUT = pcode.test(SRC)
        self.assertEquals(EXPECTED, OUT)
    
    #--------------------------------------------------------------------------
    def test_fn_bubble_arrayIJ(self):
        SRC = \
"""
"""
        EXPECTED = self.IMPORTS + \
"""
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

