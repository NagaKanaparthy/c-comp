#!/usr/bin/python
import sys
import re

from token import Token

#functions
class Lex:
	commentLvl = 0
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
		linePos = 0
		upPos = line.find("/*", linePos)
		#while(len(line) > upPos):
		#	upPos = line.find("/*",linePos)
		#	downPos = line.find("*/",linePos)
		#	if (upPos > 0):
		#		self.commentLvl+=1;
		#		return ""
		#	elif(upPos < 0 and self.commentLvl == 0):
		#
		return line
				

	def removeComments(self,fileName):
		dataFile = open(fileName,"r")
		tokens = []
		for line in iter(dataFile):
			line = self.stripSingleLineComments(line)
			line = self.checkForCommentLevelers(line);
			if(self.commentLvl == 0 and (len(line) != 0)):
				print line
		dataFile.close()
		return
