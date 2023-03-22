# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:56:50 2023

@author: Simar
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method to open jason file

json_file= open('loan_data_json.json')
data= json.load(json_file)

#transfrom to database
loandata =pd.DataFrame(data)

#Using Exp to get Actual income
income=np.exp(loandata['log.annual.inc'])
loandata['annualincome']=income

ficodata=[]
length=len(loandata)
for x in range(0,length):
    ficoscore=loandata['fico'][x]
    try:
        if ficoscore >= 300 and ficoscore< 400: 
                ficocategory='Very Poor'
        elif ficoscore >= 400 and ficoscore < 600:
                ficocategory='Poor'
        elif ficoscore >= 601 and ficoscore < 660: 
                ficocategory='Fair'
        elif ficoscore >= 660 and ficoscore < 780:
                ficocategory= 'Good'
        elif ficoscore >=780: 
                ficocategory='Excellent'
        else: 
            ficocategory='Unknown'
    except:
            ficocategory='Unknown'
    ficodata.append(ficocategory)  
    
loandata['FicoCategory']=ficodata


#conditional statements in dataframe
loandata.loc[loandata['int.rate'] >=0.12 ,'IntrestType']='High'
loandata.loc[loandata['int.rate'] <=0.12 ,'IntrestType']='Low'

#grouping by the data

catplot=loandata.groupby(['FicoCategory']).size()
catplot.plot.bar(color='red',width=0.8)
plt.show()


purplot=loandata.groupby(['purpose']).size()
purplot.plot.bar(color='green',width=0.5)
plt.show()

#scatterplot for this we need x and y axis

xpoint=loandata['annualincome']
ypoint=loandata['dti']
plt.scatter(ypoint,xpoint,)
plt.show()

#writng to csv
loandata.to_csv('loandata_cleaned.csv',index= True)
