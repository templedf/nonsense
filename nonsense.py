import random
import sys
from collections import defaultdict
from pathlib import Path

text = "I slit a sheet. A sheet I slit. Upon a slitted sheet I sit."
start=""

def parse(text):
	table=defaultdict(list)
	sentences=text.lower().strip().split(".")
	for sentence in sentences:
		if sentence=="":
			continue
		parse_sentence(table,sentence)
	return table

def parse_sentence(table,sentence):

	words=sentence.strip().split(" ")
	table[start]+=[words[0]]
	for i in range(len(words)-1):
		table[words[i]]+=[words[i+1]]
	table[words[-1]]+="."

def pick(table, word):
	n=len(table[word])
	return table[word][random.randint(0, n-1)]

def read(file):
	text=Path(file).read_text()
	return parse(text)

if len(sys.argv)>1:
	table=read(sys.argv[1])
else:
	table=parse(text)

word=start
while word!=".":
	sys.stdout.write(word)
	sys.stdout.write(" ")
	word=pick(table, word)
print(".")