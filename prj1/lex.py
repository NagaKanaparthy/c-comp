#!/usr/bin/python
import itertools
import sys
import re

from token import Token
from commentFSM import commentFSM

#functions
class Lex:
	keywords = ["if","else","int","void","while","float","return"]
	specialChars = ['+','-','/','*','<','>', ">=", "<=", "==", "=", "!=", ";",",","(",")","[","]","{","}"] 
	idRegex=r'([a-zA-Z]+)'
	intRegex=r'([+-])?(\d+)'
	floatRegex=r'([+-])?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
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
		charsPattern = re.compile(r'([ 0-9a-zA-Z]+)*([\]\[{}\)\(;,/(<=)(>=)(!=)+-])')
		data = re.finditer(charsPattern,token)
		tokenList = []
		finalList = []
		for toke in data:
			if(toke != None):
				tokenList.extend(list(toke.groups()))
		#Strip Nones fomr search Match Results
		while(None in tokenList):
			tokenList.remove(None)
		for token in tokenList:
			finalList.extend(token.split())
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

	def tokenAnalyzer(self, tokens):
		tokenString = " ".join(str(token) for token in tokens)
		tokenList = self.splitCharsToken(tokenString)
		tokenObjs = []
		for i in range(0,len(tokenList)):
			if(self.tokenIsKeyword(tokenList[i])):
				tokenObjs.append(Token(tokenList[i], "kw"))	
			
			elif(self.tokenIsId(tokenList[i])):
				tokenObjs.append(Token(tokenList[i], "id"))
			
			elif(self.tokenIsInt(tokenList[i])):
				tokenObjs.append(Token(tokenList[i], "int"))
			
			elif(self.tokenIsFloat(tokenList[i])):
				tokenObjs.append(Token(tokenList[i], "float"))

			elif(self.tokenIsSpecialChar(tokenList[i])):
				if(tokenList[i] == ">" or tokenList[i] == "<" or tokenList[i] == "!" or tokenList[i] == "="):
					if((i+1) != len(tokenList)):

						if(tokenList[i+1] == "="):
							msg = tokenList[i] + tokenList[i+1]
							tokenObjs.append(Token(msg, msg))
							continue

					elif(tokenList[i] == "!"):
						tokenObjs.append(Token(tokenList[i], "Error"))
						continue
				tokenObjs.append(Token(tokenList[i], tokenList[i]))

			else:
				tokenObjs.append(Token(tokenList[i],"Error"))

		return tokenObjs

	def printTokenTable(self, tokens):
		print "token	|type	"
		print "-----------------"
		for token in tokens:
			row = token.getValue() + "	|" + token.getType()
			print row
		return
