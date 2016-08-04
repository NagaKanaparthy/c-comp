# Project 1 Compiler
## Due 1/26/16 Tuesday  at 11:59 PM (nearly midnight)
### Specification
Your project is to use the grammar definition in the appendix
of your text to guide the construction of a lexical analyzer. 
The lexical analyzer should return tokens as described. Keep 
in mind these tokens will serve as the input to the parser.
You must enhance the definitions by adding a keyword "float"
as a data type to the material on page 493 and beyond.
Specifically, rule 5 on page 492 should state

	type-specifier -> int | void | float

and any other modifications necessary must be included. 

Page 491 and 492 should be used to guide the construction of the
lexical analyzer. A few notable features:
```
0) the project's general goal is to construct a list of tokens capable
   of being passed to a parser.
1) comments should be totally ignored, not passed to the parser and
   not reported.
2) comments might be nested.
3) one line comments are designated by //
4) multiple line comments are designated by /* followed by */ in 
   a match up fashion for the nesting.
5) a symbol table* for identifiers should be constructed (as
   per recommendation of your text, I actually recommend
   construction of the symbol table during parsing).
   a) the symbol table should keep track of the identifier
   b) be extensible
   c) keep track of scope
   d) be constructed efficiently
   * this will not be evaluated until project 3
6) upon reporting of identifiers, their nesting depth/declarations
   should be displayed.
```
### Turn-In Procedure
Appropriate documentation as described in the Syllabus should 
be included. A shar file, including all files necessary, 
(makefile, source files, test files, documentation file
("text" in ascii format), and any other files) should be submitted 
by the deadline using turnin as follows:
```bash
   turnin fn ree4620_1
```
By my typing    make    after unsharing your file, I should see an
executable called p1, if you wrote your program in C,  that will 
perform the lexical analysis. 

The analyzer will be invoked with:
```bash
   p1 test_fn
```
where p1 is the executable resulting from the make command and
test_fn is the test filename upon which lexical analysis is to be 
done. You must supply a makefile for any language you chose to use,
including scripting languages. 

If you write in other languages, you must supply at p1 file 
that will execute your program.
For example, such a p1 file might appear as:
```bash
#!/bin/ksh
ruby your_ruby_script $1
```
OR
```bash
#!/bin/ksh
java your_java_pgm $1
```
OR
```bash
#!/bin/ksh
python your_python_script $1
```
The shar file can be created as follows:

shar fn1 fn2 fn3 fn4 > fn

You should NOT shar a directory, i.e. when I unshar your project
a new subdirectory should not be created.

You should test the integrity of your shar by: 1)copying it to a
temporary directory, 2)unsharing, 3)make, and 4)execute to see that
all files are present and that the project works appropriately. 

Failure to carefully follow these guidelines will result in penalty.
If you are not sure of some characteristic, ask to verify the 
desired procedure.

You should echo the input line followed by the output in a
sequential fashion.
