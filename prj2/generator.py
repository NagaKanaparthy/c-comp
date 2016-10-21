import sys
from token import Token
class RuleDictionary:
	def __init__(self,rulesList):
		self.rulesDictionary = {}
		for rule in rulesList:
			ruleInDict = self.rulesDictionary.get(rule.name)
			if(ruleInDict == None):
				self.rulesDictionary.update({rule.name:rule})
			else:
				#add fuse rules and flag rule if confilct in predict sets
				ruleInDict.fuseRules(rule)
	def generateFunction(self,rule):
		result = "\tdef "+rule.name+"(self):\n"
		if(rule.conflict):
			result = "#Conflict" + result
		else:
			first = True
			for sRule in rule.subRules.values():
				if(first):
					result+="\t\tif("+sRule.getConditionalStatment()+"):\n\n"
					result+=self.parseRule(sRule.rule)
					#if NonTerminal then make function call
					#else if statements with nextTokenUpdate
					first = False
				else:
					result+="\t\telif("+sRule.getConditionalStatment()+"):\n\n"
					result+=self.parseRule(sRule.rule)
		result += "\t\telse:\n\t\t\tprint(\"reject\")\n"
		return result
	def parseRule(self,ruleString):
		string = ""
		tokens = ruleString.split()
		for tok in tokens:
			if('@' == tok):
				string += "\t\t\treturn\n"
			elif(self.isNonTerminal(tok)):
				string += "\n\t\t\tself."+tok+"()\n\n"
			else:
				string += "\t\t\tif(self.currentToken==\""+tok+"\")\n"
				string += "\t\t\t\tself.nextToken()\n"
				string += "\t\t\telse:\n\t\t\t\tprint(\"reject\")\n"
		return string
	def isNonTerminal(self,token):
		if(self.rulesDictionary.get(token) != None):
			return True
		return False
		#print(str(tokens))
	def toString(self):
		string = ""
		for rule in self.rulesDictionary.values():
			string += rule.toString()+'\n'
		return string
class Rule:
	def __init__(self,ruleTokenString):
		self.conflict = False
		self.confilctingSubRules = []
		dataList = ruleTokenString.split('|')
		self.name = dataList[0]
		self.subRules = {dataList[1] : SubRule(dataList[1],dataList[2])}
	def fuseRules(self,rule):
		for subRuleToFuse in rule.subRules.values():
			for subRuleInDict in self.subRules.values():
				for token in subRuleInDict.predicitTokens:
					for tokenFuse in subRuleToFuse.predicitTokens:
						if(token == tokenFuse):
							self.conflict = True
							self.confilctingSubRules.append(subRuleToFuse)
							self.confilctingSubRules.append(subRuleInDict)
			self.subRules.update({subRuleToFuse.rule:subRuleToFuse})
	def toString(self):
		string = "Rule:"+self.name
		if(self.conflict):
			string+=" ! : "
			for value in self.confilctingSubRules:
				string+="|"+value.rule
		string+='\n'
		for srule in self.subRules.values():
			string +=srule.toString()+'\n'
		return string
	def getConflicts(self):
		string = ""
		for value in self.confilctingSubRules:
                                string+="|"+value.rule
		return string
class SubRule:
	def __init__(self, rule, predicitTokenString):
		self.rule = rule
		self.predicitTokens = []
		for token in predicitTokenString.split():
			self.predicitTokens.append(token)
	def getConditionalStatment(self):
		string=""
		first = True
		for token in self.predicitTokens:
			if(first):
				string+="self.currentToken==\""+token+"\""
				first = False
			else:
				string+=" or self.currentToken==\""+token+"\""
		return string
	def toString(self):
		return self.rule+"|"+str(self.predicitTokens)
#from rule import RuleDictionary
#from rule import Rule
#from rule import SubRule
#get target output filename
outputFileName = sys.argv[1]
#read in grammer
rules = []
with open("grammer.form", "r") as ins:
    for line in ins:
        rules.append(Rule(line))
#Create Dictionary
ruleDict = RuleDictionary(rules)
for rule in ruleDict.rulesDictionary.values():
	if(rule.conflict == True):
		print(rule.name+" - "+rule.getConflicts())
#print(ruleDict.toString())
#generate parser with name from args
#tokenList = readTokenDictionary()
