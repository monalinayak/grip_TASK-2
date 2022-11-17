# -*- coding: utf-8 -*-
"""grip_TASK-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tcEDvUPIuTSkVwCco1iInywKu1b59Jo4

**The Sparks Foundation**

**Data Science and Bussiness Analytics**

**Task-2 Prediction using Unsupervised ML**

### **Name- Monali Nayak**

**Importing the Dependencies**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

df=pd.read_csv('/content/sample_data/Iris.csv')

"""**Exploring Data**"""

df.head("Add import")

df.shape

df.describe()

df.info()

df.isnull().sum()

"""**Hence, There are no null values.**"""

sns.pairplot(df)

"""**### Using Elbow Method to find the Optimal Number of Clusters**

**Data Preparation**
"""

x=df.iloc[:,1:5].values

wcss=[]
for i in range(1,11):
  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

#plotting the elbow plot
plt.plot(range(1,11),wcss,marker=".")
plt.title('The Elbow Plot')
plt.xlabel('No. of Clusters')
plt.ylabel('WCSS')
plt.show()

"""**We can conclude(from the elbow plot) that the optimal no. of clusters =3**"""

kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
#return a label per data point based on the cluster
Y=kmeans.fit_predict(x)
Y

"""**Visualizing the Clusters**"""

plt.figure(figsize=(8,8))
plt.scatter(x[Y==0,0],x[Y==0,1],s=50,c='blue',label='Iris-Setosa')
plt.scatter(x[Y==1,0],x[Y==1,1],s=50,c='red',label='Iris-Versicolor')
plt.scatter(x[Y==2,0],x[Y==2,1],s=50,c='yellow',label='Iris-Virginica')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='black',label="Centroids",marker='*')
plt.title("Visualizing Clusters")
plt.legend()
plt.show()

"""**CONCLUSION**
1. On applying the elbow method, the optimum no of clusters obtained is 3.
2. A scatter graph has been ploted for the visualization of each clusters and the centroids of each cluster is represented by a star.
"""