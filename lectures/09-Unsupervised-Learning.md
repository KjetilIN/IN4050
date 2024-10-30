# Lecture 22.oct - Unsupervised Learning 

Supervised learning: learn mapping between label and data
Unsupervised learning: learn the distribution of data

- There is no truth
- Result open to interpretation 

We are given the easy to measure feature. 
Why would be want to do this?
- Being able separate between two objects

For example, with a single feature, we might see that there are two groups. 
In 2D, (two features), we get groupings on the plane, also known as clusters.
- Very useful to represent data in 2D, by doing dimension reduction 

We could have a large number for features for the data as well. 
- Can be plotted by using features y axis, samples on x axis and color code features 

Evaluating the performance:
- No "truth" to compare with
- Performance more to interpretation
- Often we can still implement a loss function to determine which of two solutions is best

## How to generate similar data?

- We want a model that is able to create data similar to the training data set. 
- Validation: compare distribution of training data to the new data

Density function: where the area under curve is 1
- Probability of an event is the area under the curve. 
- We use a P(x in [a, b]) to find the probability 
  - Note that we cannot do P(a) since that will be 0 or the density value (which is not probability)
- Density function can describe the probability of all events on axis 
  - Can use 1D or 2D features => then the last axis will be the density

Learning a density:
- Histogram 
  - Split the space into a number of cells, then count entries in the cell 
- Smooth density estimator: kernel density estimator  
  - Define a kernel function $K(x)$ => works as a "0-detector"
  - Compute the value of $K(\frac{x-x_i}{h})$, this detect if the X is close to any of the training data 
  - Finally add all the detector values by $f(x) = \frac{1}{nh}K(\frac{x-x_i}{h})$
- GAN

## How are data are grouped?

- Known as clustering 
- Hierarchical cluster
  - Cluster in form of a three
  - Connect clusters by horizontal lines 
  - The result is not a single cluster but hierarchical clusters
  - Hight between clusters connection tell how far apart the different samples 
  - Created by
    - Make each sample be its own cluster
    - Fund two cluster that are closest to each other
    - Then repeat until there is only one cluster left 
  - We must keep track of the history 
  - Distance are also known as linkage methods
    - Single linkage => smallest distance between a sample from each cluster  
    - Average linkage => average distance between all samples from each cluster 
    - Complete linkage => use the maximum distance between a sample from each cluster
    - Ward linkage => merge two clusters and see how the cluster variance from last 
    - For distance between to samples we can use:
      - Manhattan distance
      - Euclidean distance
      - Cosine distance  
  - k-means clustering 
    - Set k clusters
    - Assign to nearest cluster center
    - Calculate new cluster centers
    - Repeat until it converges 

## How to compress the data?



## How to visualize the data in low dimension?
