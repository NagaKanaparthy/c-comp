import sys
from to import Token
class cminus:
	def __init__(self, tokenList):
		tokenList.append(Token("$","$"))
		self.tokenList = tokenList
		self.currentTokenNumber = 0
		self.currentToken=tokenList[0]
		self.debug = True
		self.debugAccept = True
		self.debugStates = False
	def nextToken(self):
		if(self.currentTokenNumber < len(self.tokenList)):
			self.currentTokenNumber += 1
		self.currentToken = self.tokenList[self.currentTokenNumber]
	def AddExpression(self):
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Term()
			self.AddExpressionPr()
	def AddExpressionPr(self):
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/"):
			self.AddOp()
			self.Term()
			self.AddExpressionPr()
	def AddOp(self):
		if(self.currentToken.getType().strip()=="+"):
			if(self.currentToken.getType().strip()=="+"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="-"):
			if(self.currentToken.getType().strip()=="-"):
				self.nextToken()
	def Args(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()==","):
			self.ArgsList()
	def ArgsList(self):
		if(self.currentToken.getType().strip()==","):
			self.ArgsListPr()
		elif(self.currentToken.getType().strip()=="id"):
			self.Expression()
	def ArgsListPr(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
				self.Expression()
				self.ArgsListPr()
	def Call(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				if(self.currentToken.getType().strip()=="("):
					self.nextToken()
					self.Args()
					if(self.currentToken.getType().strip()==")"):
						self.nextToken()
	def CmpdStatement(self):
		if(self.currentToken.getType().strip()=="{"):
			if(self.currentToken.getType().strip()=="{"):
				self.nextToken()
				self.LocalDeclaration()
				self.StatementList()
				if(self.currentToken.getType().strip()=="}"):
					self.nextToken()
	def DataTypeSpecifier(self):
		if(self.currentToken.getType().strip()=="int"):
			if(self.currentToken.getType().strip()=="int"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="float"):
			if(self.currentToken.getType().strip()=="float"):
				self.nextToken()
	def Declaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				self.DeclarationPr()
	def DeclarationList(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
	def DeclarationListPr(self):
		if(self.currentToken.getType().strip()=="$"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.Declaration()
			self.DeclarationListPr()
	def DeclarationPr(self):
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
	def Expression(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				self.ExpressionPr()
	def ExpressionPr(self):
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
	def ExpressionPrPr(self):
		if(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			self.SimpleExpression()
		elif(self.currentToken.getType().strip()=="="):
			if(self.currentToken.getType().strip()=="="):
				self.nextToken()
				self.Expression()
	def ExpressionStatement(self):
		if(self.currentToken.getType().strip()=="id"):
			self.Expression()
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		elif(self.currentToken.getType().strip()==";"):
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
	def Factor(self):
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
	def FactorPr(self):
		if(self.currentToken.getType().strip()=="["):
			self.VarPr()
		elif(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
				self.Args()
				if(self.currentToken.getType().strip()==")"):
					self.nextToken()
	def FunDeclaration(self):
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
	def LocalDeclaration(self):
		if(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			return
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.VarDeclaration()
			self.LocalDeclaration()
	def MulOp(self):
		if(self.currentToken.getType().strip()=="*"):
			if(self.currentToken.getType().strip()=="*"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="/"):
			if(self.currentToken.getType().strip()=="/"):
				self.nextToken()
	def Param(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.DataTypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				self.ParamPr()
	def ParamList(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.Param()
			self.ParamListPr()
	def ParamListPr(self):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
				self.Param()
				self.ParamListPr()
	def ParamPr(self):
		if(self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
				if(self.currentToken.getType().strip()=="]"):
					self.nextToken()
	def Params(self):
		if(self.currentToken.getType().strip()=="void"):
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			self.ParamList()
	def Program(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.DeclarationList()
	def RelOp(self):
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
	def ReturnStatement(self):
		if(self.currentToken.getType().strip()=="return"):
			if(self.currentToken.getType().strip()=="return"):
				self.nextToken()
				self.ReturnStatementPr()
	def ReturnStatementPr(self):
		if(self.currentToken.getType().strip()=="id"):
			self.Expression()
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
		elif(self.currentToken.getType().strip()==";"):
			if(self.currentToken.getType().strip()==";"):
				self.nextToken()
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
	def SelectionStatementPr(self):
		if(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			return
		elif(self.currentToken.getType().strip()=="else"):
			if(self.currentToken.getType().strip()=="else"):
				self.nextToken()
				self.Statement()
	def SimpleExpression(self):
		if(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!="):
			self.TermPr()
			self.AddExpressionPr()
			self.RelOp()
			self.AddExpression()
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
	def StatementList(self):
		if(self.currentToken.getType().strip()=="}"):
			return
		elif(self.currentToken.getType().strip()==";" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="if" or self.currentToken.getType().strip()=="return" or self.currentToken.getType().strip()=="{" or self.currentToken.getType().strip()=="while"):
			self.Statement()
			self.StatementList()
	def Term(self):
		if(self.currentToken.getType().strip()=="(" or self.currentToken.getType().strip()=="id" or self.currentToken.getType().strip()=="num"):
			self.Factor()
			self.TermPr()
	def TermPr(self):
		if(self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/"):
			self.MulOp()
			self.Factor()
			self.TermPr()
	def TypeSpecifier(self):
		if(self.currentToken.getType().strip()=="int"):
			if(self.currentToken.getType().strip()=="int"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="void"):
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
		elif(self.currentToken.getType().strip()=="float"):
			if(self.currentToken.getType().strip()=="float"):
				self.nextToken()
	def Var(self):
		if(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.nextToken()
				self.VarPr()
	def VarDeclaration(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float" or self.currentToken.getType().strip()=="void"):
			self.TypeSpecifier()
			self.VarDeclarationPr()
	def VarDeclarationPr(self):
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
	def VarPr(self):
		if(self.currentToken.getType().strip()=="=" or self.currentToken.getType().strip()=="*" or self.currentToken.getType().strip()=="/" or self.currentToken.getType().strip()==">=" or self.currentToken.getType().strip()=="<=" or self.currentToken.getType().strip()==">" or self.currentToken.getType().strip()=="<" or self.currentToken.getType().strip()=="==" or self.currentToken.getType().strip()=="!=" or self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-" or self.currentToken.getType().strip()=="," or self.currentToken.getType().strip()==")" or self.currentToken.getType().strip()=="]" or self.currentToken.getType().strip()==";"):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
				self.Expression()
				if(self.currentToken.getType().strip()=="]"):
					self.nextToken()
