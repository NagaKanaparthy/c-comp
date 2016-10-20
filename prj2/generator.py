import sys
from token import Token
from rule import RuleDictionary
from rule import Rule
from rule import SubRule
#get target output filename
outputFileName = sys.argv[1]
#read in tokens
def readTokens():
    return tokens = open("token.form","r").read().split()
#read in grammer
#generate parser with name from args
print(str(readTokens()))
