# Project 1 documentation
## Nagavarun Kanaparthy
## 8/24/2016
### Project Scope
Build a lexical analyzer for the c- language
#### Additional features
-nested comments support
-float support
### Lexical Analyzer Components
- Remove singleline comments
- Remove multiline comments
- Analyze Tokens
### Classes
Lex <- does all the work
p1 <- simple runner
### Testing
The sample test programs are within tests folder.
Unit testing documents are within tests/units folder.
You can run my tests by running using the ./test.sh
You can run the following unit tests in the unit tests folder
- python sline.py
- python nComm.py
- python tokenAnalyzer.py
### Methodology
I went about this in a Object orientated way due to time 
limitations. A real faster compiler would do away with
the objects and just use the functions with in the class.
This lexical analyzer could have been just a set of functions. The way
I did it allows it to be a option. If further speed would be
needed, you could rewrite the algorithms into c/c++ and write
a python wrapper to use inside python.

I split the program into three processes that run serially.
The first and second process is striping the comments out.
The third flags each token. I do not build the symbol table.
The first process strips single line comments.
The second process strips the multi-line/nested comments.
The third process analyzes the tokens.
### Notable libraries/language features used
- regex <- helps with flagging tokens
- pytest <- for unit testing

#challenges and feedback on project one
Multiline comment removal feature.
I struggled with adding this feature due to tracking the /*
and */ tokens. Orginally I wrote the multi line comment detector
to leverage the regex features within python. This caused a significant
amount of overhead to try organizing the detection. Ultimatly, I switched
to a manual character by character search. Next time I write a lexical
analyzer that supports nested comment i will do a char by char comparison.
