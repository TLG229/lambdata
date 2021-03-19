"""Lambdata_repo - a collections of Data Science Helper Functions"""

# accessing Libraries through pipenv
# import pandas as pd
# import numpy as np

# 
def rm_outlier():

    """a function to remove outliers using 1.5*interquartile range"""
    
    dataframe = str(input("Dateframe name:"))
    Q1 = dataframe.quantile(q=.25)
    Q3 = dataframe.quantile(q=.75)
    IQR = dataframe.apply(stats.iqr)
    outlier_remover = data[~((data < (Q1-1.5*IQR)) | (data > (Q3+1.5*IQR))).any(axis=1)]
 
rm_outlier()

def null_count():

  """ This function caluclates the number of null values in a dataframe and returns 
  the results"""
  
  dataframe = str(input("Dateframe name:"))
  null_count_total = dataframe.isnull().sum().sum()
  print("The number of missing values of the dataframe is",null_count_total)

null_count()