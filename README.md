# Witness-Set
This repository collects a small collection of functions to calculate the witness set of ensembles of binary vectors.

Given a list of binary n-tuples (for simplicty 'vectors' in what follows), **distinguishing_nodes(vectors,index)**
finds the distinguishing nodes (i.e. nodes with unique values) between the reference 
vectors (identified by the "index" id) and all the other vectors in the list.

The algorithm tests combinations of increasing length of indices. 
For each combination, it compares the values of the selected entries in the reference vector 
with the same entries in all the other attractors. 
    
If the values are different for all the other vectors, 
then the current combination of nodes is a witness set, and the function returns the IDs of the selected entries.

The function **avg_witness_set_size(vectors)** simply 
calculates the average witness set 
across the entire list of vectors.



 distribution_parameters_fixed_r (n,r,sim=100):
    
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






**Related Repositories:**
* https://github.com/EnricoBorriello/AttAttach

**Related Articles:**
* ...
* [E. Borriello & B.C. Daniels, *The basis of easy controllability in Boolean networks*. Nat Commun **12**, 5227 (2021)](https://www.nature.com/articles/s41467-021-25533-3)
