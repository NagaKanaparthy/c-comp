#!/usr/bin/python
import itertools
import sys
import re

from token import Token

#functions
class Lex:
	commentLevel = 0
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

	def stripSingleLineComments(self,line):
		try:
			posOfComment = line.find("//")
			if(posOfComment == -1):# -1 = Not Found
				return line
			else:
				return line[:posOfComment]
		except:
			return line
		return ""

	def checkForCommentLevelers(self,line):
		upPos = 0
		downPos = 0

		if(self.commentLevel == 0):
			upPos = line.find("/*")
			if(upPos > -1):
				self.commentLevel += 1
				line = line[:upPos]			

		if(self.commentLevel > 0):
			downPos = line.find("*/")
			if(downPos > -1):
				self.commentLevel -= 1
				line = line[downPos+2:]

		if(self.commentLevel > -1  and (line.find("*/") > -1 or line.find("/*") > -1)):
			return self.checkForCommentLevelers(line)

		return line	

	def tokenize(self, line):
		tokens = line.split()
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
						
	def removeComments(self,fileName):
		dataFile = open(fileName,"r")
		tokens = []
		for line in iter(dataFile):
			line = self.stripSingleLineComments(line)
			line = self.checkForCommentLevelers(line)
			if(len(self.tokenize(line)) > 0):
				tokens.extend(self.tokenize(line))
		dataFile.close()
		return tokens
	
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
		tokenString = " ".join(str(x) for x in tokens)
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
