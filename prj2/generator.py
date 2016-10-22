import sys
from token import Token
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
imports = "import sys\nfrom token import Token\nfrom rule import RuleDictionary"
header = imports + "\nclass "+outputFileName+"\n"
constructer  = "\tdef __init__(self, tokenList):\n"
constructer += "\t\ttokenList.append(Token(\"$\",\"$\"))\n"
constructer += "\t\tself.tokenList = tokenList\n"
string = header + constructer + string
#generate print to file
fileOutput = open(outputFileName,'w')
fileOutput.write(string)
fileOutput.close()
