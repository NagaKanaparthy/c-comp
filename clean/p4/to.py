#!usr/bin/python
class Token:
	def __init__(self, val="", tokenTypeVal="",depthVal=0):
		self.value = val
		self.tokenType = tokenTypeVal
		self.depth = depthVal	
	def getValue(self):
		return self.value
	def getType(self):
		return self.tokenType
	def getDepth(self):
		return self.depth
	def parseLine(self,line):
		values = line.split("|")
		self.value = values[0]
		self.tokenType = values[1]
	def toString(self):
		return self.value+"|"+self.tokenType
