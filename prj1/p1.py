#!usr/bin/python
import sys
from lex import Lex
# main function
fileName = sys.argv[1]
lexer = Lex()
if (lexer.fileFound(fileName)):
        serializedTokens = lexer.removeComments(fileName)
	tokens = lexer.tokenAnalyzer(serializedTokens)
        lexer.printTokenTable(tokens)
