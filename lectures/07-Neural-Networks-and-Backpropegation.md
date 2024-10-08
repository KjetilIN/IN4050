# Lecture 8.october 

- Very important lecture 
- Over-paramerized models: when there is a lot of parameters that needs to be tuned


## Neural Network 

### Artificial Neuron

- Weighted sum + bias. 
- Activation function that is non-linear 
- Activation function
  - Job: provide non-linearity to the input => we don't want a linear mapping 
  - Introduce non-linearity 
  - Should be differentiable => ?
  - Reduces weak signal 
  - Determines what fires the neuron 


Sigmoid activation:
- Suffer from gradient saturation

ReLu activation:
- Not differentiable in 0
- Define subgrades to be 1
- Inactive nodes to remain inactive 

LeakyReLu
- Allows negative numbers to have a small slope: min(0.01x, x)


### Network 

- A directed graph made from connected neuron 
- Can be also be recurrent 

Has input layer, hidden layers, and output layer 
- Layer index in the superscript notation of the activation 
- Neuron number from top down 
- The output is the same as the amount of classes to classify 
- A fully connected means that layer wise every node is connected to every node in the previous layer


Activation from a specific neuron in a layer: 

```math
a_k^{[l]}
```
k: neuron number
[l] : layer 


See slide 21 to see notation reference 

Input to layer L is output of activation layer L-1 

Matrix of weights for each layer 
- Each row corresponds to weights of a neuron in the layer


We can note the output like this:

```math
a_k^{[l]} = 
```

All weights and biases are trainable. 

At the end we want to turn the outputs to a prediction probability.
If we have multiple outputs, we use softmax 

.....

## Back propagation 

- Very computational effective of training a network 

### Gradient 

- Slope of each direction => n-dimensional function 

Training: 
1. Initialize weights
2. Compute gradient 
3. Update the weights by going to opposite direction of the gradient 
4. Continue until the gradient is small 

Computational complex: O(Nd) 
- d: number of parameters 
- N: sample count 

### Stochastic gradient decent
- Select only a set of samples
- Now computation is O(d)



You can calculate the number of parameters with:

Elementary operations needed for forward pass:


For one sample we need to compute in order of E^2 operations, which is too slow. 


### Forward pass
- go from layer to layer and get the activation until the end output layer => use softmax on the last layer



### Back propagation 

- Compute all partial derivatives with using order of E operations!
  - It reduces the number of operations 


For computing 
- If you know the z's, then we don't need to compute the previous layers to compute what follows

Using the chain rule to express the loss with respect to the weight: 

...

We know 


We cannot compute the delta in middle, we cannot do.
We start at the back. 

The formula for backpropagation for the current layer, we use the delta on the next layer.

We need order of 


# Stochastic Gradient Decent (mini batch)

Not all updates are good. 

Therefore we use a smaller batches.

....