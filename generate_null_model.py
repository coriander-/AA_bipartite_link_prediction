# Randomly add the given number of links back to a bipartite graph.  

# Usage: python aa_tranverse.py [input file] [output file] [number of new edges]

# Storage: left and right nodes each stored in a separate dict.
# Easy to iterate over all links, and the degree of a node is
# the size of the set

import sys
import math
import random

# Check command line arguments
args = sys.argv
if len(args) != 4:
	print "Usage: python " + args[0] + " <input graph> <output file> <number of new edges>"
	quit()
	
inputGraph = str(args[1])
outputFile = str(args[2])
numEdges = int(args[3])

leftNodes = {}
rightNodes = {}

# Read pairs of edges into a dict
#pairs = []
input = open(inputGraph, "r")
for line in input:
	line = line.rstrip()
	[left, right] = line.split("\t")
	
	# Add to dictionaries
	if left in leftNodes:
		leftNodes[left].add(right)
	else:
		leftNodes[left] = set([right])
	
	if right in rightNodes:
		rightNodes[right].add(left)
	else:
		rightNodes[right] = set([left])

# Generate the list of new pairs
newPairs = []
for i in range(0, numEdges):
	while True:
		newLeft = random.choice(leftNodes.keys())
		newRight = random.choice(rightNodes.keys())
		if (newRight not in leftNodes[newLeft]):
			leftNodes[newLeft].add(newRight)
			rightNodes[newRight].add(newLeft)
			break
					
# print everything to a file
output = open(outputFile, "w")
for i in leftNodes.keys():
	for j in leftNodes[i]:
		output.write(str(i) + "\t" + str(j) + "\n")
			
			
			
			
			
			
