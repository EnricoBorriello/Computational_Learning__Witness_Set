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

**distribution_parameters_fixed_r (n, r, sim)** generates the distribution of average sizes of witness sets over an
ensembles of **sim** simulations. Each simulations includes **r** binary vectors of length **n**. 
The output list includes: 

* The number of vectors used in the simulations (r).
* The average of the <|w|> values.
* The standard deviation of this average.
* The minimum value of the distribution.
* The maximum value of the distribution.

The r vectors are randomly selected from the list of all possible binary n-tuples. This guarantees no repetition, and 
an even likelihood of 0s and 1s over the list.

**Related Repositories:**
* https://github.com/EnricoBorriello/AttAttach

**Related Articles:**
* E. Kushilevitz, N. Linial, Y. Rabinovich & M. Saks, *Witness sets for families of binary vectors*. 
J. Comb. Theory Ser. A **73**, 376–380 (1996).
(https://www.sciencedirect.com/science/article/pii/S009731659680015X?via%3Dihub)
* [E. Borriello & B.C. Daniels, *The basis of easy controllability in Boolean networks*. Nat Commun **12**, 5227 (2021)](https://www.nature.com/articles/s41467-021-25533-3)
