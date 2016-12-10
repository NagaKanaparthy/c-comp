import sys
from to import Token
class cminus:
	def __init__(self, tokenList):
		tokenList.append(Token("$","$"))
		self.tokenList = tokenList
		self.currentTokenNumber = 0
		self.currentToken=tokenList[0]
		self.debug = True
		self.debugReject = True
	def nextToken(self):
		if(self.currentTokenNumber < len(self.tokenList)):
			self.currentTokenNumber += 1
		self.currentToken = self.tokenList[self.currentTokenNumber]
	def Reject(self, stateName):
		if(self.debugReject):
			print("REJECT with token #"+str(self.currentTokenNumber)+":"+self.currentToken.getValue()+" @"+stateName+"\n")
		else:
			print("REJECT")
		sys.exit(1)
#	Return Only Methods No Consumption
	def TypeSpecifier(self):
		if(self.currentToken.getType().strip()=="int"):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="void"):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="float"):
			return self.nextToken()
		else:
			self.Reject("TypeSpecifier")
	def DataTypeSpecifier(self):
		if(self.currentToken.getType().strip()=="int"):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="float"):
			return self.nextToken()
		else:
			self.Reject("DataTypeSpecifier")
	def RelOp(self):
		if(self.currentToken.getType().strip()==">="):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="=="):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="<="):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="!="):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="<"):
			return self.nextToken()
		elif(self.currentToken.getType().strip()==">"):
			return self.nextToken()
		else:
			self.Reject("RelOp")
	def MulOp(self):
		if(self.currentToken.getType().strip()=="*"):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="/"):
			return self.nextToken()
		else:
			self.Reject("MulOp")
	def AddOp(self):
		if(self.currentToken.getType().strip()=="+"):
			return self.nextToken()
		elif(self.currentToken.getType().strip()=="-"):
			return self.nextToken()
		else:
			self.Reject("AddOp")
