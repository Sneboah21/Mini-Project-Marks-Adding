import pandas as pd

dataframe = pd.read_csv("Input_files\Mini Project - Marks Adding.csv", sep=',')
#print(dictionary.head()) this is to print first 5 rows
#print(dataframe['Roll Num'].value_counts()) to count how many times a particular object is repeated
new_dataframe = dataframe.groupby('Roll Num').sum().reset_index()
print(new_dataframe.head())
new_dataframe.to_csv('Output_files\output.csv',index = False)
