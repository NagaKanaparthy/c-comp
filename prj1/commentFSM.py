#!/usr/bin/python
import sys
class commentFSM:
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
        return self.currentChar

    def startState(self):
        self.getNextChar()
        if(self.currentChar == '/'):
            self.getNextChar()
            self.stateTwo()
        elif(self.currentChar is None):
            return
        else:
            self.stateFive()
        return

    def stateTwo(self):
        #Handles line comment
        if(self.currentChar == '/'):
            self.stateThree()
        #Handles multi-line comment
        elif(self.currentChar == '*'):
            self.stateFour()
        else:
            self.stateFive('/')
            self.stateFive()
        return

    def stateThree(self):
        while True:
            self.getNextChar()
            if self.currentChar == '\n':
                break
        self.startState()
        return

    def stateFour(self):
        self.depth += 1
        self.getNextChar()
        if self.currentChar == '*':
            self.stateSix()
        elif self.currentChar == '/':
            self.stateNine()
        else:
            self.stateEight()
        return

    def stateFive(self):
        if self.outputFile is not None:
            self.outputFile.write(self.currentChar)
        self.startState()
        return

    def stateSix(self):
        if self.currentChar == '/':
            self.stateSeven()
        else:
            self.stateEight()
        return

    def stateSeven(self):
        self.depth -= 1
        if(self.depth > 0):
            self.stateFour()
        else:
            self.startState()
        return

    def stateEight(self):
        self.getNextChar()
        if self.currentChar == '*':
            self.stateSix()
        elif self.currentChar == '/':
            self.stateFour()
        else:
            self.stateEight()
        return

    def stateNine(self):
        self.getNextChar()
        if self.currentChar == '*':
            self.stateFour()
        else:
            self.stateEight()
        return
