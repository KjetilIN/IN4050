# Lecture 10.september - Perceptron and Linear Regression 

- Matrix multiplications can replace nested loops
- GPUs allows for high computing processing 

## Perceptron 

- Inspired by Psychology 
  - How humans think => hardware for replicating this
- Human brain has 10^11 neurons 
- A single neuron is simple, but the collections is useful. 
- Computers do compute much faster, but less efficient in other sense. 
- Hebb's rule: ...
- McCulloch and Pitts => neurons could correspond with logic
- The perceptron => Frank Rosenblatt 


Steps:
- A set of inputs
- A set of weights
- An adder
- An activation function: 0 or 1 


Activates on a threshold. 
Adjusting the fixed threshold - example: 
- left side should be one, then we know the weight 


The bias term:
- Used to adjust the threshold 
- Implicit assumption that your bias is included. 
- TODO: read more


Training perceptron:
- Based on target value t, was 1 or 0, 
- Adjust if target is not the output 
- Adjust up or down based on the 

Linear separability: of there is a feature such that data falls on one side or another

Perceptron Convergence Theorem: 
- If data is linearly separable, the perceptron will find the linear decision boundary 
- Unless learning rete is to large 
- There are many possible is solutions, some might be less robust


## Linear Regression

- We have input with well defined target values 
- In regression the target set is real numbers 
- We want to approximate a function that best fit all targets 
- We have an intuition that a linear model is enough 


Inductive bias:
- ...

Mean Square Error (MSE): 
- One way to measure performance 
- Imperical average. 
- We square it, because we take the actual value (not canceling out)
- Goal of minimizing the error

There are other variants of these: 
- SE, RSE, ++ 

The minimazation problem: 
- MSE is convex, ..