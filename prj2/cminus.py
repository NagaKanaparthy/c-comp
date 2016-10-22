import sys
from to import Token
class cminus:
	def __init__(self, tokenList):
		tokenList.append(Token("$","$"))
		self.tokenList = tokenList
		self.currentTokenNumber = 0
		self.currentToken=tokenList[0]
	def nextToken(self):
		if(self.currentTokenNumber < len(self.tokenList)):
			self.currentTokenNumber += 1
		self.currentToken = self.tokenList[self.currentTokenNumber]
	def AddExpressionPr(self):
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			self.AddOp()
			self.Term()
			self.AddExpressionPr()
		else:
			print("reject at AddExpressionPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ExpressionPr(self):
		if(self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()=="="):
			self.VarPr()
			if(self.currentToken.getType().strip()=="="):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ExpressionPr")
			self.Expression()
		elif(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			self.FactorPr()
			self.SimpleExpression()
		else:
			print("reject at ExpressionPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ExpressionStatement(self):
		if(self.currentToken.getType().strip()=="id"):
			self.Expression()
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ExpressionStatement")
		elif(self.currentToken.getType().strip()==";"):
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ExpressionStatement")
		else:
			print("reject at ExpressionStatement with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def DeclarationListPr(self):
		if(self.currentToken.getType().strip()=="$"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
		else:
			print("reject at DeclarationListPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Param(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.DataTypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Param")
			self.ParamPr()
		else:
			print("reject at Param with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Program(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.DeclarationList()
		else:
			print("reject at Program with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Params(self):
		if(self.currentToken.getType().strip()=="void"):
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Params")
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.ParamList()
		else:
			print("reject at Params with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Statement(self):
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
			print("reject at Statement with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Factor(self):
		if(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Factor")
			self.Expression()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Factor")
		elif(self.currentToken.getType().strip()=="num"):
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Factor")
		elif(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Factor")
			self.FactorPr()
		else:
			print("reject at Factor with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Var(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Var")
			self.VarPr()
		else:
			print("reject at Var with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def DataTypeSpecifier(self):
		if(self.currentToken.getType().strip()=="int"):
			if(self.currentToken.getType().strip()=="int"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" DataTypeSpecifier")
		elif(self.currentToken.getType().strip()=="float"):
			if(self.currentToken.getType().strip()=="float"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" DataTypeSpecifier")
		else:
			print("reject at DataTypeSpecifier with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ArgsList(self):
		if(self.currentToken.getType().strip()==","):
			self.ArgsListPr()
		elif(self.currentToken.getType().strip()=="id"):
			self.Expression()
		else:
			print("reject at ArgsList with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def TypeSpecifier(self):
		if(self.currentToken.getType().strip()=="int"):
			if(self.currentToken.getType().strip()=="int"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" TypeSpecifier")
		elif(self.currentToken.getType().strip()=="void"):
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" TypeSpecifier")
		elif(self.currentToken.getType().strip()=="float"):
			if(self.currentToken.getType().strip()=="float"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" TypeSpecifier")
		else:
			print("reject at TypeSpecifier with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ParamListPr(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ParamListPr")
			self.Param()
			self.ParamListPr()
		else:
			print("reject at ParamListPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def CmpdStatement(self):
		if(self.currentToken.getType().strip()=="{"):
			if(self.currentToken.getType().strip()=="{"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" CmpdStatement")
			self.LocalDeclaration()
			self.StatementList()
			if(self.currentToken.getType().strip()=="}"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" CmpdStatement")
		else:
			print("reject at CmpdStatement with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def VarDeclaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			self.VarDeclarationPr()
		else:
			print("reject at VarDeclaration with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ParamPr(self):
		if(self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ParamPr")
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ParamPr")
		else:
			print("reject at ParamPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Args(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()==","):
			self.ArgsList()
		else:
			print("reject at Args with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def MulOp(self):
		if(self.currentToken.getType().strip()=="*"):
			if(self.currentToken.getType().strip()=="*"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" MulOp")
		elif(self.currentToken.getType().strip()=="/"):
			if(self.currentToken.getType().strip()=="/"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" MulOp")
		else:
			print("reject at MulOp with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Declaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Declaration")
			self.DeclarationPr()
		else:
			print("reject at Declaration with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def SimpleExpression(self):
		if(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!="):
			self.TermPr()
			self.AddExpressionPr()
			self.RelOp()
			self.AddExpression()
		else:
			print("reject at SimpleExpression with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def SelectionStatementPr(self):
		if(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while" or self.currentToken.getType().strip()=="}"):
			return
		elif(self.currentToken.getType().strip()=="else"):
			if(self.currentToken.getType().strip()=="else"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" SelectionStatementPr")
			self.Statement()
		else:
			print("reject at SelectionStatementPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def SelectionStatement(self):
		if(self.currentToken.getType().strip()=="if"):
			if(self.currentToken.getType().strip()=="if"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" SelectionStatement")
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" SelectionStatement")
			self.Expression()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" SelectionStatement")
			self.Statement()
			self.SelectionStatementPr()
		else:
			print("reject at SelectionStatement with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def AddOp(self):
		if(self.currentToken.getType().strip()=="+"):
			if(self.currentToken.getType().strip()=="+"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" AddOp")
		elif(self.currentToken.getType().strip()=="-"):
			if(self.currentToken.getType().strip()=="-"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" AddOp")
		else:
			print("reject at AddOp with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Term(self):
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Factor()
			self.TermPr()
		else:
			print("reject at Term with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ArgsListPr(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ArgsListPr")
			self.Expression()
			self.ArgsListPr()
		else:
			print("reject at ArgsListPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ReturnStatementPr(self):
		if(self.currentToken.getType().strip()=="id"):
			self.Expression()
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ReturnStatementPr")
		elif(self.currentToken.getType().strip()==";"):
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ReturnStatementPr")
		else:
			print("reject at ReturnStatementPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def FactorPr(self):
		if(self.currentToken.getType().strip()=="[" or self.currentToken.getType().strip()=="=" or self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()==";"):
			self.VarPr()
		elif(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" FactorPr")
			self.Args()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" FactorPr")
		else:
			print("reject at FactorPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def StatementList(self):
		if(self.currentToken.getType().strip()=="}"):
			return
		elif(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			self.Statement()
			self.StatementList()
		else:
			print("reject at StatementList with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ParamList(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.Param()
			self.ParamListPr()
		else:
			print("reject at ParamList with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def AddExpression(self):
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Term()
			self.AddExpressionPr()
		else:
			print("reject at AddExpression with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Expression(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Expression")
			self.ExpressionPr()
		else:
			print("reject at Expression with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def FunDeclaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" FunDeclaration")
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" FunDeclaration")
			self.Params()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" FunDeclaration")
			self.CmpdStatement()
		else:
			print("reject at FunDeclaration with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def RelOp(self):
		if(self.currentToken.getType().strip()==">="):
			if(self.currentToken.getType().strip()==">="):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" RelOp")
		elif(self.currentToken.getType().strip()=="=="):
			if(self.currentToken.getType().strip()=="=="):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" RelOp")
		elif(self.currentToken.getType().strip()=="<="):
			if(self.currentToken.getType().strip()=="<="):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" RelOp")
		elif(self.currentToken.getType().strip()=="!="):
			if(self.currentToken.getType().strip()=="!="):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" RelOp")
		elif(self.currentToken.getType().strip()=="<"):
			if(self.currentToken.getType().strip()=="<"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" RelOp")
		elif(self.currentToken.getType().strip()==">"):
			if(self.currentToken.getType().strip()==">"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" RelOp")
		else:
			print("reject at RelOp with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def VarDeclarationPr(self):
		if(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" VarDeclarationPr")
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" VarDeclarationPr")
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" VarDeclarationPr")
		elif(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" VarDeclarationPr")
		else:
			print("reject at VarDeclarationPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def DeclarationList(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
		else:
			print("reject at DeclarationList with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def LocalDeclaration(self):
		if(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.VarDeclaration()
			self.LocalDeclaration()
		else:
			print("reject at LocalDeclaration with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def TermPr(self):
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/"):
			self.MulOp()
			self.Factor()
			self.TermPr()
		else:
			print("reject at TermPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def DeclarationPr(self):
		if(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" DeclarationPr")
			self.Params()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" DeclarationPr")
			self.CmpdStatement()
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" DeclarationPr")
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" DeclarationPr")
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" DeclarationPr")
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void" or self.currentToken.getType().strip()=="$"):
			return
		else:
			print("reject at DeclarationPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def VarPr(self):
		if(self.currentToken.getType().strip()=="=" or self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" VarPr")
			self.Expression()
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" VarPr")
		else:
			print("reject at VarPr with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def Call(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Call")
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Call")
			self.Args()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" Call")
		else:
			print("reject at Call with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def ReturnStatement(self):
		if(self.currentToken.getType().strip()=="return"):
			if(self.currentToken.getType().strip()=="return"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" ReturnStatement")
			self.ReturnStatementPr()
		else:
			print("reject at ReturnStatement with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
	def IterationStatement(self):
		if(self.currentToken.getType().strip()=="while"):
			if(self.currentToken.getType().strip()=="while"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" IterationStatement")
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" IterationStatement")
			self.Expression()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			else: print("error "+self.currentToken.getValue().strip()+" IterationStatement")
			self.Statement()
		else:
			print("reject at IterationStatement with token :"+self.currentToken.getType()+str(self.currentTokenNumber))
			sys.exit(0)
