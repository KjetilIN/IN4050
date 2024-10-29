# Lecture 29.oct - Deep Learning Networks 

## Deep Learning 

- At least two hidden layer 
- Often a more specific architecture
- Deep Learning breakthrough
  -  Alex Net
    - 16% error rate 
  - Speech recognition 
    - Was no early in 1990s, but after 2015 it worked better in CNNs
- NNs succeeded by having better models, data, and better machines. 
  - GPU was important 

Fully connected: weights from each input node to all nodes in the next layer. A connection to every node in the next layer

Weight matrix to each layer 

Vanishing gradient problem: 
- When input is large, the activations becomes 1.
- Gradients becomes 0, which will lead to no update or slow update
- Activation function matters
- ReLU is preferred


## CNNs 

For image tasks, we use multidimensional arrays. 
- Rows, columns and channels for the image,
- m x n x 3

Each point is one pixel in the image on the color channel
Node for each point in the network 

What happens if we rotate the image, or location changes?
- We should learn the features such that this does not matter 

Simplicity explanation of CNN:
- Classify a feature in an image, may be an pattern 
- Images are 20x20 pixels (black and white)
- We focus on the sub-picture, by having a kernel to slide over the image
  - We can image that we find a pattern when we find a sub-picture that fit the kernel
- In the example, a 5x5 kernel is big enough to see the feature 
- With the kernel we say we do convolution 
- The result is new nodes: one node represent one convolution over the image
- Weights are shared
- There is 5x5 edges from the convolution result to the 5x5 pixels in the original image

Kernel = filter

A single filter is not enough for learning complex tasks. 
By using several layers to learn more and more complex patterns.
We can image it works like this: 
1. Simple patterns
2. Lines, Curves
3. Contours
4. Figures
5. Features (figures but are more important for the classification)

Last we use the combination of features to classify a class!!


Filters are learned by backprop 

There are two types of layers:
- Convolutions
  - Does convolution with the kernel as matrix
- Pooling 
  - Down sampling by using pixels in a area
  - Max-pooling: takes the maximum of an area 
Key Ideas: 
- Less parameters
- Parameter sharing 
- Find localized patterns over all input tensors

Cool questions: 
- How many layers?
- How many nodes?
- The relationship between layers?


## RNN - Residual Neural Network 

- Loop of the same weights applied multiple times
- The state changes for each loop
- Repeat V times (?)

```math
h_t = g(h_{t-1}U + x_tW) \\
y_t = f(h_tV)
```

- g and f is some activation 
  - f is often softmax 

- RNN as Language Model
  - Predict next word by recurring 


Embeddings: mathematical representation of similarity as a vector (with a fixed dimension)
- one-hot-encoding for a word is not that smart, because its size would be 
- Therefor we represent it as vector in N-space
- LLM learning is learning the embeddings 