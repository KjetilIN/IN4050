# Lecture 15.october - Supervised learning tips and tricks 

- models selection 
- evaluations
- bias-variance tradeoff


Why evaluation?
- Performance on the training data is not a good indication of performance on future data, because it does not show generalization rules

Overfitting: 
- fitting the training data to precise
- also known as "memorizing the training data"
- will perform badly on new data


Underfitting:
- the model does not fit training data well

We need to pick a model that pick the lowest generalization data.
- That is why we split the data into test, train and validation 
- Validation data: used for hyperparameter tuning 


## Cross validation: 
- split the data into k subset
- test on each subset in turn 
- Remaining for training 
- Get performance
- Repeat K times
- Use the average of the scores 
- Different variations of cross validation
  - Leave-One-Out => k = number of data points
  - Repeated k-fold => k is the number of times we train the model
  - Nested k-fold => 


For large data, we don't really need cross validation, but it is very 



## Confusion matrix:
- True positive: we predict positive and it was positive
- True negative: we predict negative and it was negative
- True pos and True neg. on the diagonal 
- Style:
  - Did we predict correctly: True/false 
  - What we have predicted: Positive/negative 
  - This is what is combined 

Evaluation of matrix:
- Accuracy: true predictions over all predictions
- Precision: correct positive predictions. Focus on false positives
- Recall: true positive rate. Focuses on false negatives 
- F1-Score: balance between precision and recall 


## ROC Curve
- True positive rate on y axis
- False Positive rate on x axis
- Curve 
- Area under the curve represents the performance of the model 
  - A good model has a ROC curve where area is 1 (bad has lower area)


ROC Created by:
- Make predictions on the trained model
- Order all the scores
- Select a thresholds
- For each threshold
  - Calculate ...
  - Plot point

The random model has AUC of 0.5
- lower than 0.5 means that the model is worse than chance, but still the model is better than random because you can negate the values.

ROC curve can be misleading optimistic, by predicting the majority class correctly 

In unbalanced dataset, the FPR can remain low even when the classifier performs poorly on the minority class 

## Bias invariance: 
- Salary prediction model
- Model such as linear regression model is not able to train
- High-bias: setting to many assumptions for the model
- Low-bias: too flexible data, and are not able to capture the relationship of the data 
- Low variance: sum of squares are very similar for different datasets
- High variance: vastly difference for the sum of squares 
- The difference in fits are called variance 

A balanced model between variance and bias

Bias-variance tradeoff: 
- We will not be able to find the identical function that we are looking for 
- Two types of errors: 
  - Bias error:
    - Systemically misses target 
    - Under fitting
    - Train more or increase model complexity 
  - Variance
    - Picking up noise and being too sensible to small variation
    - Over fitting  
    - Use regularization or introduce more data 
- The model is optimum when you find the balance between variance and bias 


## Regularization 

Simples model is the best model. (Not introduce extra complexity without need)
We try to reduce the complexity of the model. 

- Two types of regularization 
    - Explicit regularization 
      - introducing a term to the optimization problem 
      - reducing the size of parameters
    - Implicit regularization 
      - Early stopping
      - Add more data
      - Feature selection 
      - Drop selection 


Does adding more data help?
- Likely to help with high variance 
- But not for bias, because..

Does feature selecting help?
- Maybe selecting only some features will remove noise from the problem
- all features + insufficient data => overfitting 
- The selected features can do the task 

A complex model with create a complex curve, when the problem itself can be simple!
- Meaning that a simple prediction model performs better

By adding a regularization term lambda, which is a new hyper parameter. 
- Used to balance 

Ridge regularization:
- Small lambda is when we don't have a regularization problem
- Most used are L2-distance => sum of squared coefficients
- Keeps all features, but reduces the size of them to be almost zero(so that least important features are reduced to very small number)

Lasso Regularization:
- Uses L1 
- Sum of absolute values of coefficients 
- Useful for feature selection 
- Retain only the most relevant features 

Elastic nets: 
- Combine L1 and L2
