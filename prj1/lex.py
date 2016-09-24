#!/usr/bin/python
import itertools
import sys
import re

from token import Token
from commentFSM import commentFSM

#functions
class Lex:
	debugMode = True
	keywords = ["if","else","int","void","while","float","return"]
	specialChars = ['+','!','-','/','*','<','>', ">=", "<=", "==", "=", "!=", ";",",","(",")","[","]","{","}"] 
	idRegex=r'([a-zA-Z]+)'
	intRegex=r'^(\d+)$'
	floatRegex=r'^(\d+(\.\d+)?)([E][+-]?\d+)?'
	def fileFound(self,fileName):
		try:
			testFile = open(fileName,"r")
			testFile.close()
			return True
		except IOError:
			print "File Not Found"
			return False

	def tokenize(self, line):
		tokens = line.split()
		return tokens
	
	def removeComments(self,fileName):
		removerStateMachine = commentFSM(fileName)
		removerStateMachine.startState()
		return

	def getTokens(self):
		tokens = []
		with open('temp.l','r') as cleanFile:
			tokens.extend(self.tokenize(cleanFile.read()))
		return tokens
	def splitCharsToken(self, token):
		charsPattern = re.compile(r'([\.\]\[{}\)\(;,/(<=)(>=)(!=)+-])')
		if(re.match(charsPattern, token) is not None):
			data = re.split(charsPattern,token)
			tokenList = []
			finalList = []
			while(None in tokenList):
				tokenList.remove(None)
			for tok in tokenList:
				finalList.extend(tok)
		else:
			return token
		return finalList
						
	def tokenIsKeyword(self, token):
		for keyword in self.keywords:
			if(keyword == token):
				return True
		return False

	def tokenIsId(self, token):
		found = re.match(self.idRegex,token)
		if(found):
			return True
		return False
	
	def tokenIsInt(self,token):
		found = re.match(self.intRegex,token)
		if(found):
			return True
		return False

	def tokenIsFloat(self,token):
		found = re.match(self.floatRegex, token)
		if(found):
			return True
		return False

	def tokenIsSpecialChar(self, token):
		for char in self.specialChars:
			if(char == token):
				return True
		return False

	def tokenHasChar(self,token):
		for char in self.specialChars:
			if(char in token):
				return True
		return False

	def tokenAnalyzer(self, tokens):
		tokenString = " ".join(str(token) for token in tokens)
		tokensTemp = tokenString.split()
		tokenList = []
		fileData = open("tempTokens","w+")
		for tempToken in tokensTemp:
			fileData.write("Tokens : "+tempToken+"\n")
    			if(self.tokenHasChar(tempToken)):
				tempTokenList = list(tempToken)
				counter = 0
				holdChars = ""
				while counter < len(tempTokenList):
					if(self.tokenIsSpecialChar(tempTokenList[counter])):
						if(holdChars != ""):
							tokenList.append(holdChars)
							holdChars = ""
						tokenList.append(tempTokenList[counter])
					else:
						holdChars += tempTokenList[counter]	
					counter += 1
				if(holdChars != ""):
					tokenList.append(holdChars)
			else:
				tokenList.append(tempToken)
		tokenObjs = []
		i = 0
		while i < len(tokenList):
			if(tokenList[i] is not None):
				if(self.tokenIsKeyword(tokenList[i])):
					tokenObjs.append(Token(tokenList[i], "kw"))
				elif(self.tokenIsId(tokenList[i])):
					tokenObjs.append(Token(tokenList[i], "id"))
				elif(self.tokenIsInt(tokenList[i])):
					tokenObjs.append(Token(tokenList[i], "number"))
				elif(self.tokenIsFloat(tokenList[i])):
					if("E" in tokenList[i]):
						if(i+1 < len(tokenList)):
							if(self.tokenIsInt(tokenList[i+1])):
								tokenObjs.append(Token(tokenList[i]+tokenList[i+1], "float"))
								i += 1
							elif("-" in tokenList[i+1] or "+" in tokenList[i+1]):
								if(i+2 < len(tokenList)):
									if(self.tokenIsInt(tokenList[i+2])):
										tokenObjs.append(Token(tokenList[i]+tokenList[i+1]+tokenList[i+2], "float"))
										i += 2
								else:
									tokenObjs.append(Token(tokenList[i]+tokenList[i+1], "Error - Float"))
									i += 1
							else:
								tokenObjs.append(Token(tokenList[i], "float"))
					else:
						tokenObjs.append(Token(tokenList[i], "float"))
				elif(self.tokenIsSpecialChar(tokenList[i])):
					if(tokenList[i] == ">" or tokenList[i] == "<" or "!" in tokenList[i] or tokenList[i] == "="):
						if((i+1) != len(tokenList)):
							if(tokenList[i] == "!"):
								if( tokenList[i+1] != "="):
									tokenObjs.append(Token(tokenList[i], "Error"))
								else:
									i += 1
									tokenObjs.append(Token("!=","!="))
							elif(tokenList[i] == "=" or tokenList[i] == "<" or tokenList[i] == ">"):
								if(tokenList[i+1] == "="):
    									msg = tokenList[i] + tokenList[i+1]
									tokenObjs.append(Token(msg, msg))
									i += 1
								else:
									tokenObjs.append(Token(tokenList[i], tokenList[i]))
					else:
						tokenObjs.append(Token(tokenList[i], tokenList[i]))
				else:
					tokenObjs.append(Token(tokenList[i],"Error"))
			i+=1
		return tokenObjs

	def printTokenTable(self, tokens):
		fileTokens = open("temp.tok","w+")
		fileTokens.write("token    |type\n-----------------\n")
		print "token	|type	"
		print "-----------------"
		for token in tokens:
			row = token.getValue() + "	|" + token.getType()
			fileTokens.write(row+"\n")
			print row
		return
