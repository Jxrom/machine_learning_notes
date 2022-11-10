"""
    Introduction to Pandas

        > Library for computation with tabular data
        > Mixed types of data allowed in a single table
        > Columns and rows of data can be named
        > Advanced data aggration and statistical functions

    TYPE             Pandas Name
    Vector           Series 
    (1 Dimension)

    Array            DataFrame
    (2 Dimensions)

"""

"""
    Pandas Series Creation and Indexing
    Use data from step tracking application to create a Pandas Series

"""
import pandas as pd
import numpy as np

step_data = [3620, 7891, 9761, 3907, 4338, 5373]

step_counts = pd.Series(step_data, name='steps') # Pandas Series

#print(step_counts)

step_counts.index = pd.date_range('20150329', periods=6) # Add a date range to the Series
 
#print(step_counts)

# Select data by the index values

# Just like a dictionary
#print(step_counts['2015-04-01'])

# Or by index position--like an array
#print(step_counts[3])

# Select all of April
#print(step_counts['2015-04'])

"""
    Pandas Data Types and Imputation
    Data types can be viewed and converted

"""

# View the data type
#print(step_counts.dtypes)

# Convert to a float
step_counts = step_counts.astype(np.float)

# View the data type
#print(step_counts.dtypes)

# Invalid data points can be easily filled with values

# Create invalid data
step_counts[1:3] = np.NaN

# Now fill it in with zeros
step_counts = step_counts.fillna(0.)
# equivalently,
# step_counts.fillna(0., inplace=True)

#print(step_counts[1:3])

"""
    Pandas DataFrame Creation and Methods
    DataFrames can be created from lists, dictionaries, and Pandas Series

"""

# Cycling distance
cycling_data = [10.7, 0, None, 2.4, 15.3, 10.9, 0, None]

# Create a tuple of data
joined_data = list(zip(step_data, cycling_data))

# The dataframe
activity_df = pd.DataFrame(joined_data)

#print(activity_df)

# Add column names to dataframe
activity_df = pd.DataFrame(
    joined_data, 
    index = pd.date_range('20150329', periods = 6), 
    columns = ['Walking', 'Cycling'])

#print(activity_df)

"""
    Indexing DataFrame Rows
    DataFrame rows can be indexed by row using the 'loc' and 
    'iloc' methods

"""

# Select row of data by index name
#print(activity_df.loc['2015-04-01'])

# Select row of data by integer position
#print(activity_df.iloc[-3])

"""
    Indexing DataFrame Columns
    Dataframe columns can be indexed by name

"""

# Name of column
#print(activity_df['Walking'])

# Object-oriented approach
#print(activity_df.Walking)

# First Column
#print(activity_df.iloc[:,0])

"""
    Reading Data with Pandas
    CSV and other common filetypes can be read with a single command

"""

# The location of the data file
filepath = r'D:\My Documents\Machine Learning\Intel Machine Learning Course\Class1_Introduction_to_Machine_Learning_and_Tools (1)\Class1_Introduction_to_Machine_Learning_and_Tools\data\Iris_Data.csv'

# Import the data
data = pd.read_csv(filepath)

# Print a few rows
#print(data.iloc[:5])

"""
    Assigning New Data to a DataFrame
    Data can be (re-)assigned to a DataFrame column

"""

# Create a new column that is a product
# of both measurements 
data['sepal_area'] = data.sepal_length * data.sepal_width

# Print a few rows and columns
#print(data.iloc[:5, -3:])

"""
    Applying a Function to a DataFrame Column
    Functions can be applied  to columns or rows of a DataFrame or Series

"""

# The lambda function applies what
# follows it to each row of data

data['abbrev'] = (data.species.apply(lambda x: x.replace('Iris-', '')))

# Note that there are other ways to 
# accomplish the above

#print(data.iloc[:5, -3:])

"""
    Concatenating Two DataFrames
    Two DataFrames can be concatenated along either dimension
"""

# Concatenate the first two and 
# last two rows
small_data = pd.concat([data.iloc[:2], data.iloc[-2:]])

#print(small_data.iloc[:, -3:])

# See the 'join' method for
# SQL style joining of dataframes

"""
    Aggregated Statistics with GroupBy
    Using the groupby method calculated aggregated DataFrame statistics

"""

# Use the size method with a
# DataFrame to get count
# For a Series, use the .value_counts
# method

group_sizes = (data.groupby('species').size())

#print(group_sizes)

"""
    Performing Statistical Calculations
    Pandas contains a variety of statistical methods-mean, median, and mode
"""

# Mean calculated on a DataFrame
#print(data.mean())

# Median calculated on a Series
#print(data.petal_length.median())

# Mode calculated on a Series
#print(data.petal_length.mode())

# Standard dev, variance, and SEM
#print(data.petal_length.std(),
#      data.petal_length.var(),
#      data.petal_length.sem())

# As well as quantiles
#print(data.quantile(0))

#print(data.describe())

"""
    Sampling from DataFrames
    DataFrames can be randomly sampled from
"""

# Sample 5 rows without replacement
sample = (data.sample(n=5, replace=False, random_state=42))

#print(sample.iloc[:, -3:])

"""
    Basic Scatter Plots with Matplotlib
    Scatter plots can be created from Pandas Series
"""

# %%
import matplotlib.pyplot as plt


#plt.plot(data.sepal_length, data.sepal_width, ls='', marker='o')

#plt.plot(data.sepal_length, data.sepal_width, ls='', marker='o', label='sepal')

#plt.plot(data.petal_length, data.petal_width, ls='', marker='o', label='petal')

"""
    Histogram with Matplotlib
    Histrograms can be created from Pandas Series
"""

#plt.hist(data.sepal_length, bins=25)

"""
    Customizing Matplotlib Plots
    Every feature of Matplotlib plots can be customized
"""

fig, ax = plt.subplots()

ax.barh(np.arange(10), data.sepal_width.iloc[:10])

# Set position of ticks and tick labels
#ax.set_yticks(np.arange(0.4, 10.4, 1.0))
#ax.set_yticklabels(np.arange(1, 11))
#ax.set(xlabel='xlabel', ylabel='ylabel',title='Title')


(data.groupby('species').mean().plot(color=['red', 'blue', 'black',
    'green'], fontsize=10.0, figsize=(4, 4)))


import seaborn as sns

sns.jointplot(x='sepal_length',y='sepal_width', data=data, size=4)


sns.pairplot(data, hue='species', size=3)
# %%