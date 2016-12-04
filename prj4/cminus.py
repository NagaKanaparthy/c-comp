import sys
from to import Token
class cminus:
	def __init__(self, tokenList):
		tokenList.append(Token("$","$"))
		self.tokenList = tokenList
		self.currentTokenNumber = 0
		self.currentToken=tokenList[0]
		self.debug = True
		self.debugStates = False
	def nextToken(self):
		if(self.currentTokenNumber < len(self.tokenList)):
			self.currentTokenNumber += 1
		self.currentToken = self.tokenList[self.currentTokenNumber]
	def AddExpression(self):
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Term()
			self.AddExpressionPr()
		else:
			if(self.debug):
				print("REJECT@ AddExpression with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def AddExpressionPr(self):
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/"):
			self.AddOp()
			self.Term()
			self.AddExpressionPr()
		else:
			if(self.debug):
				print("REJECT@ AddExpressionPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def AddOp(self):
		if(self.currentToken.getType().strip()=="+"):
			if(self.debugStates):
				print ("AddOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="+"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="-"):
			if(self.debugStates):
				print ("AddOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="-"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ AddOp with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Args(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()==","):
			self.ArgsList()
		else:
			if(self.debug):
				print("REJECT@ Args with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ArgsList(self):
		if(self.currentToken.getType().strip()==","):
			self.ArgsListPr()
		elif(self.currentToken.getType().strip()=="id"):
			self.Expression()
		else:
			if(self.debug):
				print("REJECT@ ArgsList with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ArgsListPr(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.debugStates):
				print ("ArgsListPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
			self.Expression()
			self.ArgsListPr()
		else:
			if(self.debug):
				print("REJECT@ ArgsListPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Call(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.debugStates):
				print ("Call: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			if(self.debugStates):
				print ("Call: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Args()
			if(self.debugStates):
				print ("Call: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ Call with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def CmpdStatement(self):
		if(self.currentToken.getType().strip()=="{"):
			if(self.debugStates):
				print ("CmpdStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="{"):
				self.nextToken()
			self.LocalDeclaration()
			self.StatementList()
			if(self.debugStates):
				print ("CmpdStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="}"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ CmpdStatement with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def DataTypeSpecifier(self):
		if(self.currentToken.getType().strip()=="int"):
			if(self.debugStates):
				print ("DataTypeSpecifier: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="int"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="float"):
			if(self.debugStates):
				print ("DataTypeSpecifier: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="float"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ DataTypeSpecifier with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Declaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):    
			if(self.debugStates):
				print ("Declaration: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			self.nextToken()
			self.DeclarationPr()
		else:
			if(self.debug):
				print("REJECT@ Declaration with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def DeclarationList(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
		else:
			if(self.debug):
				print("REJECT@ DeclarationList with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def DeclarationListPr(self):
		if(self.currentToken.getType().strip()=="$"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
		else:
			if(self.debug):
				print("REJECT@ DeclarationListPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def DeclarationPr(self):
		if(self.currentToken.getType().strip()=="("):
			if(self.debugStates):
				print ("DeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
				self.Params()
				if(self.debugStates):
					print ("DeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
					if(self.currentToken.getType().strip()==")"):
						self.nextToken()
					self.CmpdStatement()
		elif(self.currentToken.getType().strip()=="["):
			if(self.debugStates):
				print ("DeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
				if(self.debugStates):
					print ("DeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
				if(self.currentToken.getType().strip()=="num"):
					self.nextToken()
					if(self.debugStates):
						print ("DeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
					if(self.currentToken.getType().strip()=="]"):
						self.nextToken()
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void" or self.currentToken.getType().strip()=="$"):
			return
		else:
			if(self.debug):
				print("REJECT@ DeclarationPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Expression(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.debugStates):
				print ("Expression: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.ExpressionPr()
		else:
			if(self.debug):
				print("REJECT@ Expression with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ExpressionPr(self):
		if(self.currentToken.getType().strip()=="[" or self.currentToken.getType().strip()=="=" or self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			self.VarPr()
			self.ExpressionPrPr()
		elif(self.currentToken.getType().strip()=="("):
			if(self.debugStates):
				print ("ExpressionPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Args()
			if(self.debugStates):
				print ("ExpressionPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.SimpleExpression()
		else:
			if(self.debug):
				print("REJECT@ ExpressionPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ExpressionPrPr(self):
		if(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			self.SimpleExpression()
		elif(self.currentToken.getType().strip()=="="):
			if(self.debugStates):
				print ("ExpressionPrPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="="):
				self.nextToken()
			self.Expression()
		else:
			if(self.debug):
				print("REJECT@ ExpressionPrPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ExpressionStatement(self):
		if(self.currentToken.getType().strip()=="id"):
			self.Expression()
			if(self.debugStates):
				print ("ExpressionStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		elif(self.currentToken.getType().strip()==";"):
			if(self.debugStates):
				print ("ExpressionStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ ExpressionStatement with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Factor(self):
		if(self.currentToken.getType().strip()=="("):
			if(self.debugStates):
				print ("Factor: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Expression()
			if(self.debugStates):
				print ("Factor: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="num"):
			if(self.debugStates):
				print ("Factor: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="id"):
			if(self.debugStates):
				print ("Factor: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.FactorPr()
		else:
			if(self.debug):
				print("REJECT@ Factor with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def FactorPr(self):
		if(self.currentToken.getType().strip()=="["):
			self.VarPr()
		elif(self.currentToken.getType().strip()=="("):
			if(self.debugStates):
				print ("FactorPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Args()
			if(self.debugStates):
				print ("FactorPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ FactorPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def FunDeclaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			if(self.debugStates):
				print ("FunDeclaration: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			if(self.debugStates):
				print ("FunDeclaration: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Params()
			if(self.debugStates):
				print ("FunDeclaration: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.CmpdStatement()
		else:
			if(self.debug):
				print("REJECT@ FunDeclaration with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def IterationStatement(self):
		if(self.currentToken.getType().strip()=="while"):
			if(self.debugStates):
				print ("IterationStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="while"):
				self.nextToken()
			if(self.debugStates):
				print ("IterationStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Expression()
			if(self.debugStates):
				print ("IterationStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.Statement()
		else:
			if(self.debug):
				print("REJECT@ IterationStatement with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def LocalDeclaration(self):
		if(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.VarDeclaration()
			self.LocalDeclaration()
		else:
			if(self.debug):
				print("REJECT@ LocalDeclaration with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def MulOp(self):
		if(self.currentToken.getType().strip()=="*"):
			if(self.debugStates):
				print ("MulOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="*"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="/"):
			if(self.debugStates):
				print ("MulOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="/"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ MulOp with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Param(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.DataTypeSpecifier()
			if(self.debugStates):
				print ("Param: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.ParamPr()
		else:
			if(self.debug):
				print("REJECT@ Param with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ParamList(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.Param()
			self.ParamListPr()
		else:
			if(self.debug):
				print("REJECT@ ParamList with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ParamListPr(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.debugStates):
				print ("ParamListPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
			self.Param()
			self.ParamListPr()
		else:
			if(self.debug):
				print("REJECT@ ParamListPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ParamPr(self):
		if(self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.debugStates):
				print ("ParamPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			if(self.debugStates):
				print ("ParamPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ ParamPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Params(self):
		if(self.currentToken.getType().strip()=="void"):
			if(self.debugStates):
				print ("Params: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.ParamList()
		else:
			if(self.debug):
				print("REJECT@ Params with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Program(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.DeclarationList()
		else:
			if(self.debug):
				print("REJECT@ Program with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def RelOp(self):
		if(self.currentToken.getType().strip()==">="):
			if(self.debugStates):
				print ("RelOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==">="):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="=="):
			if(self.debugStates):
				print ("RelOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="=="):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="<="):
			if(self.debugStates):
				print ("RelOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="<="):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="!="):
			if(self.debugStates):
				print ("RelOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="!="):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="<"):
			if(self.debugStates):
				print ("RelOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="<"):
				self.nextToken()
		elif(self.currentToken.getType().strip()==">"):
			if(self.debugStates):
				print ("RelOp: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==">"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ RelOp with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ReturnStatement(self):
		if(self.currentToken.getType().strip()=="return"):
			if(self.debugStates):
				print ("ReturnStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="return"):
				self.nextToken()
			self.ReturnStatementPr()
		else:
			if(self.debug):
				print("REJECT@ ReturnStatement with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def ReturnStatementPr(self):
		if(self.currentToken.getType().strip()=="id"):
			self.Expression()
			if(self.debugStates):
				print ("ReturnStatementPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		elif(self.currentToken.getType().strip()==";"):
			if(self.debugStates):
				print ("ReturnStatementPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ ReturnStatementPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def SelectionStatement(self):
		if(self.currentToken.getType().strip()=="if"):
			if(self.debugStates):
				print ("SelectionStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="if"):
				self.nextToken()
			if(self.debugStates):
				print ("SelectionStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
			self.Expression()
			if(self.debugStates):
				print ("SelectionStatement: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()==")"):
				self.nextToken()
			self.Statement()
			self.SelectionStatementPr()
		else:
			if(self.debug):
				print("REJECT@ SelectionStatement with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def SelectionStatementPr(self):
		if(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			return
		elif(self.currentToken.getType().strip()=="else"):
			if(self.debugStates):
				print ("SelectionStatementPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="else"):
				self.nextToken()
			self.Statement()
		else:
			if(self.debug):
				print("REJECT@ SelectionStatementPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def SimpleExpression(self):
		if(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!="):
			self.TermPr()
			self.AddExpressionPr()
			self.RelOp()
			self.AddExpression()
		else:
			if(self.debug):
				print("REJECT@ SimpleExpression with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
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
			if(self.debug):
				print("REJECT@ Statement with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def StatementList(self):
		if(self.currentToken.getType().strip()=="}"):
			return
		elif(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			self.Statement()
			self.StatementList()
		else:
			if(self.debug):
				print("REJECT@ StatementList with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Term(self):
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Factor()
			self.TermPr()
		else:
			if(self.debug):
				print("REJECT@ Term with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def TermPr(self):
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/"):
			self.MulOp()
			self.Factor()
			self.TermPr()
		else:
			if(self.debug):
				print("REJECT@ TermPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def TypeSpecifier(self):
		if(self.currentToken.getType().strip()=="int"):
			if(self.debugStates):
				print ("TypeSpecifier: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="int"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="void"):
			if(self.debugStates):
				print ("TypeSpecifier: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="float"):
			if(self.debugStates):
				print ("TypeSpecifier: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="float"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ TypeSpecifier with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def Var(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.debugStates):
				print ("Var: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
			self.VarPr()
		else:
			if(self.debug):
				print("REJECT@ Var with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def VarDeclaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			self.VarDeclarationPr()
		else:
			if(self.debug):
				print("REJECT@ VarDeclaration with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def VarDeclarationPr(self):
		if(self.currentToken.getType().strip()=="["):
			if(self.debugStates):
				print ("VarDeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			if(self.debugStates):
				print ("VarDeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="num"):
				self.nextToken()
			if(self.debugStates):
				print ("VarDeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="id"):
			if(self.debugStates):
				print ("VarDeclarationPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ VarDeclarationPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
	def VarPr(self):
		if(self.currentToken.getType().strip()=="=" or self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.debugStates):
				print ("VarPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
			self.Expression()
			if(self.debugStates):
				print ("VarPr: "+self.currentToken.getType()+" | "+self.currentToken.getValue())
			if(self.currentToken.getType().strip()=="]"):
				self.nextToken()
		else:
			if(self.debug):
				print("REJECT@ VarPr with "+self.currentToken.getType()+"|"+str(self.currentTokenNumber))
