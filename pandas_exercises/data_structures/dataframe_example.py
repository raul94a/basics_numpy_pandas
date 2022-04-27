from pickle import FALSE
import numpy as np
import pandas as pd

data = pd.read_csv('data/project_data.csv')
print(data.head(1))
print(data.loc[0,'year_of_birth '])

# print(data)
#if you wanna select 5 first rows
#print(data.head())
#some data manipulation with boolean masking and fancy indexing
# print(data.loc[data['year_of_birth '] == 2000, ['educational_level', 'marital_status', 'annual_income']][0:5])
#if you wanna select 5 last rows
#print(data.tail())

##unique values
# print(data['year_of_birth '].unique())
# for i in data.keys():
#     print(data[i].unique())ç

##applying value_counts
##if you don't pass normalize=True the method returns TOTAL of each type. When normalized it returns the percentage of occurrence of each value

# print(round(data['educational_level'].value_counts(normalize=True),2))

# #duplicated
# print(data.duplicated().sum())

# ##selecting Master or PhD education level with > 1990 year of birth
# selected_data = data[list((data['year_of_birth '] > 1993) & (data['educational_level'].isin(['Master','PhD'])))]

# print(selected_data.sort_values(by= ['annual_income'], ascending=False))