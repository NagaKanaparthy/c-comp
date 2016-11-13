import sys
from lex import Lex
# main function
fileName = sys.argv[1]
lexer = Lex()
if (lexer.fileFound(fileName)):
        lexer.removeComments(fileName)
	serializedTokens = lexer.getTokens()
	tokens = lexer.tokenAnalyzer(serializedTokens)
        lexer.printTokenTable(tokens)
