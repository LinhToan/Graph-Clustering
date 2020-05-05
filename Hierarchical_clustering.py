# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:13:31 2020

@author: Hiro
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib as mpl
%matplotlib inline

mpl.rcParams['figure.figsize'] = (8, 8)

#create a toy data set
X = np.array([[5,3], [10, 15], [15,12], [24, 10], [30, 30], [85, 70], [71, 80], [60, 78], [70, 55], [80, 91]])

labels = range(len(X))
plt.figure()
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:, 0], X[:, 1], label = 'True Position')

for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(label, xy = (x, y), xytext = (-3, 3), textcoords = 'offset points', ha = 'right', va = 'bottom')

#using scikit learn
from sklearn.cluster import AgglomerativeClustering as AC

cluster = AC(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
cluster.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=cluster.labels_, cmap = 'rainbow')

#using the iris dataset
from sklearn import datasets

iris = datasets.load_iris()

cluster = AC(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
cluster.fit_predict(iris.data)

cluster.labels_