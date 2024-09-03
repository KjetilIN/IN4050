# Lecture 3.sep 2024

- Machine Learning is the study of computer algorithms that improve automatically through experience

Three types of ML: 
- Supervised learning => learn for labeled data
- Unsupervised learning => no data and tasked to identify similarities
- Reinforcement learning => training with reward systems


## Supervised learning

Given training data that is labeled, train on it, and predict label on unseen data. 


### Classifier
- A domain of object/input that we are to classify
- Labels: a finite set of labels
- Classifier: a mapping which maps each object to ...

F.eks: MNIST
Domain: handwritten digits
Labels: number 0-9 


You can classify one or more classes


### Feature

A set of attributes that we can use to observe.
Based on the domain knowledge you select the features needed, and pick useful features.

The task becomes to predict based on the set of features,

This course will mainly use pre-made datasets. The focus wil be pn algorithmic and experimental. 

Types: 
- Numerical => discrete or continuous set set  
- Categorical 

You might want to transform categorical data to numerical data.

You make them a vector of inputs:

```math
x = (x_1, \dots, x_n)
```

Consider we have a classification: 
```math
x \rightarrow y
```

TODO: finish
...


### Structure 

O: observations
L: Labeled set 

TODO: finish


### Training 

- Split data into training and test set.  
- Split 80/20 
- Train on train set, test set is not used 
- Test set will give you a measurement for performance of the data
- Also reasonable with development set
  - Develop set will tell you what the test data will do, so we can use it to improve the data'


### Confusion Matrix
- Goal: evaluate classifier. 

Accuracy = (tp + tn) / N
tp: true positives
tn: true negatives
N: number of samples

With more than two classes?: 
- Matrix with predicted and true label
- Sum of diagonal divided by number of samples 



### K Nearest Neighbors algorithm 

- Clustering algorithm
- Choosing K matters a lot
- Distance estimation with euclidean distance
  - Also matters 
- Increasing K might increase the performance 
  - Large K is more general 
  - Smaller K fits the data more, but this might overfit to the data
- Binary classifier with odd k always reach a decision 
- Might be draw when there is a draw, therefor odd K might be a good idea

### Scaling axises: 
- Important for the distance 
- Scale per axis
- Two scales with the same range could give more tightly coupled datasets
- Scaling does not guarnty 


#### Max Min Scaling 

- N training sets 

TODO: 

#### Normalizing 

- TODO: write about