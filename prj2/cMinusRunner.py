import sys
from to import Token
from lex import Lex
from cminus import cminus
# main function
fileName = sys.argv[1]
lexer = Lex()
if (lexer.fileFound(fileName)):
        lexer.removeComments(fileName)
	serializedTokens = lexer.getTokens()
	tokens = lexer.tokenAnalyzer(serializedTokens)
parser = cminus(tokens)
#parser.nextToken()
parser.Program()
print('ACCEPT')
