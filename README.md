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

Additionally:

* The function/proc is not called

I have modified my src/pcode_test.pc to fix these issues.


