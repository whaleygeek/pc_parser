#! /bin/bash

cd sandbox

# copy in other files required to run the application

cp ../../src/pcode.py .
cp ../../src/pcode_lexer.py .
cp ../../src/pygen.py .
cp ../../src/pcode_test.pc .
cp ../../src/runtime/*.py .
cp ../../src/tests.py .

python pcode.py < pcode_test.pc > pcode_test_out.py

#python tests.py

cd ..