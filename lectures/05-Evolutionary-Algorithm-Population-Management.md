# Lecture 24. september 

Partially mapped crossover: 
- important for adjacency between elements decides the quality 


Tips for lecturer: If you know discrete mathematics, statistics and linear algebra, then ML will be easy.

## 8-queens problem:
- Could use GA to solve
- C(64,8) possible combinations 
- Minimize the possible options by thinking that one queen per column. 

Solved with GA Here:
- Phenotype: a board configuration 
- Genotype: a possible mapping of numbers 1-8
- Fitness function: penalty ..
- Mutation: swap to ways
- Recombination with crossover: using one point. Solve conflicts.
- Selection: Pick five random and take best 2 for crossover
- Surviver selection: merge old and new. Throw out the 2 worst solution  


## Population management and more

- We want to preserve diversity 
- Two types of selection: parent and survivor selection  
- Selection Pressure: how much pressure is there for selecting the best solution 

Fitness-Proportionate Selection: 
- Probability for individual i to be selected is equal to the fitness of i divided by the sum of fitness of every other

Rank-Based Selection: 
- Select all based on relative fitness. 
- Rank the population based on selection probability on their rank
- Linear ranking: **s** is the parameter between 1 and 2 (2 inclusive).
  - Increasing S increased 
- Exponential ranking:
  - ...

Tournament Selection: 
- Randomly pick k members and then make them compete. 
- Repeat until we have the given amount of selections that we want
- higher k, higher selection pressure

Uniform selection:
- Parents are selected by uniform random distribution 


Fitness-based replacement - for example:
- Elitism 
- ....



### Multimodality - preserving diversity  

- Often we might want to have 



GA can be used for hyperparameter optimization 
- GA's are used to tune hyperparameter. 