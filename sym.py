import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm

# Our first step is to read the given data
data_csv = pd.read_csv('data.csv')
x_title = list(data_csv)[0]
y_title = list(data_csv)[1]
group_title = list(data_csv)[2]

# Specify inputs for the model
xy = data_csv[[x_title, y_title]].values
type_label = np.where(data_csv[group_title]==1, 1, 2)

# Create and fit the linear SVN model
model = svm.SVC(kernel='linear')
model.fit(xy, type_label)

# Get the hyperplane
w = model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(min(xy[:,0]), max(xy[:,1]))
yy = a * xx - (model.intercept_[0] / w[1])

# Visualize the results
sns.lmplot(x_title, y_title, data=data_csv, hue=group_title, fit_reg=False) # Plot the points
plt.plot(xx, yy, linewidth=2, color='black') # Plot the hyperplane
plt.show()
