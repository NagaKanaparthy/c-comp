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
					result+="\t\tif("+sRule.getConditionalStatment()+"):\n"
					result+=self.parseRule(sRule.rule,rule)
					#if NonTerminal then make function call
					#else if statements with nextTokenUpdate
					first = False
				else:
					result+="\t\telif("+sRule.getConditionalStatment()+"):\n"
					result+=self.parseRule(sRule.rule,rule)
		result += "\t\telse:\n\t\t\tself.Reject(\""+ rule.name +"\")\n"
#		result += "\t\telse:\n\t\t\tif(self.debug):"+\
#				  "\n\t\t\t\tprint(\"REJECT@ "+rule.name+" with \"+self.currentToken.getType()+\"|\"+str(self.currentTokenNumber))\n"#+\"\n\t\t\tsys.exit(-1)\n"
		return result
	def parseRule(self,ruleString,rule):
		string = ""
		tokens = ruleString.split()
		depth = 3
		for tok in tokens:
			if('@' == tok):
				string += self.getTabString(depth) +"return\n"
			elif(self.isNonTerminal(tok)):
				string += self.getTabString(depth) +"self."+tok+"()\n"
#				string += "\t\t\tif(self.debugAccept):\n"
#				string += "\t\t\t\tprint(\"accept@" + rule.name + "@" + ruleString + " : \"+self.currentToken.getType()" + ")\n"
			else:
#				string += "\t\t\tif(self.debugStates):\n"+\
#				 "\t\t\t\tprint (\""+rule.name+": \"+self.currentToken.getType()+\" | \"+self.currentToken.getValue())\n"
				string += self.getTabString(depth)+"if(self.currentToken.getType().strip()==\""+tok+"\"):\n"
				string += self.getTabString(depth+1)+"self.nextToken()\n"
				string += self.getTabString(depth)+"else:\n"
				string += self.getTabString(depth+1)+"self.Reject(\""+rule.name+"\")\n"
				depth += 1
		return string
	def isNonTerminal(self,token):
		if(self.rulesDictionary.get(token) != None):
			return True
		return False
	def getTabString(self,numTabs):
    		string = ""
		for r in range(0,numTabs):
    			string += '\t'
		return string
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
				string+="self.currentToken.getType().strip()==\""+token+"\""
				first = False
			else:
				string+=" or self.currentToken.getType().strip()==\""+token+"\""
		return string
	def toString(self):
		return self.rule+"|"+str(self.predicitTokens)
