# Python Parser Generator Assistance (PPGA)
##### I like the word FPGA :D No Idea how to program one though :C
### Nagavarun Kanaparthy

## Purpose
This was for my COP4620 Compilers class with Dr. Eggen. After the class is
complete I plan to branch out to creating LL1 parsers for some common
Serial Communication and bit level parsing.

This will be used on the UNF TALON's Robosub and for speeding up
interfacing sensors into the robot's system.

May be also used for UNF IEEE Southeast Robot. <- not as complicated

## Usage
Have the grammar in a csv format using | as the delimiter. You can use
[this](http://hackingoff.com/compilers/predict-first-follow-set) website to help
calculate the predicts and see the first and follows. the tokens should be space
delimited.

1. Look at the **grammer.form** file for an example grammer.
  * **Empty** is the **@** symbol
2. Look at the **token.form** file for an example file with kw
3. Have your lex analyzer do the token handling you can use the **token.py**
file to get an idea of how your tokens should look like.


## COP4620 Class Specs
The rule table below has my left recursion fixed grammer of the C- grammer.
I know there are some predict conflicts, so I made the generator let the User
handle those rules. Gives a nice warning comment on the function declaration.

I left the original generated one as the **og.py** file.

After my tool generated this,
  all I did was add accepts and fixed conflict functions.

### Rule Table
|parentRule|subRule|first and follow(predict)|
|--|--|--|
|Program|DeclarationList|int float void|
|DeclarationList|Declaration DeclarationListPr|int float void|
|DeclarationListPr|Declaration DeclarationListPr|int float void|
|DeclarationListPr|@|$|
|Declaration|VarDeclaration|int float void|
|Declaration|FunDeclaration|int float void|
|VarDeclaration|TypeSpecifier id|int float void|
|VarDeclaration|TypeSpecifier [ num ]|int float void|
|TypeSpecifier|int|int|
|TypeSpecifier|float|float|
|TypeSpecifier|void|void|
|FunDeclaration|TypeSpecifier id ( Params ) CmpdStatement|int float void|
|Params|ParamList|int float void|
|Params|void|void|
|ParamList|Param ParamListPr|int float void|
|ParamListPr|, Param ParamListPr|,|
|ParamListPr|@|)|
|Param|TypeSpecifier id|int float void|
|Param|TypeSpecifier id [ ]|int float void|
|CmpdStatement|{ LocalDeclaration StatementList }|{|
|LocalDeclaration|VarDeclaration LocalDeclaration|int float void|
|LocalDeclaration|@|; id ( num if return { while|
|StatementList|Statement StatementList|; id ( num if return { while|
|StatementList|@|}|
|Statement|ExpressionStatement|; id ( num|
|Statement|CmpdStatement|{|
|Statement|SelectionStatement|if|
|Statement|IterationStatement|while|
|Statement|ReturnStatement|return|
|ExpressionStatement|Expression ;|id ( num|
|ExpressionStatement|;|;|
|SelectionStatement|if ( Expression ) Statement|if|
|SelectionStatement|if ( Expression ) Statement else Statement|if|
|IterationStatement|while ( Expression ) Statement|while|
|ReturnStatement|return ;|return|
|ReturnStatement|return Expression ;|return|
|Expression|Var = Expression|id|
|Expression|SimpleExpression|( num id|
|Var|id|id|
|Var|id [ Expression ]|id|
|SimpleExpression|AddExpression RelOp AddExpression|( num id|
|RelOp|>=|>=|
|RelOp|<=|<=|
|RelOp|>|>|
|RelOp|<|<|
|RelOp|==|==|
|RelOp|!=|!=|
|AddExpression|Term AddExpressionPr|( num id|
|AddExpressionPr|AddOp Term AddExpressionPr|+ -|
|AddExpressionPr|@|>= <= > < == != , ) ;|
|AddOp|+|+|
|AddOp|-|-|
|Term|Factor TermPr|( num id|
|TermPr|MulOp Factor TermPr|* /|
|TermPr|@|+ - >= <= > < == != , ) ;|
|MulOp|*|*|
|MulOp|/|/|
|Factor|( Expression )|(|
|Factor|Var|id|
|Factor|Call|id|
|Factor|num|num|
|Call|id ( Args )|id|
|Args|ArgsList|id ( num ,|
|Args|@|)|
|ArgsList|Expression|id ( num|
|ArgsList|ArgsListPr|,|
|ArgsListPr|, Expression ArgsListPr|,|
|ArgsListPr|@|)|
