# SVM-Model
This is a program that creates a support vector machine (SVM) based on the data given in the data.csv file. An SVM is a machine learning algorithm that can attempt to find a distinction between two groups of data with the maximum margin. For this specific implementation, if you supply this algorithm with two-dimensional data in the data.csv file, it will attempt to find a linear hyperplane that will characterize the different groups and display it out to the screen.

![Image of SVM model](https://image.ibb.co/eKECoe/svm_model.png)

## Requirements
You will require to install following libraries in python3. You can easily install any of them using "pip install [library]".
  - Pandas
  - Numpy
  - Matplotlib
  - Seaborn
  - Scikit-learn

## Usage
To use this program, edit the data.csv file to include the data that you would like to have. The data should have three columns: 1.) the X value, 2.) the Y value, 3.) the group that the point is in. Then run the program using python, and it will create a line that will predict the location of your values.
