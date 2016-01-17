#! /bin/bash

# clear out any old build outputs
rm -rf sandbox
mkdir sandbox

# create a safe context to generate and run
cd sandbox
ln -s ../ply ply

# generate the parser code from the yacc spec
# (note this will overwrite anything you added)

python ../yply/yply.py ../../src/calc.y > calc_parser.py

.


