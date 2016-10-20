import sys
from token import Token
class RuleDictionary:
   def __init__(self,rulesList):
	self.rulesDictionary = {}
	for rule in rulesList:
            if(self.rulesDictionary.get(rule.name) == None):
                self.rulesDictionary.update({rule.name:rule})
            else:
                print(rule.toString())
		
class Rule:
    def __init__(self,ruleTokenString):
        self.confilct = False
        self.confilctingSubRules = []
        dataList = ruleTokenString.split('|')
        self.name = dataList[0]
        self.subRules = {dataList[1] : SubRule(dataList[1],dataList[2])}
    def toString(self):
        string = "Rule:"+self.name+'\n'
        for srule in self.subRules.values():
            string +=srule.toString()+'\n'
	return string
class SubRule:
    def __init__(self, rule, predicitTokenString):
        self.rule = rule
        self.predicitTokens = {}
        for token in predicitTokenString.split():
            self.predicitTokens.update({token:token})
    def toString(self):
        return self.rule+"|"+str(self.predicitTokens.keys())
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
