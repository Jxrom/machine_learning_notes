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
print(data.iloc[:5])

"""
    Assigning New Data to a DataFrame
    Data can be (re-)assigned to a DataFrame column

"""

# Create a new column that is a product
# of both measurements 
data['sepal_area'] = data.sepal_length * data.sepal_width

# Print a few rows and columns
print(data.iloc[:5, -3:])
