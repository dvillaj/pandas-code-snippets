# Reusable Pandas Code Snippets

This repo is inspired for the article ["How to re-use code snippets"](https://medium.com/ibm-data-ai/how-to-re-use-code-snippets-in-jupyterlab-3e4495fa6e31) by Patrick Titzler

Contains a collection of Pandas Snippets from data reading to data analysis or cleaning for use in a JupyterLab setting.

Each Code Snippet contains a working example of a Pandas funcionality:

- Base knowledge of pandas (`Base` tag) 
    - Applying a lambda function to two columns in a Dataframe
    - Checking Missing or Null Values in a Serie
    - Columns of a Dataframe
    - Creating a Dataframe from a Serie
    - Operations with two Series
    - Selecting a cell from a Dataframe
    - Selecting a single column of a Dataframe
    - Shape of a Dataframe
    - Statistical methods
    - String Operations on Series
    - Transforming Series
    - Transposing a Dataframe

- Read and Writing data (`Read & Write` tag)
    - CSV
    - JSON File
    - Excel
    - HTML
    - Web Services
    - Python dictionary
    - Relational Database
    - Fake Data
    - Pickle

- Exploring a Dataframe (`Exploring Data` tag)
    - Compute pairwise correlation of a Dataframe
    - Configuring global behavior related to DataFrame display
    - Counting unique values
    - Generate descriptive statistics
    - Getting information about a Dataframe
    - Getting some rows of a Dataframe
    - Highlight a Dataframe
    - Profiling Report

- Exploring local Files in a Jupyter notebook (`Bash` tag)
    - List files in a directory
    - Locate files into a directory (and all the subdirectories)
    - Search for a text inside a file
    - Show the content of a file   

- Data Analysis (`Data Analysis` tag)
    - Adding new columns
    - Concatenating Dataframes
    - Deleting columns
    - Deleting rows
    - Duplicate column names
    - Filtering Rows
    - Grouping data
    - Joining data
    - Pivot Tables
    - Renaming columns
    - Replacing existing columns
    - Rewiting SQL in Pandas
    - Selecting columns
    - Selecting distinct values
    - Sorting columns

- Data Cleaning (`Data Cleaning` tag)
    - Converting Data Types
    - Data Format
    - Dropping Duplicates
    - FIlling Missing Values
    - Identifying Data Types
    - Identifying Duplicates
    - Identifying Missing Values
    - Identifying duplicate labels
    - Joining Columns
    - Narrowing down tables
    - Separating columns
    - Set a Column as Index
    - Special Case
    - Widening tables

## How to install

In order to use these code snippets it is necessary to perform the following steps:

- Install the [Elyra Code Snippet extension](https://github.com/elyra-ai/elyra)

```
pip install elyra-code-snippet-extension
```

- Identify the location of Jupyter Data Directory

```
jupyter --data-dir
```

- Clone this repo in a subdirectory named `metadata` under the location of Jupyter Data Directory

In my environment, I use the following command:

```
git clone git@github.com:dvillaj/pandas-code-snippets.git C:\Users\Daniel\AppData\Roaming\jupyter\metadata\code-snippets
```
