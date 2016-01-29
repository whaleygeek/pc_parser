#! /bin/bash

# clear out any old build outputs
rm -rf sandbox
mkdir sandbox

# create a safe context to generate and run
cd sandbox
ln -s ../yply/ply ply

# generate the parser code from the yacc spec
# (note this will overwrite anything you added)

python ../yply/yply.py ../../src/pcode.y > pcode_parser.py



