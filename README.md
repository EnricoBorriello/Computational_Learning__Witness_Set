# Witness-Set
A collection of functions to calculate the witness set of ensembles of binary vectors.


Given a list of attractors, "attractors", 
    find the distinguishing nodes (i.e. nodes with unique values) between the reference 
    attractor (identified by the "att_index" id) and all the other attractors in the list.
    
    The "attractors" argument is expected to be a list of binary lists. 

    To find the distinguishing nodes, the function starts with a combination 
    length of 1 and iterates over all possible combinations of nodes. 
    It then compares the values of the selected nodes in the reference attractor 
    with the same nodes in all the other attractors. 
    
    If the values are different for all the other attractors, 
    then the current combination of nodes is the distinguishing nodes 
    and is returned by the function.

    The function continues to increase the combination length 
    and repeats the process until it finds the distinguishing nodes 
    or exhausts all possible combinations. 
    If it exhausts all possible combinations and cannot find distinguishing nodes, 
    it will return None.
