# Program to measure the number of successfully restored edges

# Usage: python testRestore.py <original> <restored> <number of predicted edges>

import sys

# Check command line arguments
args = sys.argv
if len(args) != 4:
	print "Usage: python " + args[0] + " <original> <restored> <number of predicted edges>"
	quit()

numPredicted = int(args[3])

orig = set()
rest = set()

origFile = open(args[1], "r")
restFile = open(args[2], "r")

# Read in each file into a set of tuples
filesize = 0
for line in origFile:
	line = line.rstrip()
	data = line.split("\t")
	dataTup = tuple(data)
	orig.add(dataTup)
	filesize += 1

for line in restFile:
	line = line.rstrip()
	data = line.split("\t")
	dataTup = tuple(data)
	rest.add(dataTup)

# Get the difference and determine the percentage of correctness
FP = len([x for x in rest if x not in orig])
FN = len([x for x in orig if x not in rest])
TP = numPredicted - FP
TN = numPredicted - FN
SR = float(TP) / numPredicted

print "Stats:"
print "False Positives: " + str(FP)
print "False Negatives: " + str(FN)
print "True Positives: " + str(TP)
print "True Negatives: " + str(TN)

print "Success Rate: " + str(SR * 100) + "%"
