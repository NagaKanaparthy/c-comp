import sys
from token import Token
from rule import RuleDictionary
class cminus.py
	def __init__(self, tokenList):
		tokenList.append(Token("$","$"))
		self.tokenList = tokenList
	def AddExpressionPr(self):
		if(self.currentToken==">=" or self.currentToken=="<=" or self.currentToken==">" or self.currentToken=="<" or self.currentToken=="==" or self.currentToken=="!="):

			return
		elif(self.currentToken=="+" or self.currentToken=="-"):


			self.AddOp()


			self.Term()


			self.AddExpressionPr()

		else:
			print("reject")
			sys.exit(0)
	def ExpressionPr(self):
		if(self.currentToken=="," or self.currentToken=="="):


			self.VarPr()

			if(self.currentToken.getType()=="=")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Expression()

		elif(self.currentToken=="(" or self.currentToken=="*" or self.currentToken=="/" or self.currentToken==">=" or self.currentToken=="<=" or self.currentToken==">" or self.currentToken=="<" or self.currentToken=="==" or self.currentToken=="!=" or self.currentToken=="+" or self.currentToken=="-"):


			self.FactorPr()


			self.SimpleExpression()

		else:
			print("reject")
			sys.exit(0)
	def ExpressionStatement(self):
		if(self.currentToken=="id"):


			self.Expression()

			if(self.currentToken.getType()==";")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken==";"):

			if(self.currentToken.getType()==";")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def DeclarationListPr(self):
		if(self.currentToken=="$"):

			return
		elif(self.currentToken=="int" or self.currentToken=="float" or self.currentToken=="void"):


			self.Declaration()


			self.DeclarationListPr()

		else:
			print("reject")
			sys.exit(0)
	def Param(self):
		if(self.currentToken=="int" or self.currentToken=="float"):


			self.DataTypeSpecifier()

			if(self.currentToken.getType()=="id")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.ParamPr()

		else:
			print("reject")
			sys.exit(0)
	def Program(self):
		if(self.currentToken=="int" or self.currentToken=="float" or self.currentToken=="void"):


			self.DeclarationList()

		else:
			print("reject")
			sys.exit(0)
	def Params(self):
		if(self.currentToken=="void"):

			if(self.currentToken.getType()=="void")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="int" or self.currentToken=="float"):


			self.ParamList()

		else:
			print("reject")
			sys.exit(0)
	def Statement(self):
		if(self.currentToken=="return"):


			self.ReturnStatement()

		elif(self.currentToken==";" or self.currentToken=="id"):


			self.ExpressionStatement()

		elif(self.currentToken=="{"):


			self.CmpdStatement()

		elif(self.currentToken=="while"):


			self.IterationStatement()

		elif(self.currentToken=="if"):


			self.SelectionStatement()

		else:
			print("reject")
			sys.exit(0)
	def Factor(self):
		if(self.currentToken=="("):

			if(self.currentToken.getType()=="(")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Expression()

			if(self.currentToken.getType()==")")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="num"):

			if(self.currentToken.getType()=="num")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="id"):

			if(self.currentToken.getType()=="id")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.FactorPr()

		else:
			print("reject")
			sys.exit(0)
	def Var(self):
		if(self.currentToken=="id"):

			if(self.currentToken.getType()=="id")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.VarPr()

		else:
			print("reject")
			sys.exit(0)
	def DataTypeSpecifier(self):
		if(self.currentToken=="int"):

			if(self.currentToken.getType()=="int")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="float"):

			if(self.currentToken.getType()=="float")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def ArgsList(self):
		if(self.currentToken==","):


			self.ArgsListPr()

		elif(self.currentToken=="id"):


			self.Expression()

		else:
			print("reject")
			sys.exit(0)
	def TypeSpecifier(self):
		if(self.currentToken=="int"):

			if(self.currentToken.getType()=="int")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="void"):

			if(self.currentToken.getType()=="void")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="float"):

			if(self.currentToken.getType()=="float")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def ParamListPr(self):
		if(self.currentToken==","):


			self.Param()


			self.ParamListPr()

		elif(self.currentToken==")"):

			return
		else:
			print("reject")
			sys.exit(0)
	def CmpdStatement(self):
		if(self.currentToken=="{"):

			if(self.currentToken.getType()=="{")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.LocalDeclaration()


			self.StatementList()

			if(self.currentToken.getType()=="}")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def VarDeclaration(self):
		if(self.currentToken=="int" or self.currentToken=="float" or self.currentToken=="void"):


			self.TypeSpecifier()


			self.VarDeclarationPr()

		else:
			print("reject")
			sys.exit(0)
	def ParamPr(self):
		if(self.currentToken=="," or self.currentToken==")"):

			return
		elif(self.currentToken=="["):

			if(self.currentToken.getType()=="[")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="]")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def Args(self):
		if(self.currentToken==")"):

			return
		elif(self.currentToken=="id" or self.currentToken==","):


			self.ArgsList()

		else:
			print("reject")
			sys.exit(0)
	def MulOp(self):
		if(self.currentToken=="*"):

			if(self.currentToken.getType()=="*")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="/"):

			if(self.currentToken.getType()=="/")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def Declaration(self):
		if(self.currentToken=="int" or self.currentToken=="float" or self.currentToken=="void"):


			self.TypeSpecifier()

			if(self.currentToken.getType()=="id")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.DeclarationPr()

		else:
			print("reject")
			sys.exit(0)
	def SimpleExpression(self):
		if(self.currentToken=="*" or self.currentToken=="/" or self.currentToken=="+" or self.currentToken=="-" or self.currentToken==">=" or self.currentToken=="<=" or self.currentToken==">" or self.currentToken=="<" or self.currentToken=="==" or self.currentToken=="!="):


			self.TermPr()


			self.AddExpressionPr()


			self.RelOp()


			self.AddExpression()

		else:
			print("reject")
			sys.exit(0)
	def SelectionStatementPr(self):
		if(self.currentToken==";" or self.currentToken=="id" or self.currentToken=="if" or self.currentToken=="return" or self.currentToken=="{" or self.currentToken=="while" or self.currentToken=="}"):

			return
		elif(self.currentToken=="else"):

			if(self.currentToken.getType()=="else")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Statement()

		else:
			print("reject")
			sys.exit(0)
	def SelectionStatement(self):
		if(self.currentToken=="if"):

			if(self.currentToken.getType()=="if")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="(")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Expression()

			if(self.currentToken.getType()==")")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Statement()


			self.SelectionStatementPr()

		else:
			print("reject")
			sys.exit(0)
	def AddOp(self):
		if(self.currentToken=="+"):

			if(self.currentToken.getType()=="+")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="-"):

			if(self.currentToken.getType()=="-")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def Term(self):
		if(self.currentToken=="(" or self.currentToken=="id" or self.currentToken=="num"):


			self.Factor()


			self.TermPr()

		else:
			print("reject")
			sys.exit(0)
	def ArgsListPr(self):
		if(self.currentToken==")"):

			return
		elif(self.currentToken==","):

			if(self.currentToken.getType()==",")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Expression()


			self.ArgsListPr()

		else:
			print("reject")
			sys.exit(0)
	def ReturnStatementPr(self):
		if(self.currentToken=="id"):


			self.Expression()

			if(self.currentToken.getType()==";")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken==";"):

			if(self.currentToken.getType()==";")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def FactorPr(self):
		if(self.currentToken=="[" or self.currentToken=="=" or self.currentToken=="*" or self.currentToken=="/" or self.currentToken==">=" or self.currentToken=="<=" or self.currentToken==">" or self.currentToken=="<" or self.currentToken=="==" or self.currentToken=="!=" or self.currentToken=="+" or self.currentToken=="-" or self.currentToken=="," or self.currentToken==")" or self.currentToken==";"):


			self.VarPr()

		elif(self.currentToken=="("):

			if(self.currentToken.getType()=="(")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Args()

			if(self.currentToken.getType()==")")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def StatementList(self):
		if(self.currentToken=="}"):

			return
		elif(self.currentToken==";" or self.currentToken=="id" or self.currentToken=="if" or self.currentToken=="return" or self.currentToken=="{" or self.currentToken=="while"):


			self.Statement()


			self.StatementList()

		else:
			print("reject")
			sys.exit(0)
	def ParamList(self):
		if(self.currentToken=="int" or self.currentToken=="float"):


			self.Param()


			self.ParamListPr()

		else:
			print("reject")
			sys.exit(0)
	def AddExpression(self):
		if(self.currentToken=="(" or self.currentToken=="id" or self.currentToken=="num"):


			self.Term()


			self.AddExpressionPr()

		else:
			print("reject")
			sys.exit(0)
	def Expression(self):
		if(self.currentToken=="id"):

			if(self.currentToken.getType()=="id")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.ExpressionPr()

		else:
			print("reject")
			sys.exit(0)
	def FunDeclaration(self):
		if(self.currentToken=="int" or self.currentToken=="float" or self.currentToken=="void"):


			self.TypeSpecifier()

			if(self.currentToken.getType()=="id")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="(")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Params()

			if(self.currentToken.getType()==")")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.CmpdStatement()

		else:
			print("reject")
			sys.exit(0)
	def RelOp(self):
		if(self.currentToken==">="):

			if(self.currentToken.getType()==">=")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="=="):

			if(self.currentToken.getType()=="==")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="<="):

			if(self.currentToken.getType()=="<=")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="!="):

			if(self.currentToken.getType()=="!=")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="<"):

			if(self.currentToken.getType()=="<")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken==">"):

			if(self.currentToken.getType()==">")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def VarDeclarationPr(self):
		if(self.currentToken=="["):

			if(self.currentToken.getType()=="[")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="num")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="]")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="id"):

			if(self.currentToken.getType()=="id")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def DeclarationList(self):
		if(self.currentToken=="int" or self.currentToken=="float" or self.currentToken=="void"):


			self.Declaration()


			self.DeclarationListPr()

		else:
			print("reject")
			sys.exit(0)
	def LocalDeclaration(self):
		if(self.currentToken==";" or self.currentToken=="id" or self.currentToken=="if" or self.currentToken=="return" or self.currentToken=="{" or self.currentToken=="while"):

			return
		elif(self.currentToken=="int" or self.currentToken=="float" or self.currentToken=="void"):


			self.VarDeclaration()


			self.LocalDeclaration()

		else:
			print("reject")
			sys.exit(0)
	def TermPr(self):
		if(self.currentToken==">=" or self.currentToken=="<=" or self.currentToken==">" or self.currentToken=="<" or self.currentToken=="==" or self.currentToken=="!=" or self.currentToken=="+" or self.currentToken=="-"):

			return
		elif(self.currentToken=="*" or self.currentToken=="/"):


			self.MulOp()


			self.Factor()


			self.TermPr()

		else:
			print("reject")
			sys.exit(0)
	def DeclarationPr(self):
		if(self.currentToken=="("):

			if(self.currentToken.getType()=="(")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Params()

			if(self.currentToken.getType()==")")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.CmpdStatement()

		elif(self.currentToken=="["):

			if(self.currentToken.getType()=="[")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="num")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="]")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		elif(self.currentToken=="int" or self.currentToken=="float" or self.currentToken=="void" or self.currentToken=="$"):

			return
		else:
			print("reject")
			sys.exit(0)
	def VarPr(self):
		if(self.currentToken=="=" or self.currentToken=="*" or self.currentToken=="/" or self.currentToken==">=" or self.currentToken=="<=" or self.currentToken==">" or self.currentToken=="<" or self.currentToken=="==" or self.currentToken=="!=" or self.currentToken=="+" or self.currentToken=="-"):

			return
		elif(self.currentToken=="["):

			if(self.currentToken.getType()=="[")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Expression()

			if(self.currentToken.getType()=="]")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def Call(self):
		if(self.currentToken=="id"):

			if(self.currentToken.getType()=="id")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="(")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Args()

			if(self.currentToken.getType()==")")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
		else:
			print("reject")
			sys.exit(0)
	def ReturnStatement(self):
		if(self.currentToken=="return"):

			if(self.currentToken.getType()=="return")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.ReturnStatementPr()

		else:
			print("reject")
			sys.exit(0)
	def IterationStatement(self):
		if(self.currentToken=="while"):

			if(self.currentToken.getType()=="while")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)
			if(self.currentToken.getType()=="(")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Expression()

			if(self.currentToken.getType()==")")
				self.nextToken()
			else:
				print("reject")
				sys.exit(0)

			self.Statement()

		else:
			print("reject")
			sys.exit(0)
