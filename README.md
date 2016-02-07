# pc_parser
A simple pseudo-code parser, that generates runnable python code.

Inspired by this:

https://github.com/gbaman/Python-To-AQA-Pseudocode

and looking at this:

http://filestore.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF

I decided to use this:

http://www.dabeaz.com/ply/

to build something that would turn Pseudo Code into real code.

(It's a component of a bigger project, but pretty much a stand-alone
implementation)




RELEASE NOTE
----

SMOKE TEST
---
Either:

    git clone https://github.com/whaleygeek/pc_parser

Or: Press the DOWNLOAD AS ZIP and unzip the zip archive

Then:

    cd pc_parser/build/release
    python pcode.zip < test.pc > test.py
    python test.py

KNOWN ISSUES
---
1. fileio.py and arrays.py have to be in your directory
2. there are ambiguities on global variables in functions depending on where declared
3. you can't write to global variables in functions 
4. python 2 support only (at the moment)
5. It strips out all your comments (at the moment)
6. No documentation at all (but read the AQA spec)
http://filestore.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF



Suggested changes to the AQA grammar
---

The CASE statement is ambiguous, it generates a lot of
shift/reduce parse warnings. I have added WHEN prior to the case option expressions
to resolve this ambiguity in the grammar. This is because something like this:

    CASE a OF
    1: b <- 1 + 2
    -3: c <- 2 + 4
    ENDCASE
    
i.e. there are two possible outcomes, either b<-1 + 2 or b<-1 + 2 - 3
and hence the grammar is ambiguous.

readline and writeline take non quoted names for files as the filename parameter.
This is generally bad, because a filename could have spaces or other lexical symbols
in it, including a comma, like this

    writeline(myfile-with,name.txt, 4, "data")

I have mandated that filenames must be strings. This also then means that the
name of the file can now be a string variable as well as a string literal:

    writeline("myfile-with,name.txt", 4, "data")
    writeline(myfilename, 5, data)

