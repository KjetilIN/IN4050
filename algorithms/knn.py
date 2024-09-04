# K-Nearest Neighbor (KNN) Algorithm Implementation in Python
# 
# This script implements the K-Nearest Neighbor (KNN) algorithm, a simple yet powerful 
# supervised learning technique used for classification and regression tasks. 
# The KNN algorithm classifies a new data point by finding the 'K' most similar instances 
# in the training data and making predictions based on the majority class among those instances.
#
# The algorithm's simplicity, effectiveness, and non-parametric nature make it widely used 
# in various applications, including pattern recognition, data mining, and computer vision.
#
# For a detailed explanation of the KNN algorithm and its use cases, refer to this article: 
# https://dugamakash.medium.com/lets-learn-knn-182045ca1e00
#
# Author: Kjetil Indrehus
#

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np 
import random 

# This function will be used to generate random points  between a given max and min value
MIN_VAL = 0
MAX_VAL = 100

# We are going to be classifying two clusters.
# We assume that this is a real dataset
NUM_CLUSTERS = 2

# Randomize how many points per cluster 
POINTS_PER_CLUSTER = random.randint(20,70)

# We randomize the spread of the cluster 
CLUSTER_STD_DEV = random.randint(5,15) 


# This function is going to generate a random cluster center point 
def generate_random_cluster_center() -> tuple:
    cord = random.randint(MIN_VAL, MAX_VAL)
    return (cord, cord)


def generate_point(cluster_center: tuple, class_label: int) -> tuple:
    # Generate x and y coordinates using a normal distribution around the cluster center
    x = int(random.gauss(cluster_center[0], CLUSTER_STD_DEV))
    y = int(random.gauss(cluster_center[1], CLUSTER_STD_DEV))
    
    # Return the point with its class label
    return (x, y, class_label)


# This next function will be used to generate a random set of points 
def generate_points(amount_per_class) -> list[tuple]:
    # Generate cluster centers
    cluster_centers = [generate_random_cluster_center(), generate_random_cluster_center()]

    # Iterate through each cluster center and generate the point 
    result = []
    for class_label, cluster_center in enumerate(cluster_centers):
        for _ in range(amount_per_class):
            result.append(generate_point(cluster_center, class_label))
    return result


# We also need a function for calculating the distance between two points
def euclidean_distance(point1, point2) -> int:
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[2])**2)


# K Nearest Neighbor 
def kNN(k, points) -> list[list[tuple]]:
    # List of classes 
    classes = []

    # Iterate through all points 
    for point in points:
        # Calculate the distance from current point to all other points 
        distances = []
        for other_point in points:
            if point != other_point:
                # Append the distance with the class of the other point 
                distance = euclidean_distance(point1=point, point2=other_point)
                distances.append((distance, other_point[2]))

        # Sort by distances 
        distances.sort()

        # Take K amount of points that is the closest (smallest distance)
        k_nearest = distances[:k]

        # Do class voting on the majority 
        class_votes = {}
        for (_, class_label) in k_nearest:
            class_votes[class_label] = class_votes.get(class_label, 0) + 1

        # Append the point as a majority of votes
        # That is the class that the point will be assigned to 
        max_votes_class = max(class_votes, key=class_votes.get)
        classes.append((point[0], point[1], max_votes_class))

    return classes



# Generate the points 
points:list[tuple] = generate_points(amount_per_class=POINTS_PER_CLUSTER)

# Classify points with kNN 
classified_points = kNN(1, points)

# Plot each point 
# Class 0 has the color red
# Class 1 has the color blue
for point in classified_points:
    if point[2] == 0:
        plt.plot(point[0], point[1], 'ro')  
    else:
        plt.plot(point[0], point[1], 'bo')  

plt.show()
