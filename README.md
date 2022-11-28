# Reusable Pandas Code Snippets

This repo is inspired by the article ["How to re-use code snippets"](https://medium.com/ibm-data-ai/how-to-re-use-code-snippets-in-jupyterlab-3e4495fa6e31) by Patrick Titzler

Contains a collection of Pandas Snippets from data reading to data analysis or cleaning for use in a JupyterLab setting.

Each Code Snippet contains a working example of a Pandas funcionality:

- Base knowledge of pandas (`Base` tag) 
    - Applying a lambda function to two columns in a Dataframe
    - Checking Missing or Null Values in a Serie
    - Columns of a Dataframe
    - Creating a Dataframe
    - Operations with two Series
    - Selecting a cell from a Dataframe
    - Selecting a single column of a Dataframe
    - Shape of a Dataframe
    - Statistical methods
    - String Operations on Series
    - Transforming Series
    - Transposing a Dataframe

- Read and Writing data (`Read & Write` tag)
    - Generating Synthetic data
    - Loading JSON data into a Python Dictionary
    - Reading Financial data
    - Reading Web Service data
    - Reading and Writing data in a compatible format
    - Reading binay data
    - Reading data from Excel
    - Reading data from a Database
    - Reading data from a Python Dictionary
    - Reading data from a String
    - Reading data from a Web Service
    - Reading from a JSON File
    - Reading from a Text File
    - Reading from data from a Web Page / HTML
    - Writing a binary format
    - Writing data to Excel
    - Writing data to a JSON File
    - Writing data to a Relational Database
    - Writing data to a Text File

- Exploring a Dataframe (`Exploring Data` tag)
    - Compute pairwise correlation of a Dataframe
    - Configuring global behavior related to DataFrame display
    - Counting unique values
    - Exploring a Value from a Dataframe
    - Exploring some rows of a Dataframe
    - Generate descriptive statistics
    - Getting information about a Dataframe
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

- Regex Snippets (`Regex` tag)

## How to use

Check it out this [article](https://medium.com/ibm-data-ai/how-to-re-use-code-snippets-in-jupyterlab-3e4495fa6e31)

## How to install

In order to use these code snippets it is necessary to perform the following steps:

- Open a [Command Line Prompt](https://www.lifewire.com/how-to-open-command-prompt-2618089)

- Install the Elyra Code Snippet extension package

```
pip install elyra-code-snippet-extension
```

- Identify the location of Jupyter Data Directory

```
jupyter --data-dir
```

- Go to the location of Jupyter Data Directory and check if a subdirectory named `metadata` exists. 

In my environment, I used the following command:

```
cd C:\Users\Daniel\AppData\Roaming\jupyter

dir
```

If not exists create it

In my environment, I used the following command:

```
cd C:\Users\Daniel\AppData\Roaming\jupyter

mkdir metadata
```

- Clone this repo in a subdirectory named `code-snippets` under the location `metadata` subdirectory

In my environment, I used the following command:

```

cd C:\Users\Daniel\AppData\Roaming\jupyter\metadata

git clone https://github.com/dvillaj/pandas-code-snippets.git code-snippets
```
