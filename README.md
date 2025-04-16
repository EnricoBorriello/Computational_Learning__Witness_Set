# Distinguishing Nodes in Binary Attractors

This repository contains a small collection of functions for calculating the witness set of ensembles of binary vectors.

Given a list of binary n-tuples (referred to as 'vectors' hereafter), the function **'distinguishing_nodes(vectors, index)'** identifies the distinguishing nodes—nodes with unique values—between the reference vectors (identified by the **'index'** ID) and all other vectors in the list.

The algorithm tests combinations of increasing lengths of indices. For each combination, it compares the values of the selected entries in the reference vector with the corresponding entries in all other attractors.
If the values are different for all other vectors, the current combination of nodes is considered a witness set, and the function returns the IDs of the selected entries.

The function **'avg_witness_set_size(vectors)'** simply calculates the average witness set size across the entire list of vectors.

The function **'distribution_parameters_fixed_r(n, r, sim)'** generates the distribution of average sizes of witness sets over an ensemble of **'sim'** simulations. Each simulation includes **'r'** binary vectors of length **'n'**. The output list includes:

* The number of vectors used in the simulations (**r**);
* The average of the values;
* The standard deviation of this average;
* The minimum value of the distribution;
* The maximum value of the distribution.

The **'r'** vectors are randomly selected from the list of all possible binary n-tuples. This guarantees no repetition and an equal likelihood of 0s and 1s over the whole set of vectors.


---

## 🧩 Functions

### `distinguishing_nodes(attractors, att_index)`
Finds a minimal combination of nodes that uniquely identifies the attractor at `att_index` compared to all others.

- **Input:**  
  `attractors` – List of binary vectors  
  `att_index` – Index of the target attractor

- **Output:**  
  Tuple of node indices that distinguish the selected attractor.

---

### `avg_witness_set_size(attractors)`
Computes the **average number of distinguishing nodes** (witness set size) across all attractors in the list.

- **Input:**  
  `attractors` – List of unique binary vectors

- **Output:**  
  Float representing the mean witness set size.

---

### `distribution_parameters_fixed_r(n, r, sim=100)`
Estimates the statistical properties of average witness set sizes for random sets of binary attractors.

- **Inputs:**
  - `n` – Length of each binary vector (number of nodes)
  - `r` – Number of attractors per simulation
  - `sim` – Number of simulation runs (default: 100)

- **Output:**  
  List containing:
  - `r` – Number of vectors used
  - Mean of average witness sizes
  - Standard deviation
  - Minimum and maximum values of the distribution

---

## Example Usage

```python
# Define some binary attractors
attractors = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 1]
]

# Find distinguishing nodes for attractor at index 0
distinguishing_nodes(attractors, 0)

# Calculate average witness set size
avg_witness_set_size(attractors)

# Run simulation on random 5-bit binary attractors
distribution_parameters_fixed_r(n=5, r=10, sim=100)
```
---



## Related Repositories
* https://github.com/EnricoBorriello/AttAttach

---


## Related Articles
* [E. Kushilevitz, N. Linial, Y. Rabinovich & M. Saks, *Witness sets for families of binary vectors*. 
J. Comb. Theory Ser. A **73**, 376–380 (1996).](https://www.sciencedirect.com/science/article/pii/S009731659680015X?via%3Dihub)
* [E. Borriello & B.C. Daniels, *The basis of easy controllability in Boolean networks*. Nat Commun **12**, 5227 (2021)](https://www.nature.com/articles/s41467-021-25533-3)