#	Logic methods
	def Program(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.DeclarationList()
		else:
			self.Reject("Program")
	def DeclarationList(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
		else:
			self.Reject("DeclarationList")
	def DeclarationListPr(self):
		if(self.currentToken.getType().strip()=="$"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
		else:
			self.Reject("DeclarationListPr")
	def Declaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			self.DeclarationPr()
		else:
			self.Reject("Declaration")
	def DeclarationPr(self):
		if(self.currentToken.getType().strip()=="id"):
			self.nextToken()
			self.DeclarationPrPr()
		else:
			self.Reject("DeclarationPr")
	def DeclarationPrPr(self):
		if(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
				self.Params()
				if(self.currentToken.getType().strip()==")"):
					self.nextToken()
					self.CmpdStatement()
				else:
					self.Reject("DeclarationPrPr")
			else:
				self.Reject("DeclarationPr")
		elif(self.currentToken.getType().strip()=="[" or self.currentToken.getType().strip()==";"):
			self.VarDeclaration()
		else:
			self.Reject("DeclarationPr")
	def VarDeclaration(self):
		if(self.currentToken.getType().strip()==";"):
			self.nextToken()
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
				if(self.currentToken.getType().strip()=="num"):
					self.nextToken()
					if(self.currentToken.getType().strip()=="]"):
						self.nextToken()
						if(self.currentToken.getType().strip()==";"):
							self.nextToken()
						else:
							self.Reject("VarDeclaration")
					else:
						self.Reject("VarDeclaration")
				else:
					self.Reject("VarDeclaration")
			else:
				self.Reject("VarDeclaration")
		else:
			self.Reject("VarDeclaration")
	def Params(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.DataTypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				self.ParamPr()
				self.ParamList()
			else:
				self.Reject("Params")
		elif(self.currentToken.getType().strip()=="void"):
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
				self.ParamList()
			else:
				self.Reject("Params")
		else:
			self.Reject("Params")
	def ParamList(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
				self.Param()
				self.ParamList()
			else:
				self.Reject("ParamList")
		else:
			self.Reject("ParamList")
	def Param(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.DataTypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				self.ParamPr()
			else:
				self.Reject("Param")
		else:
			self.Reject("Param")
	def ParamPr(self):
		if(self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
				if(self.currentToken.getType().strip()=="]"):
					self.nextToken()
				else:
					self.Reject("ParamPr")
			else:
				self.Reject("ParamPr")
		else:
			self.Reject("ParamPr")
	def CmpdStatement(self):
		if(self.currentToken.getType().strip()=="{"):
			if(self.currentToken.getType().strip()=="{"):
				self.nextToken()
				self.LocalDeclaration()
				self.StatementList()
				if(self.currentToken.getType().strip()=="}"):
					self.nextToken()
				else:
					self.Reject("CmpdStatement")
			else:
				self.Reject("CmpdStatement")
		else:
			self.Reject("CmpdStatement")
	def LocalDeclaration(self):
		if(self.currentToken.getType().strip() in ["(","id","num","return","if","while",";", "}","{"]):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			self.DeclarationPr()
			self.LocalDeclaration()
		else:
			self.Reject("LocalDeclaration")

	def Statement(self):
		if(self.currentToken.getType().strip()=="return"):
			self.ReturnStatement()
		elif(self.currentToken.getType().strip() in ["(","id","num",";"]):
			self.ExpressionStatement()
		elif(self.currentToken.getType().strip()=="{"):
			self.CmpdStatement()
		elif(self.currentToken.getType().strip()=="while"):
			self.IterationStatement()
		elif(self.currentToken.getType().strip()=="if"):
			self.SelectionStatement()
		else:
			self.Reject("Statement")
	def StatementList(self):
		if(self.currentToken.getType().strip()=="}"):
			return
		elif(self.currentToken.getType().strip() in ["(","id","num","return","if","while",";","{","("]):
			self.Statement()
			self.StatementList()
		else:
			self.Reject("StatementList")
	def ExpressionStatement(self):
		if(self.currentToken.getType().strip() in ["(", "num", "id"]):
			self.Expression()
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
			else:
				self.Reject("ExpressionStatement")
		elif(self.currentToken.getType().strip()==";"):
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
			else:
				self.Reject("ExpressionStatement")
		else:
			self.Reject("ExpressionStatement")
	def SelectionStatement(self):
		if(self.currentToken.getType().strip()=="if"):
			if(self.currentToken.getType().strip()=="if"):
				self.nextToken()
				if(self.currentToken.getType().strip()=="("):
					self.nextToken()
					self.Expression()
					if(self.currentToken.getType().strip()==")"):
						self.nextToken()
						self.Statement()
						self.SelectionStatementPr()						
					else:
						self.Reject("SelectionStatement")
				else:
					self.Reject("SelectionStatement")
			else:
				self.Reject("SelectionStatement")
		else:
			self.Reject("SelectionStatement")
	def SelectionStatementPr(self):
		if(self.currentToken.getType().strip()=="else"):
			if(self.currentToken.getType().strip()=="else"):
				self.nextToken()
				self.Statement()
			else:
				self.Reject("SelectionStatementPr")
		elif(self.currentToken.getType().strip() in ["num","id","return","while","if","(","{", ";","}"]):
			return
		else:
			self.Reject("SelectionStatementPr")
	def IterationStatement(self):
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
						self.Reject("IterationStatement")
				else:
					self.Reject("IterationStatement")
			else:
				self.Reject("IterationStatement")
		else:
			self.Reject("IterationStatement")
	def ReturnStatement(self):
		if(self.currentToken.getType().strip()=="return"):
			self.nextToken()
			self.ReturnStatementPr()
		else:
			self.Reject("ReturnStatement")
	def ReturnStatementPr(self):
		if(self.currentToken.getType().strip() in ["(", "num", "id"]):
			self.Expression()
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
			else:
				self.Reject("ReturnStatementPr")
		elif(self.currentToken.getType().strip()==";"):
			self.nextToken()
		else:
			self.Reject("ReturnStatementPr")
	def Expression(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.DataTypeSpecifier()
			self.AddExpression()
			self.SimpleExpression()
		elif(self.currentToken.getType().strip()=="("):
			self.nextToken()
			self.Expression()
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
				self.TermPr()
				self.AddExpression()
				self.SimpleExpression()
			else:
				self.Reject("Expression")
		elif(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				self.ExpressionPr()
			else:
				self.Reject("Expression")
		elif(self.currentToken.getType().strip()=="num"):
			self.nextToken()
			self.TermPr()
			self.AddExpression()
			self.SimpleExpression()
		else:
			self.Reject("Expression")
	def ExpressionPr(self):
		if(self.currentToken.getType().strip() in ["<=",">=","==","!=","<",">","+","*","-","/","=",")",";","[","]",","]):
			self.VarPr()
			self.ExpressionPrPr()
		elif(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
				self.Args()
				if(self.currentToken.getType().strip()==")"):
					self.nextToken()
					self.TermPr()
					self.AddExpression()
					self.SimpleExpression()
				else:
					self.Reject("ExpressionPr )")
			else:
				self.Reject("ExpressionPr (")
		else:
			self.Reject("ExpressionPr")
	def ExpressionPrPr(self):
		if(self.currentToken.getType().strip() in ["<=",">=","==","!=","<",">","+","*","-","/",")",";","]",","]):
			self.TermPr()
			self.AddExpression()
			self.SimpleExpression()
		elif(self.currentToken.getType().strip()=="="):
			self.nextToken()
			self.Expression()
		else:
			self.Reject("ExpressionPrPr")
	def VarPr(self):
		if(self.currentToken.getType().strip() in ["<=",">=","==","!=","<",">","*","/","+","-","=",")",";","]",","]):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
				self.Expression()
				if(self.currentToken.getType().strip()=="]"):
					self.nextToken()
				else:
					self.Reject("VarPr")
			else:
				self.Reject("VarPr")
		else:
			self.Reject("VarPr")
	def SimpleExpression(self):
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!="):
			self.RelOp()
			self.Term()
			self.AddExpression()
		elif(self.currentToken.getType().strip() in [")", ";", "]", ","]):
			return
		else:
			self.Reject("SimpleExpression")
	def AddExpression(self):
		if(self.currentToken.getType().strip() in ["<=",">=","==","!=","<",">",")",";","]",","]):
			return
		elif(self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			self.AddOp()
			self.Term()
			self.AddExpression()
		else:
			self.Reject("AddExpression")
	def Term(self):
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Factor()
			self.TermPr()
		else:
			self.Reject("Term")
	def TermPr(self):
		if(self.currentToken.getType().strip() in ["<=",">=","==","!=","<",">","+","-","=",")",";","]",","]):
			return
		elif(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/"):
			self.MulOp()
			self.Factor()
			self.TermPr()
		else:
			self.Reject("TermPr")
	def Factor(self):
		if(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
				self.Expression()
				if(self.currentToken.getType().strip()==")"):
					self.nextToken()
				else:
					self.Reject("Factor")
			else:
				self.Reject("Factor")
		elif(self.currentToken.getType().strip()=="num"):
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
			else:
				self.Reject("Factor")
		elif(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				self.FactorPr()
			else:
				self.Reject("Factor")
		else:
			self.Reject("Factor")
	def FactorPr(self):
		if(self.currentToken.getType().strip() in ["<=",">=","==","!=","<",">","+","*","-","/",")",";","[","]",","]):
			self.VarPr()
		elif(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
				self.Args()
				if(self.currentToken.getType().strip()==")"):
					self.nextToken()
				else:
					self.Reject("FactorPr")
			else:
				self.Reject("FactorPr")
		else:
			self.Reject("FactorPr")			
	def Args(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()in ["(", "num", "id"]):
			self.ArgsList()
		else:
			self.Reject("Args")
	def ArgsList(self):
		if(self.currentToken.getType().strip() in ["(", "num", "id"]):
			self.Expression()
			self.ArgsListPr()
		else:
			self.Reject("ArgsList")
	def ArgsListPr(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
				self.Expression()
				self.ArgsListPr()

			else:
				self.Reject("ArgsListPr")
		else:
			self.Reject("ArgsListPr")