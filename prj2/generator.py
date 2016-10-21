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
class Rule:
    def __init__(self,ruleTokenString):
        self.confilct = False
        self.confilctingSubRules = []
        dataList = ruleTokenString.split('|')
        self.name = dataList[0]
        self.subRules = {dataList[1] : SubRule(dataList[1],dataList[2])}
	def fuseRules(self,rule):
		for subRuleToFuse in rule.subRules.values:
			for subRuleInDict in self.subRules.values:
				for token in subRuleInDict.predicitTokens:
					for tokenFuse in subRuleToFuse.predicitTokens:
						if(token == tokenFuse):
							self.conflict = True
							self.confilctingSubRules.append(subRuleToFuse)
							self.confilctingSubRules.append(subRuleInDict)
			self.subRules.update({subRuleToFuse.rule:subRuleToFuse})
    def toString(self):
        string = "Rule:"+self.name+'\n'
        for srule in self.subRules.values():
            string +=srule.toString()+'\n'
	return string
class SubRule:
    def __init__(self, rule, predicitTokenString):
        self.rule = rule
        self.predicitTokens = []
        for token in predicitTokenString.split():
            self.predicitTokens.append(token)
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
#generate parser with name from args
#tokenList = readTokenDictionary()
