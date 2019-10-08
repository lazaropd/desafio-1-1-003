import string, sys

# Formato de entrada : python programa.py arquivo-de-entrada.txt 

fileName = sys.argv[1]
inputFile = open(fileName,"r")

words = inputFile.read().splitlines()
print(words)

