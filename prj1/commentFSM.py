#!/usr/bin/python
import sys
class commentFSM:
    debugMode = True
    currentChar = ''
    filename = ''
    depth = 0
    inputFile = None
    outputFile = None

    def __init__(self, inputFilename):
        self.currentChar = ''
        self.filename = inputFilename
        self.inputFile = open(inputFilename, "r")
        self.outputFile = open("temp.l", "w+")
        return

    def getNextChar(self):
        self.currentChar = self.inputFile.read(1)
        if(self.currentChar == ''):
            return
        return self.currentChar

    def startState(self):
        self.getNextChar()
        if self.debugMode:
            print "State 1 :"+self.currentChar
        if '/' in self.currentChar:
            self.getNextChar()
            self.stateTwo()
        elif self.currentChar == '':
            return
        else:
            self.stateFive()
        return

    def stateTwo(self):
        if self.debugMode:
            print "State 2 :"+self.currentChar
        #Handles line comment
        if '/' in self.currentChar:
            self.stateThree()
        #Handles multi-line comment
        elif '*' in self.currentChar:
            self.stateFour()
        else:
            self.outputFile.write('/')
            self.stateFive()
        return

    def stateThree(self):
        while True:
            self.getNextChar()
            if self.debugMode:
                print "State 3 : "+self.currentChar
            if '\n' in self.currentChar:
                break
        self.startState()
        return

    def stateFour(self):
        self.depth += 1
        self.getNextChar()
        if self.debugMode:
            print "State 4 - Depth : "+str(self.depth)+" :"+self.currentChar
        if '*' in self.currentChar:
            self.stateSix()
        elif '/' in self.currentChar:
            self.stateNine()
        else:
            self.stateEight()
        return

    def stateFive(self):
        if self.debugMode:
            print "Outputted Char : "+str(self.currentChar)
        if self.outputFile is not None:
            self.outputFile.write(self.currentChar)
        self.startState()
        return

    def stateSix(self):
        self.getNextChar()
        if self.debugMode:
            print "State 6 : "+self.currentChar
        if '/' in self.currentChar:
		self.stateSeven()
        elif '*' in self.currentChar:
		self.stateSix()
	else:
            self.stateEight()
        return

    def stateSeven(self):
        self.depth -= 1
        if self.debugMode:
            print "State 7 - Depth : "+str(self.depth)
        if(self.depth > 0):
            self.stateEight()
        else:
            self.startState()
        return

    def stateEight(self):
        self.getNextChar()
        if self.debugMode:
            print "State 8 : "+self.currentChar
        if '*' in self.currentChar:
            self.stateSix()
        elif '/' in self.currentChar:
            self.stateNine()
        elif self.currentChar == '':
            return
        else:
            self.stateEight()
        return

    def stateNine(self):
        self.getNextChar()
        if self.debugMode:
            print "State 9 : "+self.currentChar
        if '*' in self.currentChar:
            self.stateFour()
        elif '/' in self.currentChar:
            self.stateNine()
        else:
            self.stateEight()
        return
