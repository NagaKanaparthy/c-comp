import sys
from cminus import cMinus
from token import Token
#get Tokens from sys.in
tokens = []
header = 2
for line in sys.stdin:
	if(header > 0):
		header -= 1
	else:
		temp = Token("","")
		temp.parseLine(line)
		tokens.append(temp)
