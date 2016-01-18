#! /bin/bash

cd sandbox

# copy in other files required to run the application

cp ../../src/pcode.py .
cp ../../src/pcode_lexer.py .
cp ../../src/pygen.py .

python pcode.py
cd ..