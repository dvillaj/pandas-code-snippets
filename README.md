# Pandas Code Snippets

This repo is inspired for the article ["How to re-use code snippets](https://medium.com/ibm-data-ai/how-to-re-use-code-snippets-in-jupyterlab-3e4495fa6e31) by Patrick Titzler

Contains a collection of Pandas Snippets from data reading to data analysis or cleaning for use in a JupyterLab setting.

## How to install

In order to use these code snippets it is necessary to perform the following steps:

- Install the (Elyra Code Snippet extension](https://github.com/elyra-ai/elyra)

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
