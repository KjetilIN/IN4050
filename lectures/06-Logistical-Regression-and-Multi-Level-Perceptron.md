# Lecture 1.okt 

For a multi-class image classification task:

Goal: for an image label $(x,y)$ pair drawn from a unknown distribution, find a classifier $h \in H$ with a minium misclassification probability:

$$
\min_{h \in H} Pr(h(x) \neq y)
$$

## Empirical Risk Minimization (ERM)

ERM is a principle in statistical learning theory which defines a family of learning algorithms based on evaluating performance over a known and fixed dataset. 

h is some classifier 

$$
h_w : X \to Y
$$

You need a loss function, that explains how well the model is doing
Typical loss functions:
- Logistic loss: 
  - $\ell (h_w(x), y) = log(1+e^{-yh_w(x)})$
- Quadratic loss: 
  - $\ell (h_w(x), y) = ||y - h_w(x)||^2_2$
    - Notation note: stands for 2-norm, also known as euclidean norm
- Hinge loss
  - maximizes the margin for the support vector machines 
  - $\ell (h_w(x), y) = \max (0, 1-yh_w(x))$


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

Linear mapping into a sigmoid:

$$h_w(x) = x^Tw$$ 

Into sigmoid it becomes:

$$
s(h_w(x))= \frac{1}{e^{-x^Tw} +1}
$$

Then the output becomes between 0 and 1 inclusive. 

Output: the predicted probability of correct value

$$
\^p_w(1|x) = s(h_w(x)) = \frac{\exp(x^Tw)}{1 + \exp(x^Tw)} \newline

\^p_w(-1|x) = 1 - s(h_w(x)) = \frac{1}{1 + \exp(x^Tw)} \\

$$

Output: $\left[\^p_w(-1|x), \^p_w(1|x)\right]^T$

For training example $(x_n, y_n)$, then the loss function becomes:
 $\ell_n(w) = -\log(\^p_w(y_n|x_n))$

To have a smaller loss, give higher probability to true label. 


## Cross-entropy loss

For the data point $(x_i, y_i)$, the loss is defined as: 
$$
\ell_i(w) = -y_i\log(s(h_w(x_i)) - (1-y_i)\log(1-s(h_w(x_i))))
$$

For one hot labels: 

$$
\ell_i(w) = 
\begin{cases} 
    -\log(s(h_w(x_i))) & \text{ if } y_i = 1 \\
    -\log(1 - s(h_w(x_i))) & \text{ if } y_i = 0
\end{cases}

$$


To note: 
- Logistic regression is a method for classification problem
- Apply sigmoid to a linear mapping
- Output can be interpreted as the predicted probability $\^p_w (y_i|x_i)$
- Cross-entropy loss derived by maximum likelihood estimation of w
- Cross-entropy loss is the sum of the negative logarithms of the predicted probabilities weighted by the ground-truth distribution
- For one-hot labels, the negative logarithm of the predicted probability of the ground-truth class



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

### Multi-Class Classification

- Each node has its own connections 
  - Column in the weight matrix is a set of weights connected to a single node
  - A row in the weight matrix is a set of weights connected to a list of nodes 

Multi-label perceptron: 
- N output nodes that all are used to classify their own thing
- Each set of weights are connected to that node - i.e when we update the weights for a output node, then we don't interfere with the other nodes. 
- Could have described the system as n independent binary perceptions!
- Use **argmax** to find the max value for each output note. When it does not match, we use the same update rule as perceptron 

### Multi-output linear regression 

- Using the MSE as loss function 
- Again the same as using a set of independent models

## Multinomial Logistic Regression

- Apply softmax-function S, to the output: 

$y_j = (S(z_1, \dots, z_n))_j = \frac{e^{z_j}}{\sum_{k=1}^n e^{z_k}}$

Note the following : 
- sum of output y is equal to 1
- A probability distribution is created 


### Training of Multinomial Logistic regression with cross-entropy loss

$$
L_{CE}(y,t) = - \sum_{j=1}^n t_j \log y_j = -log y_s
$$

Goal is to find $\frac{\partial}{\partial w_{i,j}}L_{CE}(x,t,w)$ for all weights. Result is simple: 

$$
\frac{\partial}{\partial w_{i,j}}L_{CE}(x,t,w) = (y_j-t_j)x_i
$$