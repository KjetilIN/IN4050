# Lecture 1.okt 

For a multi-class image classification task:

Goal: for an image label $(x,y)$ pair drawn from a unknown distribution, find a classifier $h \ell H$ with a minium misclassification probability:

$$
add 

$$

## Empirical Risk Minimization (ERM)

h is some classifier 

$$
h_w : X \to Y
$$

You need a loss function, that explains how well the model is doing
Typical loss functions:
- Logistic loss:
- Quadratic loss: 
- Hinge loss => maximizes the margin for the support vector machines 


## Classification 

- For each image predict the class
- Binary classification 
- Idea: apply a linear mapping and classify the according to the sign of the output

$$
h_w(x) = x^T w, f_w(x) = sgn(h_w(x))
$$

- The output would be between -1 or 1, because of the sign activation function. 
- If we know the $h_w(x) \approx 0$, we are uncertain of the classification
- Else, when its far away from the decision boundary we are much more certain.

We get this information on certainty.

Instead of sign: we create a mapping between 0 and 1. This will be the output of the model. 


- Need CDF, with a medium of 0 

Most known are the sigmoid: 

$$
s(u) = \frac{1}{e^{-u} + 1}
$$

Sigmoids can also have a variable C. 


## Logistic Regression 

Linear mapping into a sigmoid 

Output: the predicted probability of correct value

Interpret 

TODO: review 


Minimizing the weights is the same ass cross entropy loss of out data points. -log of the probability is the .................


Cross-entropy loss: 


One hot labels: 



## Multi-class Classification 

- Still a discrete set of classes, but more than two classes
- For each observation, set one label for the set C


- The values cannot be in a range from 1-N for each output. This could lead the element to be between two elements. 
- You want instead instinct values for each, and they are not connected: 
- Solution: one-hot-encoding, where you have a vector of 0s and a single 1 for the given type. This makes them not encoded together. 


### Multi-label to multi-class

Label version:
- Make N classifier for classifying N labels 
- One vs rest: each classifier focuses on itself
  - Problem: space is not patrician correctly
  - Solution: choose the class with highest probability 