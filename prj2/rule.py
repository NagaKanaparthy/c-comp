import sys
from token import Token
class RuleDictionary:
    def __init__(self):
        self.rules = {}
    def addRule(self, ruleTokenString):
        tempRule = Rule(ruleTokenString)
        #Check if rule is within dict. True then add subrule and
        if(tempRule)
    def rulecount(self):
        return len(self.rules)

class Rule:
    def __init__(self,ruleTokenString):
        self.confilct = False
        self.confilctingSubRules = []
        dataList = ruleTokenString.split('|')
        self.name = dataList[0]
        self.subRules = {dataList[1] : SubRule(dataList[1],dataList[2])}
    def __init__(self,name,subRule):
        self.confilct = False
        self.confilctingSubRules = []
        self.name = name
        self.subRules = {subRule.rule : subRule}
    def addSubRule(self, subRule):
        if(self.subRule.get(subRule.rule) != None):
            print("Error Fix your grammer duplicate sub rule")
            sys.exit()
        else:
            toAdd = []
            for rule,token in self.subRules:
                for comparingKey,comparingToken in subRule.predicitTokens:
                    if(key == comparingKey):
                        self.
                    else:
                        toAdd.append(comparingKey)


class SubRule:
    def __init__(self, rule, predicitTokenString):
        self.rule = rule
        self.predicitTokens = {}
        for token in predicitTokenString.split():
            predicitTokens.update(token, Token(token))
    def  compareRulePredicates(self,comparingSubRule):
