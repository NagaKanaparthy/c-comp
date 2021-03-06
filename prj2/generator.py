import sys
from to import Token
from rule import RuleDictionary
from rule import Rule
from rule import SubRule
#get target output filename
outputFileName = sys.argv[1]
#read in grammer
rules = []
with open("grammer.form", "r") as ins:
    for line in ins:
        rules.append(Rule(line))
#Create Dictionary
string =""
ruleDict = RuleDictionary(rules)
for rule in ruleDict.rulesDictionary.values():
	if(rule.conflict == False):
		string += ruleDict.generateFunction(rule)
	else:
		print(rule.name)
#gen header
imports = "import sys\nfrom to import Token\n"
header = imports + "class "+outputFileName+":\n"
constructer  = "\tdef __init__(self, tokenList):\n"
constructer += "\t\ttokenList.append(Token(\"$\",\"$\"))\n"
constructer += "\t\tself.tokenList = tokenList\n"
constructer += "\t\tself.currentTokenNumber = 0\n"
constructer += "\t\tself.currentToken=tokenList[0]\n"
nextToken =   "\tdef nextToken(self):\n"
nextToken +=   "\t\tif(self.currentTokenNumber < len(self.tokenList)):\n"
nextToken +=   "\t\t\tself.currentTokenNumber += 1\n"
nextToken +=   "\t\tself.currentToken = self.tokenList[self.currentTokenNumber]\n"
string = header + constructer + nextToken + string
#generate print to file
fileOutput = open(outputFileName+".py",'w')
fileOutput.write(string)
fileOutput.close()
