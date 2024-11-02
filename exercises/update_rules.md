# Machine Learning Algorithms Update Rules Cheatsheet

## 1. Perceptron
### Scalar Form
* Prediction: $\hat{y} = \text{sign}(w^T x + b)$
* Update Rule: $w \leftarrow w + \eta(y - \hat{y})x$
* Bias Update: $b \leftarrow b + \eta(y - \hat{y})$

### Matrix Form
* Prediction: $\hat{Y} = \text{sign}(XW + b)$
* Update Rule: $W \leftarrow W + \eta X^T (Y - \hat{Y})$
* Bias Update: $b \leftarrow b + \eta(Y - \hat{Y})$

## 2. Linear Regression
### Scalar Form
* Prediction: $\hat{y} = w^T x + b$
* Gradient: $\nabla w = -2x(y - \hat{y})$
* Update Rule: $w \leftarrow w - \eta\nabla w = w - \eta(-2x(y - \hat{y}))$
* Bias Update: $b \leftarrow b - \eta(-2(y - \hat{y}))$

### Matrix Form
* Prediction: $\hat{Y} = XW + b$
* Gradient: $\nabla W = -2X^T(Y - \hat{Y})$
* Update Rule: $W \leftarrow W - \eta\nabla W = W - \eta(-2X^T(Y - \hat{Y}))$
* Closed Form Solution: $W = (X^T X)^{-1}X^T Y$

## 3. Logistic Regression
### Scalar Form
* Prediction: $\hat{y} = \sigma(w^T x + b)$ where $\sigma(z) = \frac{1}{1 + e^{-z}}$
* Loss: $L = -[y \log(\hat{y}) + (1-y)\log(1-\hat{y})]$
* Update Rule: $w \leftarrow w - \eta(\hat{y} - y)x$
* Bias Update: $b \leftarrow b - \eta(\hat{y} - y)$

### Matrix Form
* Prediction: $\hat{Y} = \sigma(XW + b)$
* Loss: $L = -[Y\odot\log(\hat{Y}) + (1-Y)\odot\log(1-\hat{Y})]$
* Update Rule: $W \leftarrow W - \eta X^T(\hat{Y} - Y)$
* Bias Update: $b \leftarrow b - \eta(\hat{Y} - Y)$

## 4. Multi-layer Perceptron (Single Hidden Layer)
### Forward Pass
* Hidden Layer: $h = \sigma(W_1x + b_1)$
* Output Layer: $\hat{y} = \sigma(W_2h + b_2)$

### Update Rules
* Output Layer:
  * $\delta_2 = (\hat{y} - y)\odot\sigma'(W_2h + b_2)$
  * $W_2 \leftarrow W_2 - \eta\delta_2h^T$
  * $b_2 \leftarrow b_2 - \eta\delta_2$
* Hidden Layer:
  * $\delta_1 = (W_2^T \delta_2)\odot\sigma'(W_1x + b_1)$
  * $W_1 \leftarrow W_1 - \eta\delta_1x^T$
  * $b_1 \leftarrow b_1 - \eta\delta_1$

## 5. Neural Network (General Case)
### Forward Pass
For each layer $l$ from 1 to $L$:
* $z^{[l]} = W^{[l]}a^{[l-1]} + b^{[l]}$
* $a^{[l]} = g^{[l]}(z^{[l]})$ where $g$ is the activation function

### Backpropagation
For output layer $L$:
* $\delta^{[L]} = \nabla a_L\odot g'^{[L]}(z^{[L]})$
* $\nabla W^{[L]} = \delta^{[L]}(a^{[L-1]})^T$
* $\nabla b^{[L]} = \delta^{[L]}$

For hidden layers $l = L-1$ down to 1:
* $\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]}\odot g'^{[l]}(z^{[l]})$
* $\nabla W^{[l]} = \delta^{[l]}(a^{[l-1]})^T$
* $\nabla b^{[l]} = \delta^{[l]}$

### Update Rules
For each layer $l$:
* $W^{[l]} \leftarrow W^{[l]} - \eta\nabla W^{[l]}$
* $b^{[l]} \leftarrow b^{[l]} - \eta\nabla b^{[l]}$

## Common Notation:
* $w, W$: weights (scalar and matrix form)
* $b$: bias
* $\eta$: learning rate
* $x, X$: input features (scalar and matrix form)
* $y, Y$: true labels
* $\hat{y}, \hat{Y}$: predicted labels
* $\sigma()$: sigmoid activation function
* $\odot$: element-wise multiplication
* $^T$: matrix transpose
* $L$: loss function
* $\nabla$: gradient operator