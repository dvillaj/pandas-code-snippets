# Reusable Pandas Code Snippets

This repo is inspired by the article ["How to re-use code snippets"](https://medium.com/ibm-data-ai/how-to-re-use-code-snippets-in-jupyterlab-3e4495fa6e31) by Patrick Titzler

Contains a collection of Pandas code snippets from data reading to data analysis or cleaning for use in a JupyterLab setting.

Each Code Snippet contains a working example of a Pandas funcionality:

- Base knowledge of NumPy & Pandas (`Base` tag) 
    - Accessing to NumPy Arrays
    - Accessing to Series
    - Column Selection on a Dataframe
    - Convert a Serie into a Dataframe
    - Creating NumPy Arrays
    - Creating a Dataframe
    - Creating a Serie
    - Dataframe  Rows Selection
    - Dataframe Rows Selection
    - Empty or Null Values on a Serie
    - Filtering NumPy Arrays
    - Filtering Series
    - Manipulating Strings on Series
    - Multi Column Selection on a Dataframe
    - Operating with Columns in a Dataframe
    - Operating with Series
    - Reshaping a NumPy Array
    - Shape of a Dataframe
    - Single Row Selection by position
    - Statistical methods
    - Transforming Series
    - Values and Index of a Serie
    - Values, Columns and Index of a Dataframe

- Read and Writing data (`Read & Write` tag)
    - Generating Synthetic data
    - Loading JSON data into a Python Dictionary
    - Reading Financial data
    - Reading and Writing data in a compatible format
    - Reading data from Excel
    - Reading data from a Database
    - Reading data from a JSON File
    - Reading data from a Python Dictionary
    - Reading data from a String
    - Reading data from a Text File
    - Reading data from a Web Page / HTML
    - Reading data from a Web Service
    - Reading data from a binary format
    - Unix commands to explore directories
    - Unix commands to explore files
    - Unix commands to explore online data
    - Writing data to Excel
    - Writing data to a JSON File
    - Writing data to a Relational Database
    - Writing data to a Text File
    - Writing data to a binary format

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
    - Do not allow duplicate column names
    - Dropping Duplicates
    - Filling Missing Values
    - Identifying Data Types
    - Identifying Duplicates
    - Identifying Missing Values
    - Identifying duplicates
    - Joining Columns
    - Narrowing down tables
    - Removing columns name
    - Removing index name
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
