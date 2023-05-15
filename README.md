# Witness-Set
This repository collects a small collection of functions to calculate the witness set of ensembles of binary vectors.

Given a list of binary n-tuples (for simplicty 'vectors' in what follows), **distinguishing_nodes(attractors,att_index)**
finds the distinguishing nodes (i.e. nodes with unique values) between the reference 
attractor (identified by the "att_index" id) and all the other attractors in the list.

The algorithm tests combinations of increasing length of indices. 
For each combination, it compares the values of the selected entries in the reference vector 
with the same entries in all the other attractors. 
    
If the values are different for all the other vectors, 
then the current combination of nodes is a witness set, and the function returns the IDs of the selected entries.


**Related Repositories:**
* https://github.com/EnricoBorriello/AttAttach
