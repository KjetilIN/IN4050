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


# Book Notes chapter 10. 

- Cherry pick evolution concepts to make an efficient learning method. 
- Want the fitter organism 
- GAs model sexual reproduction 
- Randomness as mutation from parent
- Usually a set of parameters that is hard to set and crucial to the algorithm 
  

### GA

Computational approximation to how evolution performs search.
This is done by producing modifications of the parent genomes in their offspring and thus producing new individual new fitness. 

We need:
- A method for representing problems as chromosomes
- A way to calculate the fitness of a solution 
- A selection method to choose parents 
- A way to generate offspring by breeding the parents 

NP-complete: 
NP is the set of all decision problems (questions with a yes-or-no answer) for which the 'yes'-answers can be verified in polynomial time (O(n^k) where n is the problem size, and k is a constant) by a deterministic Turing machine. Polynomial time is sometimes used as the definition of fast or quickly.
(In simple terms: NP-problems is computational impossible to bruteforce as N increases)


#### Knapsack problem (variation from book):

Suppose that you are packing for your holidays. There is little room in your bag. There is a set of things that you are required to bring, and a set of items that you want to bring. Everything will not fit. You must find a way to fit the bag with as much items as you can, to get the best value out of the flight.


A greedy algorithm will take the most valued item at each step, but this will not lead to an optimal solution. 


#### GA: representing problems as chromosomes

Goal: represent a possible solution 

We need to encode a possible solution. We can do this by finding a way to encode descriptions of the solution as a single solution. For example: use a string to represent a solution. 

For the Knapsack problem, we can make the string as long as the amount of items available. Then have each item be 0 or 1 if we brought that string. We can also use bits (where the amount of bits is the amount of items), which makes it take less memory. The binary value at each point would represent if we brought that item or not. (Note: that we might include a solution that is not even possible to do)

#### GA: Evaluating fitness 

Goal: evaluate the solution 

For the Knapsack problem, it would take the possible solution and return a value for that string. 
We want the bag to be as full as possible. Therefor we need to know the volume for each item, and we use that to calculate the value for the solution 


### GA: Population 

Goal: create random solutions to initially start using. 

In numpy we can use the `np.random.rand` and `np.where` to create the initial population. 


### GA: Parent selection

Goal: from the population, choose random parents.

There are three strategies for selecting the solutions.

- Tournament Selection: Take four string from the population and choose the to most fittest
- Truncation Selection: Pick a x% of the best solutions. Usually with this strategy 50% is picked. 
- Fitness Selection: Select solutions at a probability, with the probability being selected by a proportion of its fitness.

```math
p^{\alpha} = \frac{F^{\alpha}}{\sum_{\alpha'} F^{\alpha'}}
```

Where:
- $F^{\alpha}$ is the fitness
- $p^{\alpha}$ is the probability 

Problem: the fittest solution will have the same probability as the rest. Therefore we can add more entries of the best solutions to the pool of options. 


### GA: Generating offspring, and selecting a new population 

To create offsprings, we need to combine to solutions into a single solution. Again, many strategies to choose from here. 

Crossover:
- We find a single point to split both solutions into two
- Then we make the new solution by taking one part of the first solution and one part of the second solution 
- This option might lead to a lot of invalid solutions. For example in Traveling salesmen problem, it might create a route that is not valid. 

Mutation: 
- Change som values in the solution by some probability p. Often $p\approx \frac{1}{L}$ where L is the length of the solution (amount of descriptors). This lead to one mutation in each solution.
- We do not want to mutate a lot. This will avoid moving away from a solution that works. 

At this stage we have new solutions and their parents. What do we do now? Replacing parents by children could lead to replacing a good solution by a bad. We avoid this by elitism.

Elitism: 
- Take som number of the best solutions from the children
- Put them in the population, by replacing at random, or replace parents with smallest fitness.

This encourages premature convergence, and the algorithm might take the best every time and not explore enough. This could lead to some solutions being never able to discover. The randomness is why GA works so well. To fix this we could use niching.
- Split the population into separate sub-populations, and let them evolve individually 
- This makes the them able to converge at different local maximum

There is also other solutions to solve this problem. 


### Punctuated Equilibrium 

When GAs run for a while, the fitness over time will flatten out. It turns out that if we run it long enough, a solution might modify something is such a way that allows us move in a direction that allows for new modifications such that the fitness grows again! 

This is true in evolution also, but the changes happens over 100-1000 years, and then it flattens out again. This is the problem with GAs. It might take a lot of time before it is able to move out of the local maxima. It is also hard to analyze a GA. 


GA could help choose a topology of a neural network. There are then a set of allowed:
- Delete a neuron
- Delete a weight 
- Add a neuron 
- Add a connection 


### Genetic programming
- Representing programming: using threes to represent a program.
- For example represent a arithmetical threes. 