# Reusable Pandas Code Snippets

This repo is inspired by the article ["How to re-use code snippets"](https://medium.com/ibm-data-ai/how-to-re-use-code-snippets-in-jupyterlab-3e4495fa6e31) by Patrick Titzler

Contains a collection of Pandas code snippets from data reading to data analysis or cleaning for use in a JupyterLab setting.

Each Code Snippet contains a working example of a Pandas funcionality:

- Base knowledge of NumPy & Pandas (`Base` tag) 
    - Column Selection
    - Creating a Dataframe
    - Operating with Series
    - Statistical Methods
    - Transforming Series

- Read and Writing data (`Read & Write` tag)
    - Loading JSON data into a Dictionary
    - Reading Excel data
    - Reading Financial data
    - Reading HTML data
    - Reading JSON data
    - Reading PDF data
    - Reading Text data
    - Reading and Writing data from a Database
    - Reading and Writing data in a binary format
    - Reading and Writing data in a compatible format
    - Reading data from a String
    - Synthetic data
    - Writing data to CSV
    - Writing data to Excel
    - Writing data to JSON
    - Writing data to a Dictionary

- Data Analysis (`Data Analysis` tag)
    - Adding new columns
    - Concatenating Dataframes
    - Dataframe Interactive View
    - Dataframe Pretty Print
    - Deleting columns
    - Deleting rows
    - Distinct values
    - Exploring a Dataframe
    - Filtering Rows
    - Filtering columns
    - Grouping data
    - Joining Dataframes
    - Method Chaining
    - Ordering Rows
    - Pandas Options
    - Pandas styling
    - Pivot Tables
    - Renaming columns
    - Reordering Columns
    - Updating existing Columns

- Data Cleaning (`Data Cleaning` tag)
    - Converting Data Types
    - Data Formatting
    - Dropping Duplicates
    - Filling Missing Data
    - Identifying Data Types
    - Identifying Duplicates
    - Identifying Missing Data
    - Identifying duplicated column names
    - Joining Columns
    - Pandas Flags
    - Removing Missing Data
    - Removing columns name
    - Removing index name
    - Reshaping Dataframes
    - Separating columns
    - Special Cases
    - Transforming Dataframes


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
