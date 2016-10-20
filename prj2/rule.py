import sys
from token import Token
class Rule:
    numberRules = 0
    def __init__(self,name,subrule):
        self.name = name
        self.subrule = subrule
        Rule.numberRules += 1

    def rulecount():
        print("Total # of Rules: "Rule.numberRules)

class SubRule:
    def __init__(rule, predicitTokenString):
        self.flagWarning = False
        self.rule = rule
        self.predicitTokens = {}
        for token in predicitTokenString.split():
            predicitTokens.update(token, Token())
