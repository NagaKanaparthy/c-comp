#!usr/bin/python
class Token:
	def __init__(self, val, tokenTypeVal):
		self.value = val
		self.tokenType = tokenTypeVal
	def getValue(self):
		return self.value
	def getType(self):
		return self.tokenType
