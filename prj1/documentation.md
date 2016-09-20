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
commentFSM <- handles the comment removal speed
Lex <- does all the work
p1 <- simple runner
### Testing
The sample test programs are within tests folder.
### Methodology
I went about this in a Object orientated way due to time 
limitations. A real faster compiler would do away with
the objects and just use the functions with in the class.
This lexical analyzer could have been just a set of functions. The way
I did it allows it to be a option. If further speed would be
needed, you could rewrite the algorithms into c/c++ and write
a python wrapper to use inside python. For the comment removal,
I wrote a finite state machine to help handle the unquie comment
structure.

I split the program into three processes that run serially.
The first and second process is striping the comments out.
The third flags each token. I do not build the symbol table.
The first process strips single line and multi line comments.
The second process  tokenizes cleaned file
The third process analyzes the tokens.
### Notable libraries/language features used
- regex <- helps with flagging tokens
#challenges and feedback on project one
Multiline comment removal feature.
I struggled with adding this feature due to tracking the /*
and */ tokens. Orginally I wrote the multi line comment detector
to leverage the regex features within python. This caused a significant
amount of overhead to try organizing the detection. Ultimatly, I switched
to a manual character by character search. I wrote a Finite
State Machine to handle the changes. The diagram can be found in
the fsm.png. Additional comments in the classes are present.
