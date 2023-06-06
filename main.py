##### IMPORT LIBRARIES #####
import pandas as pd
import re
import numpy as np
from datetime import datetime


##### IMPORT DATA #####
T1 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-1.csv",skiprows=12)
T3 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-3.csv",skiprows=12)
T3S = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-3S.csv",skiprows=12)
T4 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-4.csv",skiprows=12)
T5 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-5-(2021-22).csv",skiprows=12)
T6 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-6.csv",skiprows=12)
T7 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-7.csv",skiprows=12)
T8 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-8-(2021-22).csv",skiprows=12)
T9 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-9.csv",skiprows=12)
T10 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-10.csv",skiprows=12)
T11 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-11-(2021-22).csv",skiprows=12)
T12 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-12.csv",skiprows=12)
T13 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-13.csv",skiprows=12)
T15 = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-15.csv",skiprows=12)
T7c = pd.read_csv("C:/Users/nia.comley/PycharmProjects/CombinedFinance/Data/table-7c.csv",skiprows=12)

##### CLEAN DATA #####
#Table 1 amendments
print(T1['Financial year end'].unique())
print(T1['Academic year'].unique())

#View datatypes
print(T1.dtypes)

# Print the number of null values in each column
print(T1.isnull().sum())

#Convert UKPRN to string
T1['UKPRN'] = T1['UKPRN'].astype(str)
T1['UKPRN'] = T1['UKPRN'].str.replace(r'\..*', '', regex=True)


#Convery NaN to 0
T1['Value(£000s)'] = T1['Value(£000s)'].fillna(0)

# Remove brackets and negate the numbers in 'Value(£000s)'. Convert to integer
T1['Value(£000s)'] = T1['Value(£000s)'].apply(lambda x: int(re.sub(r'\((\d+)\)', r'-\1', str(x))) if pd.notnull(x) else np.nan)

#Double check it has corrected it
print(sorted(T1['Value(£000s)'].unique()))


#Convert data type to datetime for Financial year end
T1['Financial year end'] = pd.to_datetime(T1['Financial year end'], errors='coerce')
T1['Financial year end'] = T1['Financial year end'].dt.strftime('%Y-%m-%d')
print(T1['Financial year end'].unique()) #to check

#Merge Category and Category Marker
T1['Category Overall'] = T1['Category marker']+ ' : ' +T1['Category']

#Recheck data types
T1.dtypes

##### FILTER DATA #####

#Filter out nulls from Financial year end
T1_Final = T1.dropna(subset=['Financial year end'])

#Restrict dataset to certain number of academic years
academic_years = ['2015/16', '2016/17', '2017/18', '2018/19', '2019/20', '2020/21', '2021/22'] #amend this where needed
T1_Final = T1_Final[T1_Final['Academic year'].isin(academic_years)]

#Drop fields don't need
T1_Final = T1_Final.drop(columns=['Category marker', 'Category'])

##### EXPORT DATA #####
T1_Final.to_csv('C:/Users/nia.comley/PycharmProjects/CombinedFinance/Outputs/T1.csv', index=False)
# Print a confirmation message
print("CSV file exported successfully.")