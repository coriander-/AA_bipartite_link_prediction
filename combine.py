# Program to take the highest predicted links and insert them into
# a new file

# usage: python combine.py <new edges> <old edges> <number of new edges> <output file>

import sys

# Check command line arguments
args = sys.argv
if len(args) != 5:
	print "Usage: python " + args[0] + " <new edges> <old edges> <number of new edges> <output file>"
	quit()
	
newName = str(args[1])
oldName = str(args[2])
numEdges = int(args[3])
outputName = str(args[4])

# First, copy the old file into the new file
old = open(oldName, "r")
output = open(outputName, "w")
for line in old:
	line = line.rstrip()
	[left, right] = line.split("\t")
	output.write(str(left) + "\t" + str(right) + "\n")

# Now write the best predicted links to the file
new = open(newName, "r")
count = 0
for line in new:
	line = line.rstrip()
	[score, left, right] = line.split("\t")
	output.write(str(left) + "\t" + str(right) + "\n")
	count += 1
	#print "count: " + str(count) + " numEdges: " + str(numEdges)
	if count >= numEdges:
		break

