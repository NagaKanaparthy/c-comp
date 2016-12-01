import os
import sys
from lex import Lex
from cminus import cminus
# main function
fileName = sys.argv[1]
lexer = Lex()
if (lexer.fileFound(fileName)):
	lexer.removeComments(fileName)
	serializedTokens = lexer.getTokens()
	tokens = lexer.tokenAnalyzer(serializedTokens)
	os.remove("temp.l")
	os.remove("tempTokens")
	os.remove("temp.tok")
parser = cminus(tokens)
#parser.nextToken()
parser.Program()
print('ACCEPT')
