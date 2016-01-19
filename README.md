# pc_parser
A simple pseudo-code parser

Inspired by this:

https://github.com/gbaman/Python-To-AQA-Pseudocode

and looking at this:

http://filestore.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF

I decided to use this:

http://www.dabeaz.com/ply/

to build something that would turn Pseudo Code into real code.

(It's a component of a bigger project, but pretty much a stand-alone
implementation)

Target testdata is informed from here by gbaman:
http://pastebin.com/FvcuPGW4

Note: This test file is not valid AQA syntax, for the following reasons:

* should be no colon at end of FUNCTION

* colons at end of IF should be THEN

* the use of ELSEIF is not allowed

* there is no ENDFUNCTION

* the FUNCTION should be a PROCEDURE, because it does not return a result

* The function/proc is not called

Suggested changes to the AQA grammer

* The CASE statement is ambiguous, it generates a lot of
shift/reduce parse warnings. I have added WHEN prior to the case option expressions
to resolve this ambiguity in the grammar. This is because something like this:

    CASE a OF
    1: b <- 1 + 2
    -3: c <- 2 + 4
    ENDCASE
    
i.e. there are two possible outcomes, either b<-1 + 2 or b<-1 + 2 - 3
and hence the grammar is ambiguous.

* readline and writeline take non quoted names for files as the filename parameter.
This is generally bad, because a filename could have spaces or other lexical symbols
in it, including a comma, like this

    writeline(myfile-with,name.txt, 4, "data")

I have mandated that filenames must be strings. This also then means that the
name of the file can now be a string variable as well as a string literal:

    writeline("myfile-with,name.txt", 4, "data")
    writeline(myfilename, 5, data)

