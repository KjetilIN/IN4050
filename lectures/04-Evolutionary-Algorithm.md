# Lecture 17.september - Evolutionary Algorithms

- Natural selection: certain traits become more more common, due to their effect on the survival and reproduction

Key aspects:
- variations: individual have variations in traits 
- heritability: inherited traits
- differential survival and reproduction: some trait server survival and reproduction than others
- adaptation: populations become better adapted to their environment 


Biology background:
- dna and genes 


EA:
- Developed by John Holland.
- In nature very stochastic 
- Example: Boeing used it to optimize design of wing 
- It explores more space

1. Create population
2. Select parents with some probability that the best parents will be picked 
3. Recombine (crossover) to create offspring
4. Mutate the offspring (apply slight changes)
5. Use the best of population add offspring to repeat
6. Terminate when we hit a quality or termination condition is met


- The most time consuming part is the evaluation.
- Variation is then increased by recombining to get new entries 
- Then we only select a few, to push towards a better quality
- Its a balance between exploration and exploitation


Main components in more details:
- Represent the problem 
- Binary representation is small and lightweight. Could split up a sequence to represent different parts.
  - Array of 0s and 1s
- Gene: one element in the array
- Locus: index of the gene
- Allele: the value that a gene could have
- Genotype: a set of gene values
- Phenotype: what could be built/developed for.
  

Fitness function:
- Giving a solution a score
- Represents the task to solve
- Enables selection, and provide something for comparison


Population:
- candidate solutions 
- the population is evolving and not the individual 


Parent selection is usually probabilistic. 
- Stochastic nature can aid to escape local optima!!

Mutation:
- Arity 1: 
- Arity > 1: 
- Arity = 2: crossover
- Arity > 2:  
- Apply this simple random change to avoid a genotype 


Recombination: 
- merge from parents
- choice of information to merge is stochastic 
- Crossover by cutting at random place, and then combine the two parts to create a offspring 


Initialize and terminate: 
- Ensure a even mix of possible allele values when initializing 
- Termination can be some fitness



## Traveling salesman 

- For 30 cities (30-1)! = 10^31 possible tours
- Mutations might lead to a inadmissible solution 


## Summary:
- Lot of parameters can be used and modified over time 