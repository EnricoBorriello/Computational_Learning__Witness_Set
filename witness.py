import numpy as np
import itertools
import random

def distinguishing_nodes(attractors,att_index):

    """
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
    """
    
    # Initial check: attractors are all distinct
    if len(np.unique(attractors, axis=0)) == len(attractors):
        
        # "att_index" is the index of the attractor 
        # for which we want to find distinguishing nodes.
        selected_attractor = attractors[att_index]
    
        # We then creates a list of the "remaining_attractors"
        remaining_attractors = attractors[:att_index] + attractors[att_index+1 :]

        num_diff = 0
        comb_len = 0
        while num_diff != len(remaining_attractors):
            comb_len = comb_len +1
            #print 'trying comb_len = '+str(comb_len)
            comb = list(itertools.combinations(range(len(attractors[0])),comb_len))
            possibilities = len(list(comb))
            comb_index = 0
            while num_diff != len(remaining_attractors) and comb_index < possibilities:
                selected_nodes_values = [selected_attractor[i] for i in list(comb)[comb_index]]
                num_diff = 0
                for other_attractor in remaining_attractors:
                    other_nodes_values = [other_attractor[i] for i in list(comb)[comb_index]]
                    num_diff = num_diff + int(selected_nodes_values != other_nodes_values)
                if num_diff == len(remaining_attractors):
                    #print 'delta = '+str(comb_len)
                    #print 'distinguishing nodes: '+str(comb[comb_index])
                    return comb[comb_index]
                else:
                    comb_index = comb_index + 1
    else:
        return print('The list of attractors includes repeated arrays.')


def avg_witness_set_size(attractors):
    
    """
    The "attractors" argument is expected to be a list of attractors. 

    The purpose of the function is to calculate the average 
    delta value for all attractors in the list. 
    Delta is defined as the number of distinguishing nodes 
    for a given attractor, which is the number of nodes that 
    have different values between that attractor and all other attractors.

    The function first initializes an empty list named "delta". 
    It then iterates through all the attractors in the "attractors" 
    list using a for loop.

    For each attractor, the function calls the "distinguishing_nodes" 
    function to determine the number of distinguishing nodes 
    for that attractor. It then appends the delta value to the "delta" list.

    After iterating through all the attractors, the function returns 
    the average of all delta values using the "np.mean" function. 
    """
    
    # Initial check: attractors are all distinct
    if len(np.unique(attractors, axis=0)) == len(attractors):
    
        w = []
        for i in range(len(attractors)):
            w_i = len(distinguishing_nodes(attractors,i))
            w.append(w_i)
        return np.mean(w)
    
    else:
        return print('The list of attractors includes repeated arrays.')


def distribution_parameters_fixed_r (n,r,sim=100):
    
    """
    The function takes three parameters:

    n = The number of the binary n-tuples.
    r = The number of such n-tuples.
    sim = The number of simulations to perform. (The default value is 100 if not provided.)
    The avgd_dist list is initialized to store the average deltas for each simulation.

    In each simulation:

    r n-tuples are randomly selected from the list of all possible binary n-tuples (also 'vectors in the following').
    The function "avg_witness_set_size" is used to calculate the average witness set size of these r vectors.
    After all the simulations are completed, the function returns the following parameters of the distribution of
    <|w|> values:

    The number of vectors used in the simulations (r).
    The average of the <|w|> values.
    The standard deviation of this average.
    The minimum value of the distribution.
    The maximum value of the distribution.
    """
    
    avgd_dist = []
    tuples = list(itertools.product(*[(0, 1)] * n)) 
    for _ in range(sim):
        attractors = random.sample(tuples,r) 
        avgd = avg_witness_set_size(attractors)
        avgd_dist.append(avgd)
    return [r,np.mean(avgd_dist), np.std(avgd_dist), min(avgd_dist), max(avgd_dist)]




