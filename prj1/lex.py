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
	
	def tokenAnalyzer(self, tokens):
		tokenString = " ".join(str(x) for x in tokens)
		tokenList = self.splitCharsToken(tokenString)
		print tokenList
		#Check if keyword
			# add as token obj
		#check if special char
			# add as token obj
		#check if Identifier
			# add as token obj
		#check if Num
			#check if float
				# add as token obj
			#check if int
				# add as token obj
		return tokens
