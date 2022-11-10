"""
    Machine Learning Overview

    Machine Learning is a way of taking data and turning it into insights.
    We use computer power to analyze examples from the past to build
    a model that can predict the result for new examples.

    Machine Learning can be used to create a chatbot, detect spam or 
    image recognition.
"""

"""
    Pandas is used for reading data and data manipulation
    Numpy is used for computations of numerical data
    Matplotlib is used for graphing data
    Scikit-learn is used for machine learning models
"""

"""
    Types of Machine Learning

    Supervised Learning - is when we have a known target based on past data
        e.g Predicting what price a house will sell for
    Unsupervised Learning - is when there isn't a known past answer
        e.g Determining the topics discussed in restaurant reviews
"""

"""
    Supervised Learning Categories
        Regression - prediciting a numerical value
            e.g. Predicting what price a house will sell for
        Classification -Prediciting what class something belongs to
            e.g. Predicting if a borrower will default on their loan
"""

"""
    Statistics Review

        Averages
            15, 16, 18, 19, 22, 24, 29, 30, 34 

            The mean is the most commonly known average

            Add up all the values and divide by the number of values:
            (15 + 16 + 18 + 19 + 22 + 24 + 29 + 30 + 34) / 9 =  207/9 = 23

            The median is the value in the middle. In this case, since there are 9 values, 
            the middle value is the 5th, which is 22.

            In statistics, both the mean and the median are called averages.
            The layman's average is the mean.

        Percentiles
            The median can also be thought of as the 50th percentile. 
            This means that 50% of the data is less than the median and 50% of the data is greater than the median. 
            This tells us where the middle of the data is, but we often want more of an understanding of the distribution of the data. 
            We’ll often look at the 25th percentile and the 75th percentile.

            The 25th percentile is the value that’s one quarter of the way through the data. 
            This is the value where 25% of the data is less than it (and 75% of the data is greater than it).

            Similarly, the 75th percentile is three quarters of the way through the data. 
            This is the value where 75% of the data is less than it (and 25% of the data is greater than it).

            If we look at our ages again:
                15, 16, 18, 19, 22, 24, 29, 30, 34 
            
            We have 9 values, so 25% of the data would be approximately 2 datapoints. So the 3rd datapoint is greater than 25% of the data. 
            Thus, the 25th percentile is 18 (the 3rd datapoint).
            Similarly, 75% of the data is approximately 6 datapoints. So the 7th datapoint is greater than 75% of the data. 
            Thus, the 75th percentile is 29 (the 7th datapoint).

            The full range of our data is between 15 and 34. The 25th and 75th percentiles tell us that half our data is between 18 and 29. 
            This helps us gain understanding of how the data is distributed.

            If there is an even number of datapoints, to find the median (or 50th percentile), 
            you take the mean of the two values in the middle.

        Standard Deviation & Variance
            We can get a deeper understanding of the distribution of our data with the standard deviation and variance. The standard deviation and variance are measures of how dispersed or spread out the data is.

            We measure how far each datapoint is from the mean.

            Let's look at our group of ages again:
                15, 16, 18, 19, 22, 24, 29, 30, 34
            
            Recall that the mean is 23.

            Let's calculate how far each value is from the mean. 
            15 is 8 away from the mean (since 23-15=8).

            Here's a list of all these distances:

            8, 7, 5, 4, 1, 1, 6, 7, 11
            
            We square these values and add them together.

            We divide this value by the total number of values and that gives us the variance.
            362 / 9 = 40.22 
"""

"""
    Statistics with Python

    We can calculate all of these operations with Python. We will use the Python package numpy. 
    We will use numpy more later for manipulating arrays, but for now we will just use a few functions 
    for statistical calculations: mean, median, percentile, std, var.

    First we import the package. It is standard practice to nickname numpy as np
"""

import numpy as np

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

print("mean:", np.mean(data))
print("median:", np.median(data))
print("50th percentile (median):", np.percentile(data, 50))
print("25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))
print("standard deviation:", np.std(data))
print("variance:", np.var(data))