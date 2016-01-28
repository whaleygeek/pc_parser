#! /bin/bash

SRC=../../src
SANDBOX=sandbox
REL=release
YPLY=../yply/yply.py

# clear out any old build outputs
rm -rf $SANDBOX
mkdir $SANDBOX

# create a safe context to generate and run
cd $SANDBOX
cp -r ../yply/ply ply

# generate the parser code from the yacc spec
# (note this will overwrite anything you added)

python $YPLY $SRC/pcode.y > pcode_parser.py


# copy in other files required to run the application

cp $SRC/pcode.py .
cp $SRC/pcode_lexer.py .
cp $SRC/pygen.py .
cp $SRC/__main__.py .

# run it with no input, to generate the parse tables
python pcode.py < /dev/null

# zip it up
zip -r pcode.zip *

cd ..
rm -rf $REL
mkdir $REL
cd $REL
cp ../$SANDBOX/pcode.zip .
cp $SRC/runtime/arrays.py .
cp $SRC/runtime/fileio.py .

# smoke test it
cat <<ENDPROG > test.pc
FOR a<-1 TO 10
  OUTPUT "hello"
ENDFOR
ENDPROG

python pcode.zip < test.pc > test.py
python test.py




