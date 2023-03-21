# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 07:51:35 2023

@author: Simar
"""

import pandas as pd

data= pd.read_csv('transaction.csv',sep=';')

#summary of data

data.info()


#Fetchin the coloumn from the dataframe
CostPerItem= data['CostPerItem']
SellingPricePerItem= data['SellingPricePerItem']


#creating New Coloumn
NumberOfItemsPurchased= data['NumberOfItemsPurchased']
CostPerTransactions= CostPerItem * NumberOfItemsPurchased
data['CostPerTransactions']= data['CostPerItem']*data['NumberOfItemsPurchased']
data['SalesPerTransaction']= data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['profit']= data['SalesPerTransaction']-data['CostPerTransactions']
data['Markup']=data['profit']/data['CostPerTransactions']


#Rounding Markup
data['Markup']= round(data['Markup'],2)


#CHnaging The variable type

print(data['Day'].dtype)
day=data['Day'].astype(str)
print(day.dtype)
print(data['Year'].dtype)
year=data['Year'].astype(str)
mydate= day+'-'+data['Month']+'-'+year

#Combining date

data['Date']= mydate


#Usig iloc to view specific row/coloumn
data.iloc[0]
data.iloc[0:3]#First 3 rows
data.iloc[0:-5]#LAST 5 COLUMNS
data.iloc[-5]#laST 5 rOWS

#SPLITING THE CLIENT KEYWOD COLOUMN
col_split= data['ClientKeywords'].str.split(',', expand=True)

#Adding the coloun to the dataframe
data['ClientAge'] = col_split[0]
data['ClientType'] = col_split[1]
data['LenthOfContact']= col_split[2]

#Replacing the bractits

data['ClientAge']= data['ClientAge'].str.replace('[','')
data['LenthOfContact']= data['LenthOfContact'].str.replace(']','')

#Lowering Item Description

data['ItemDescription']= data['ItemDescription'].str.lower()

#merging another dataset with our current dataset
seasons= pd.read_csv('value_inc_seasons.csv',sep=';')
data= pd.merge(data,seasons, on='Month')
#on='key' key means the common column
data = data.drop('ClientKeywords',axis = 1)
data = data.drop('Year',axis = 1)   
data = data.drop('Month',axis = 1)
data = data.drop('Day',axis = 1)

#Export_to_csv
data.to_csv('ValueInc_Cleaned.csv', index=False)

