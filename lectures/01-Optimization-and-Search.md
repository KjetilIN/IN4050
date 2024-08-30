# Book notes (chapter 9)

- All algorithms have some type of optimization
- There is no algorithm that guarantee to perform the best on every problem. This requires you to test multiple algorithms out. This is called to **No free lunch theorem**

The common problem is that we want to minimize a given function with a set of features. We need to take the derivative in respect to each element in the feature list. The derivative with respect to each feature - i.e each dimension - is called the gradient of the function noted with the following: 

```math
\nabla f(x) = (\frac{\partial f}{\partial x_0}, \frac{\partial f}{\partial x_1}, ... , \frac{\partial f}{\partial x_n})
```

This is the direction to to, therefore to find to local minimum, we need to move towards the opposite direction than the what the gradient is pointing to. 

We know to stop when the gradient is 0. Note that this is the local minima with no guaranties that this is the global minima. In some cases we also stop when the absolute value of a gradient is less than a given value epsilon(note epsilon could be any arbitrary value):

```math
|\nabla f| < \epsilon \\
\text{where } \epsilon = 10^{-5}
```

There is another concept that it can be useful to think about, which is the places that we can travel to without going up or down, i.e., the places that are at the same level as we are. The full set of places that have the same function value are known as **level sets** of the function.

## Line Search 

If we know what direction to move in, then we cal simply look in that direction. The mathematical notation is:

```math
x_{k+1} = x_k + \alpha_k P_k \\ 
```

- x: x_k is the current guess 
- Alpha_k: distance to travel in. Also known as step size 
- P_k: direction that we have chosen to move towards

Finding a good value for alpha k is expensive and is therefore estimated. Trust region is another way to estimate distance.

P k can be chosen in a lot of different ways. Greedy option is to move towards the minimum as fast as possible.



### Jacobian

We can also approximating the function at a point in terms of its derivate. This is where Jacobian is used. It is a two dimensional matrix 

```math
J(x) = \frac{\partial f(x)}{\partial x} = \left(\frac{\partial f}{\partial x_0}, \frac{\partial f}{\partial x_1}, \dots , \frac{\partial f}{\partial x_n}\right )
```

### Hessian Matrix

The matrix of second derivatives. (Three dimensional matrix): 

```math
H(x) = \frac{\partial}{\partial x_i}\frac{\partial}{\partial x_j} f(x) \\ 
.\\
H(x) = \nabla^2 f(x)
```

It is used to compute the Newton direction, which is the inverse of the Hessian matrix dot-product with Jacobian.  

## Least-Squares Optimization

When it comes to the least-squares error function to compute the cost. The studies on such problems have been worked on before by others. The objective function is 

### The Levenberg–Marquardt Algorithm

...

> [!WARNING]
> To be continued