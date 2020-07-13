from flask import Flask, render_template
app = Flask(__name__)

import pandas as pd
import numpy as np

from IPython.display import display

@app.route('/')
def index():

    pandas_df_data = python_input()

    dframe_isnull(pandas_df_data, 'Description')

    dframe_notnull(pandas_df_data, 'Description')

    dframe_isjunkchar(pandas_df_data, 'Description')

    dframe_notjunkchar(pandas_df_data, 'Description')

    return "Execution is successful!"


def python_input():

    # Data inputs from Amazin s3 / Public Hosted Endpoint
    # pandas_df_data = pd.read_csv("https://ecom-su-html-test-reports-nonprod.s3-eu-west-1.amazonaws.com/AutomatedTest/E-Commerce_Product.csv")

    # Data inputs from Local Path
    pandas_df_data = pd.read_csv("Resource/Features/E-OnlineRetai.csv", encoding= 'unicode_escape')

    print('################## Total Data Count and shape ##################')
    display(pandas_df_data.shape)

    np.savetxt(r'Python-Report/Pandas_df_data.txt', pandas_df_data.values, fmt='%s', delimiter='\t')

    return pandas_df_data


def dframe_isnull(pandas_df_data, dColumn_Name):

    pandas_dataframe_isnull = pandas_df_data[pd.isnull(pandas_df_data[dColumn_Name])]

    print('################## Total Data ('+dColumn_Name+') Count and shape - IS NULL ##################')

    display(pandas_dataframe_isnull.shape)
    display(pandas_dataframe_isnull)

    np.savetxt(r'Python-Report/Pandas_dataframe_isnull.txt', pandas_dataframe_isnull.values, fmt='%s', delimiter='\t')

    return pandas_dataframe_isnull


def dframe_notnull(pandas_df_data, dColumn_Name):

    pandas_dataframe_notnull = pandas_df_data[pd.notnull(pandas_df_data[dColumn_Name])]

    print('################## Total Data ('+dColumn_Name+') Count and shape - NOT NULL ##################')

    display(pandas_dataframe_notnull.shape)
    display(pandas_dataframe_notnull)

    np.savetxt(r'Python-Report/Pandas_dataframe_notnull.txt', pandas_dataframe_notnull.values, fmt='%s', delimiter='\t')

    return pandas_dataframe_notnull


def dframe_isjunkchar(pandas_df_data, dColumn_Name):

    spec_chars = '[!@#$%&*_+-=|\:";<>,./()[\]{}\']'

    pandas_dataframe_isjunkchar = pandas_df_data.loc[pandas_df_data[dColumn_Name].str.contains(r''+spec_chars+'') == True]

    print('################## Total Data ('+dColumn_Name+') Count and shape - JUNK CHARACTER ##################')
    print(spec_chars)

    display(pandas_dataframe_isjunkchar.shape)
    display(pandas_dataframe_isjunkchar)

    np.savetxt(r'Python-Report/Pandas_dataframe_isjunkchar.txt', pandas_dataframe_isjunkchar.values, fmt='%s', delimiter='\t')

    return pandas_dataframe_isjunkchar


def dframe_notjunkchar(pandas_df_data, dColumn_Name):

    spec_chars = '[!@#$%&*_+-=|\:";<>,./()[\]{}\']'

    pandas_dataframe_notjunkchar = pandas_df_data.loc[pandas_df_data[dColumn_Name].str.contains(r''+spec_chars+'') == False]

    print('################## Total Data ('+dColumn_Name+') Count and shape - NOT JUNK CHARACTER ##################')
    print(spec_chars)

    display(pandas_dataframe_notjunkchar.shape)
    display(pandas_dataframe_notjunkchar)

    np.savetxt(r'Python-Report/Pandas_dataframe_notjunkchar.txt', pandas_dataframe_notjunkchar.values, fmt='%s', delimiter='\t')

    return pandas_dataframe_notjunkchar


if __name__ == '__main__':
    app.run(debug=True)