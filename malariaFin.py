import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/quarkoli/PycharmProjects/pythonWork/datasets/incidence_by_ctry.csv')
df1 = pd.read_csv('/Users/quarkoli/PycharmProjects/pythonWork/datasets/incidence_by_region.csv')

# pre-processing
df.columns = ['Country','2017','2016','2015','2014','2013','2012','2011','2010','2005','2000']
df1.columns = ['WHO region','2017','2016','2015','2014','2013','2012','2011','2010','2005','2000']
df = df.drop([0],axis=0)
df1 = df1.drop([0],axis=0)
df.set_index('Country', inplace=True)
df1.set_index('WHO region', inplace=True)
# want to reindex years
years = ['2000','2005','2010','2011','2012','2013','2014','2015','2016','2017']
df = df.reindex(columns =years)
df1 = df1.reindex(columns= years)
print(df1)
# this is how I will subset by country
# print(df.loc['Angola'])

# incidence of malaria per 1000
# needs title, axes labels, and legend
x1 = df.loc['Angola',years].plot()
x2 = df.loc['Burundi',years].plot()
x3 = df.loc['Democratic Republic of the Congo',years].plot()
x4 = df.loc['India'].plot()
x5 = df.loc['United Republic of Tanzania'].plot()
x6 = df.loc['Yemen'].plot()
plt.legend()
plt.show()

m1 = df1.loc['Africa',years].plot()
m2 = df1.loc['(WHO) Global',years].plot()
plt.legend()
plt.show()

