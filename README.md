AA_bipartite_link_prediction
============================

Collection of Python scripts written for a Complex Networks Project.  This repository contains scripts useful for performing Adamic/Adar link prediction on an unweighted bipartite network.

Files included:

aa_traverse.py - Takes a bipartite graph as input (stored as a text file in an adjacency list) and computes the Adamic/Adar similarity of each non-neighboring node pair.  The similarity is computed using the degree of the intermediate nodes.  The output file is written as a text file containing three fields per row.  The first number is the score of the pair, and the second two fields are the two nodes in question.

combine.py - Takes the highest predicted links in the (sorted) file output by aa_traverse.py and adds them to the network, storing the new network in a new file.  The number of predicted links added to the network is specified via the command line.  (I used the sort utility to sort the output from aa_traverse to put the highest scoring links at the top of the file before sending the file to combine.)

generate_null_model.py - Generates a null model by randomly adding a certain number of edges to the given network.  The number of edges to add is specified via the command line.

testRestore.py - Compares the original graph with the restored graph and outputs some basic statistics regarding the accuracy of the prediction.  The number of predicted edges is specified via the command line.
