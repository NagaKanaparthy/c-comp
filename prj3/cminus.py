import sys
from to import Token
class cminus:
	def __init__(self, tokenList):
		tokenList.append(Token("$","$"))
		self.tokenList = tokenList
		self.currentTokenNumber = 0
		self.currentToken=tokenList[0]
		self.debug = True
	def nextToken(self):
		if(self.currentTokenNumber < len(self.tokenList)):
			self.currentTokenNumber += 1
		self.currentToken = self.tokenList[self.currentTokenNumber]
	def AddExpressionPr(self):
		if(self.debug):
			print ("AddExpressionPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/"):
			self.AddOp()
			self.Term()
			self.AddExpressionPr()
		else:
			if(self.debug):
				debugStatement ="in AddExpressionPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ExpressionPr(self):
		if(self.debug):
			print ("ExpressionPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="[" or self.currentToken.getType().strip()=="=" or self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			self.VarPr()
			self.ExpressionPrPr()
		elif(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Args()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.SimpleExpression()
		else:
			if(self.debug):
				debugStatement ="in ExpressionPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ExpressionStatement(self):
		if(self.debug):
			print ("ExpressionStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="id"):
			self.Expression()
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		elif(self.currentToken.getType().strip()==";"):
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in ExpressionStatement at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def DeclarationListPr(self):
		if(self.debug):
			print ("DeclarationListPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="$"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
		else:
			if(self.debug):
				debugStatement ="in DeclarationListPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Param(self):
		if(self.debug):
			print ("Param: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.DataTypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.ParamPr()
		else:
			if(self.debug):
				debugStatement ="in Param at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Program(self):
		if(self.debug):
			print ("Program: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.DeclarationList()
		else:
			if(self.debug):
				debugStatement ="in Program at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Params(self):
		if(self.debug):
			print ("Params: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="void"):
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.ParamList()
		else:
			if(self.debug):
				debugStatement ="in Params at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Statement(self):
		if(self.debug):
			print ("Statement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="return"):
			self.ReturnStatement()
		elif(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id"):
			self.ExpressionStatement()
		elif(self.currentToken.getType().strip()=="{"):
			self.CmpdStatement()
		elif(self.currentToken.getType().strip()=="while"):
			self.IterationStatement()
		elif(self.currentToken.getType().strip()=="if"):
			self.SelectionStatement()
		else:
			if(self.debug):
				debugStatement ="in Statement at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Factor(self):
		if(self.debug):
			print ("Factor: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Expression()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="num"):
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.FactorPr()
		else:
			if(self.debug):
				debugStatement ="in Factor at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Var(self):
		if(self.debug):
			print ("Var: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.VarPr()
		else:
			if(self.debug):
				debugStatement ="in Var at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def DataTypeSpecifier(self):
		if(self.debug):
			print ("DataTypeSpecifier: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int"):
			if(self.currentToken.getType().strip()=="int"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="float"):
			if(self.currentToken.getType().strip()=="float"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in DataTypeSpecifier at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ArgsList(self):
		if(self.debug):
			print ("ArgsList: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()==","):
			self.ArgsListPr()
		elif(self.currentToken.getType().strip()=="id"):
			self.Expression()
		else:
			if(self.debug):
				debugStatement ="in ArgsList at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def TypeSpecifier(self):
		if(self.debug):
			print ("TypeSpecifier: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int"):
			if(self.currentToken.getType().strip()=="int"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="void"):
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="float"):
			if(self.currentToken.getType().strip()=="float"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in TypeSpecifier at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ParamListPr(self):
		if(self.debug):
			print ("ParamListPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
			self.Param()
			self.ParamListPr()
		else:
			if(self.debug):
				debugStatement ="in ParamListPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def CmpdStatement(self):
		if(self.debug):
			print ("CmpdStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="{"):
			if(self.currentToken.getType().strip()=="{"):
				self.nextToken()
			self.LocalDeclaration()
			self.StatementList()
			if(self.currentToken.getType().strip()=="}"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in CmpdStatement at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def VarDeclaration(self):
		if(self.debug):
			print ("VarDeclaration: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			self.VarDeclarationPr()
		else:
			if(self.debug):
				debugStatement ="in VarDeclaration at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ParamPr(self):
		if(self.debug):
			print ("ParamPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in ParamPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Args(self):
		if(self.debug):
			print ("Args: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()==","):
			self.ArgsList()
		else:
			if(self.debug):
				debugStatement ="in Args at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def MulOp(self):
		if(self.debug):
			print ("MulOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="*"):
			if(self.currentToken.getType().strip()=="*"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="/"):
			if(self.currentToken.getType().strip()=="/"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in MulOp at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Declaration(self):
		if(self.debug):
			print ("Declaration: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.DeclarationPr()
		else:
			if(self.debug):
				debugStatement ="in Declaration at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def SimpleExpression(self):
		if(self.debug):
			print ("SimpleExpression: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!="):
			self.TermPr()
			self.AddExpressionPr()
			self.RelOp()
			self.AddExpression()
		else:
			if(self.debug):
				debugStatement ="in SimpleExpression at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def SelectionStatement(self):
		if(self.debug):
			print ("SelectionStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="if"):
			if(self.currentToken.getType().strip()=="if"):
				self.nextToken()
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Expression()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.Statement()
			if(self.currentToken.getType().strip()=="SelectionStatementPr"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in SelectionStatement at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def AddOp(self):
		if(self.debug):
			print ("AddOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="+"):
			if(self.currentToken.getType().strip()=="+"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="-"):
			if(self.currentToken.getType().strip()=="-"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in AddOp at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Term(self):
		if(self.debug):
			print ("Term: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Factor()
			self.TermPr()
		else:
			if(self.debug):
				debugStatement ="in Term at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ArgsListPr(self):
		if(self.debug):
			print ("ArgsListPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
			self.Expression()
			self.ArgsListPr()
		else:
			if(self.debug):
				debugStatement ="in ArgsListPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ReturnStatementPr(self):
		if(self.debug):
			print ("ReturnStatementPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="id"):
			self.Expression()
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		elif(self.currentToken.getType().strip()==";"):
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in ReturnStatementPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def DeclarationPr(self):
		if(self.debug):
			print ("DeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Params()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.CmpdStatement()
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void" or self.currentToken.getType().strip()=="$"):
			return
		else:
			if(self.debug):
				debugStatement ="in DeclarationPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def StatementList(self):
		if(self.debug):
			print ("StatementList: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="}"):
			return
		elif(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			self.Statement()
			self.StatementList()
		else:
			if(self.debug):
				debugStatement ="in StatementList at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ParamList(self):
		if(self.debug):
			print ("ParamList: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.Param()
			self.ParamListPr()
		else:
			if(self.debug):
				debugStatement ="in ParamList at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def AddExpression(self):
		if(self.debug):
			print ("AddExpression: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Term()
			self.AddExpressionPr()
		else:
			if(self.debug):
				debugStatement ="in AddExpression at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Expression(self):
		if(self.debug):
			print ("Expression: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.ExpressionPr()
		else:
			if(self.debug):
				debugStatement ="in Expression at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def FunDeclaration(self):
		if(self.debug):
			print ("FunDeclaration: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Params()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.CmpdStatement()
		else:
			if(self.debug):
				debugStatement ="in FunDeclaration at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def RelOp(self):
		if(self.debug):
			print ("RelOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()==">="):
			if(self.currentToken.getType().strip()==">="):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="=="):
			if(self.currentToken.getType().strip()=="=="):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="<="):
			if(self.currentToken.getType().strip()=="<="):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="!="):
			if(self.currentToken.getType().strip()=="!="):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="<"):
			if(self.currentToken.getType().strip()=="<"):
				self.nextToken()
		elif(self.currentToken.getType().strip()==">"):
			if(self.currentToken.getType().strip()==">"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in RelOp at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def VarDeclarationPr(self):
		if(self.debug):
			print ("VarDeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in VarDeclarationPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ExpressionPrPr(self):
		if(self.debug):
			print ("ExpressionPrPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			self.SimpleExpression()
		elif(self.currentToken.getType().strip()=="="):
			if(self.currentToken.getType().strip()=="="):
				self.nextToken()
			self.Expression()
		else:
			if(self.debug):
				debugStatement ="in ExpressionPrPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def DeclarationList(self):
		if(self.debug):
			print ("DeclarationList: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
		else:
			if(self.debug):
				debugStatement ="in DeclarationList at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def LocalDeclaration(self):
		if(self.debug):
			print ("LocalDeclaration: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.VarDeclaration()
			self.LocalDeclaration()
		else:
			if(self.debug):
				debugStatement ="in LocalDeclaration at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def TermPr(self):
		if(self.debug):
			print ("TermPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/"):
			self.MulOp()
			self.Factor()
			self.TermPr()
		else:
			if(self.debug):
				debugStatement ="in TermPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def FactorPr(self):
		if(self.debug):
			print ("FactorPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="["):
			self.VarPr()
		elif(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Args()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in FactorPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def VarPr(self):
		if(self.debug):
			print ("VarPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="=" or self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			self.Expression()
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in VarPr at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def Call(self):
		if(self.debug):
			print ("Call: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Args()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
		else:
			if(self.debug):
				debugStatement ="in Call at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def ReturnStatement(self):
		if(self.debug):
			print ("ReturnStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="return"):
			if(self.currentToken.getType().strip()=="return"):
				self.nextToken()
			self.ReturnStatementPr()
		else:
			if(self.debug):
				debugStatement ="in ReturnStatement at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
	def IterationStatement(self):
		if(self.debug):
			print ("IterationStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
		if(self.currentToken.getType().strip()=="while"):
			if(self.currentToken.getType().strip()=="while"):
				self.nextToken()
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Expression()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.Statement()
		else:
			if(self.debug):
				debugStatement ="in IterationStatement at"+self.currentToken.getType()+str(self.currentTokenNumber)
			else:
				debugStatement =""
			print("REJECT "+debugStatement)

			sys.exit(-1)
