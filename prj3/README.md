## COP4620 Class Specs
The rule table below has my left recursion fixed grammer of the C- grammer.
I know there are some predict conflicts, so I made the generator let the User
handle those rules. Gives a nice warning comment on the function declaration.

I left the original generated one as the **og.py** file.

After my tool generated this,
  all I did was add accepts and fixed conflict functions.

### Semantics Supporting the following:
* functions declared int or float  must have a return value of the correct type.
* void functions may or may not have a return, but must not return a value.
* parameters and arguments agree in number
* parameters and arguments agree in type
* operand agreement
* operand/operator agreement
* array index agreement
* variable declaration (all variables must be declared ... scope)
* variable declaration (all variables declared once ... scope)
* void functions cannot have a return value
* each program must have one main function
* return only simple structures
* id's should not be type void
* each function should be defined (actually a linker error)

### Rule Table

|parentRule|subRule|first and follow(predict)|
|:---:|:--:|:--:|
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
|TermPr|MulOp Factor TermPr|\* /|
|TermPr|@|+ - >= <= > < == != , ) ;|
|MulOp|\*|\*|
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
