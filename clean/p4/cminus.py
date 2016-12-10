import sys
from sym import SymbolTable
from sym import Function
from to import Token
class cminus:
	def __init__(self, tokenList):
		tokenList.append(Token("$","$"))
		self.tokenList = tokenList
		#Current Token
		self.currentTokenNumber = 0
		self.currentToken=tokenList[0]
		self.tCounter = 0
		self.bCounter = 0
		#Data
		self.breakPosList = []
		self.valueStack = []
		self.symTable = SymbolTable()
		self.funcList = []
		self.quadOut = list()
		#Debug Flags
		self.debug = True
		self.debugReject = True
# Auxiallary Fucntions
	def getFunction(self,funcName=None):
		if(funcName is not None):
			for fun in self.funcList:
				if(fun.name == funcName):
					return fun
		return None
	def inFuncList(self,funcName=None):
		if(funcName is not None):
			for fun in self.funcList:
				if(fun.name == funcName):
					return True
		return False
	def getTempNameAndUpdate(self):
		self.tCounter += 1
		return "_t" + str(self.tCounter-1)
	def getTempName(self):
		return "_t" + str(self.tCounter)
	def nextToken(self):
		if(self.currentTokenNumber < len(self.tokenList)):
			self.currentTokenNumber += 1
			self.currentToken = self.tokenList[self.currentTokenNumber]
			return self.tokenList[self.currentTokenNumber-1]
	def Reject(self, stateName):
		if(self.debugReject):
			print("REJECT with token #"+str(self.currentTokenNumber)+":"+self.currentToken.getValue()+" @"+stateName+"\n")
		else:
			print("REJECT")
		sys.exit(1)
	def printQuad(self):
		for pos, quad in enumerate(self.quadOut):
			print str(pos)+'\t'+str(quad[0])+'\t'+str(quad[1])+'\t'+str(quad[2])+'\t'+str(quad[3])
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
			self.nextToken()
			return  "BGE"
		elif(self.currentToken.getType().strip()=="=="):
			self.nextToken()
			return "BEQ"
		elif(self.currentToken.getType().strip()=="<="):
			self.nextToken()
			return "BLE"
		elif(self.currentToken.getType().strip()=="!="):
			self.nextToken()
			return "BNE"
		elif(self.currentToken.getType().strip()=="<"):
			self.nextToken()
			return "BLT"
		elif(self.currentToken.getType().strip()==">"):
			self.nextToken()
			return "BGT"
		else:
			self.Reject("RelOp")
	def MulOp(self):
		if(self.currentToken.getType().strip()=="*"):
			self.nextToken()
			return "TIMES"
		elif(self.currentToken.getType().strip()=="/"):
			self.nextToken()
			return "DIV"
		else:
			self.Reject("MulOp")
	def AddOp(self):
		if(self.currentToken.getType().strip()=="+"):
			self.nextToken()
			return "ADD"
		elif(self.currentToken.getType().strip()=="-"):
			self.nextToken()
			return "SUB"
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
			typeResult = self.TypeSpecifier()
			self.DeclarationPr(typeResult)
		else:
			self.Reject("Declaration")
	def DeclarationPr(self,typeToken=Token()):
		if(self.currentToken.getType().strip()=="id"):
			idValue = self.nextToken()
			self.DeclarationPrPr(idValue,typeToken)
		else:
			self.Reject("DeclarationPr")
	def DeclarationPrPr(self,varFunId=Token(),varType=Token()):
		if(self.currentToken.getType().strip()=="("):
			if(self.currentToken.getType().strip()=="("):
				self.nextToken()
				paramList = self.Params()
				if(self.currentToken.getType().strip()==")"):
					self.nextToken()
					if(paramList == None):
						self.quadOut.append(["FUNC", "1", "void", varFunId.getValue()])
					else:
						self.quadOut.append(["FUNC", str(len(paramList)), varType.getValue(), varFunId.getValue()])
						for p in paramList:
							self.quadOut.append(["PARAM", "", "", p.getValue()])
						self.symTable.Insert(Token(varFunId.getValue(),"FUNC"))
						self.funcList.append(Function(varFunId.getValue(),paramList))
					self.CmpdStatement()
					self.quadOut.append(["END", " ", "", varFunId.getValue()])
				else:
					self.Reject("DeclarationPrPr")
			else:
				self.Reject("DeclarationPr")
		elif(self.currentToken.getType().strip()=="[" or self.currentToken.getType().strip()==";"):
			self.VarDeclaration(varFunId)
		else:
			self.Reject("DeclarationPr")
	def VarDeclaration(self,idToken=None):
		if(self.currentToken.getType().strip()==";"):
			self.nextToken()
			self.quadOut.append(["ALLOC", "4", " ", idToken.getValue()])
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
				if(self.currentToken.getType().strip()=="num"):
					number = self.nextToken()
					if(self.currentToken.getType().strip()=="]"):
						self.nextToken()
						if(self.currentToken.getType().strip()==";"):
							self.nextToken()
							self.quadOut.append(["ALLOC", str(4*int(number.getValue())), "", idToken.getValue()])
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
		listParams = []
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			paramType = self.DataTypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				paramId = self.nextToken()
				listParams.append(Token(paramId.getValue(),paramType.getValue()))
				self.ParamPr()
				remainingList = self.ParamList()
				if(remainingList is not None and len(remainingList) > 0):
					listParams.extend(remainingList)
				return listParams
			else:
				self.Reject("Params")
		elif(self.currentToken.getType().strip()=="void"):
			if(self.currentToken.getType().strip()=="void"):
				self.nextToken()
				self.ParamList()
				return None
			else:
				self.Reject("Params")
		else:
			self.Reject("Params")
	def ParamList(self, param=None):
		if(self.currentToken.getType().strip()==")"):
			return
		elif(self.currentToken.getType().strip()==","):
			if(self.currentToken.getType().strip()==","):
				self.nextToken()
				paramList = []
				param = self.Param()
				paramList.append(param)
				tempList = self.ParamList()
				if(tempList is not None):
					paramList.append(param)
					paramList.extend(tempList)
				return paramList
			else:
				self.Reject("ParamList")
		else:
			self.Reject("ParamList")
	def Param(self):
		if(self.currentToken.getType().strip()=="int" or self.currentToken.getType().strip()=="float"):
			dataType = self.DataTypeSpecifier()
			if(self.currentToken.getType().strip()=="id"):
				dataValue = self.nextToken()
				self.ParamPr()
				return Token(dataValue.getValue(),dataType.getValue())
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
				self.quadOut.append(["BLOCK"+str(self.bCounter),"","",""])
				self.bCounter += 1
				self.nextToken()
				self.symTable.IncreaseDepth()
				self.LocalDeclaration()
				self.StatementList()
				if(self.currentToken.getType().strip()=="}"):
					self.bCounter -= 1
					self.quadOut.append(["END","","","BLOCK"+str(self.bCounter)])
					self.nextToken()
					self.symTable.Pop()
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
			breakNum = self.breakPosList.pop()
			self.quadOut[breakNum][3] = len(self.quadOut)
		elif(self.currentToken.getType().strip()=="if"):
			self.SelectionStatement()
			breakNum = self.breakPosList.pop()
			self.quadOut[breakNum][3] = len(self.quadOut)
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
				breakNum = self.breakPosList.pop()
				#print(breakNum)
				self.valueStack[breakNum][3] = len(self.valueStack) + 1
				self.valueStack.append(["BR", " ", " ", " "])
				self.breakPosList.append(len(self.valueStack) - 1)
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
					whileLineNum = len(self.quadOut)
					self.Expression()
					if(self.currentToken.getType().strip()==")"):
						self.nextToken()
						self.Statement()
						self.quadOut.append(["BR", " ", " ", whileLineNum])
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
				returnValue = self.valueStack.pop()
				self.quadOut.append(["RET", " ", " ", returnValue])
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
				self.valueStack.append(self.nextToken().getValue())
				self.ExpressionPr()
			else:
				self.Reject("Expression")
		elif(self.currentToken.getType().strip()=="num"):
			self.valueStack.append(self.nextToken().getValue())
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
				paramList = []
				while(not self.inFuncList(self.valueStack[-1])):
					temp = self.valueStack.pop()
					paramList.append(temp)
				value = self.valueStack.pop()
				fun = self.getFunction(value)
				if(fun is not None):
					self.quadOut.append(["CALL", len(paramList), fun.name, self.getTempNameAndUpdate()])
					paramList.reverse()
					#print(paramList)
					for param in paramList:
						self.quadOut.append(["ARG", " ", " ", param])
				self.valueStack.append(value)
								
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
			left = self.valueStack.pop()
			right = self.valueStack.pop()
			self.quadOut.append(["ASSIGN", left, " ", right])
		else:
			self.Reject("ExpressionPrPr")
	def VarPr(self):
		if(self.currentToken.getType().strip() in ["<=",">=","==","!=","<",">","*","/","+","-","=",")",";","]",","]):
			return
		elif(self.currentToken.getType().strip()=="["):
			if(self.currentToken.getType().strip()=="["):
				self.nextToken()
				self.Expression()
				number = self.valueStack.pop()
				arrayName = self.valueStack.pop()
				self.quadOut.append(["DISP", arrayName, number, self.getTempNameAndUpdate()])
				self.valueStack.append(self.getTempName())
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
			breakType = self.RelOp()
			self.Term()
			self.AddExpression()
			right = self.valueStack.pop()
			left = self.valueStack.pop()
			self.quadOut.append(["COMP", left, right, self.getTempNameAndUpdate()])
			self.valueStack.append(self.getTempName())
			self.quadOut.append([breakType, " ", self.getTempName(), len(self.quadOut) + 2])
			self.quadOut.append(["BR", " ", " ", " "])
			whereAmI = len(self.quadOut)
			#print(whereAmI)
			self.breakPosList.append(whereAmI-1)
		elif(self.currentToken.getType().strip() in [")", ";", "]", ","]):
			return
		else:
			self.Reject("SimpleExpression")
	def AddExpression(self):
		if(self.currentToken.getType().strip() in ["<=",">=","==","!=","<",">",")",";","]",","]):
			return
		elif(self.currentToken.getType().strip()=="+" or self.currentToken.getType().strip()=="-"):
			operator = self.AddOp()
			self.Term()
			right = self.valueStack.pop()
			left = self.valueStack.pop()
			self.quadOut.append([operator, left, right, self.getTempNameAndUpdate()])
			self.valueStack.append(self.getTempName())
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
			operator = self.MulOp()
			self.Factor()
			right = self.valueStack.pop()
			left = self.valueStack.pop()
			self.quadOut.append([operator, left, right, self.getTempNameAndUpdate()])
			self.valueStack.append(self.getTempName())
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
				self.valueStack.append(self.nextToken().getValue())
			else:
				self.Reject("Factor")
		elif(self.currentToken.getType().strip()=="id"):
			if(self.currentToken.getType().strip()=="id"):
				self.valueStack.append(self.nextToken().getValue())
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
				paramList = []
				while(self.inFuncList(self.valueStack[-1])):
					paramList.append(self.valueStack.pop())
				fun = self.getFunction(self.valueStack.pop())
				self.quadOut.append(["CALL", len(paramList), " ", fun.name])
				for param in paramList:
					self.quadOut.append(["ARG", " ", " ", param])
				self.valueStack.append(func.name)
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