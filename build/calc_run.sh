#! /bin/bash

cd sandbox

# copy in other files required to run the application

cp ../../src/calc.py .
cp ../../src/calc_lexer.py

python calc.py
cd ..