# Reusable Pandas Code Snippets

This repo is inspired by the article ["How to re-use code snippets"](https://medium.com/ibm-data-ai/how-to-re-use-code-snippets-in-jupyterlab-3e4495fa6e31) by Patrick Titzler

Contains a collection of Pandas code snippets from data reading to data analysis or cleaning for use in a JupyterLab setting.

Each Code Snippet contains a working example of a Pandas funcionality:

- Base knowledge of NumPy & Pandas (`Base` tag) 
    - Accessing to NumPy Arrays
    - Accessing to Series
    - Column Selection on a Dataframe
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
    - Statistical methods on NumPy Arrays
    - Statistical methods on Series
    - Transforming Dataframes
    - Transforming Series
    - Values and Index of a Serie
    - Values, Columns and Index of a Dataframe

- Read and Writing data (`Read & Write` tag)
    - Generating Synthetic data
    - Loading JSON data into a Python Dictionary
    - Reading Financial data
    - Reading JSON data from a Python Dictionary
    - Reading and Writing data from a Database
    - Reading and Writing data in a binary format
    - Reading and Writing data in a compatible format
    - Reading data from Excel
    - Reading data from JSON
    - Reading data from a String
    - Reading data from a Text File
    - Reading data from a Web Page / HTML
    - Reading data from a Web Service
    - Unix commands to explore directories
    - Unix commands to explore files
    - Unix commands to explore online data
    - Writing data to Excel
    - Writing data to a JSON File
    - Writing data to a Text File

- Data Analysis (`Data Analysis` tag)
    - Adding new columns
    - Concatenating Dataframes
    - Deleting columns
    - Deleting rows
    - Distinct values
    - Exploring a Dataframe
    - Filtering Rows
    - Filtering columns
    - Grouping data
    - Joining Dataframes
    - Ordering Rows
    - Pandas Options
    - Pandas styling
    - Pivot Tables
    - Renaming columns

- Data Cleaning (`Data Cleaning` and `Regex` tags )
    - Converting Data Types
    - Data Formatting
    - Dropping Duplicates
    - Filling Missing Data
    - Identifying Data Types
    - Identifying Duplicates
    - Identifying Missing Data
    - Identifying duplicated column names
    - Joining Columns
    - Narrowing down tables
    - Pandas Flags
    - Removing Missing Data
    - Removing columns name
    - Removing index name
    - Separating columns
    - Special Cases
    - Transforming Dataframes
    - Widening tables

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

In my environment, I used the following commands:

```
cd C:\Users\Daniel\AppData\Roaming\jupyter

dir
```

If not exists create it

In my environment, I used the following commands:

```
cd C:\Users\Daniel\AppData\Roaming\jupyter

mkdir metadata
```

- Clone this repo in a subdirectory named `code-snippets` under the location `metadata` subdirectory

In my environment, I used the following commands:

```

cd C:\Users\Daniel\AppData\Roaming\jupyter\metadata

git clone https://github.com/dvillaj/pandas-code-snippets.git code-snippets
```
