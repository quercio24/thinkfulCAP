import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/quarkoli/PycharmProjects/pythonWork/datasets/incidence_by_ctry.csv') # incidence by ctry
df1 = pd.read_csv('/Users/quarkoli/PycharmProjects/pythonWork/datasets/incidence_by_region.csv') # incidence by region
df2 = pd.read_csv('/Users/quarkoli/PycharmProjects/pythonWork/datasets/cases_by_ctry.csv') # cases by ctry
df3 = pd.read_csv('/Users/quarkoli/PycharmProjects/pythonWork/datasets/per_Capita.csv') # gdp by ctry

# pre-processing
df.columns = ['Country','2017','2016','2015','2014','2013','2012','2011','2010','2005','2000']
df1.columns = ['WHO region','2017','2016','2015','2014','2013','2012','2011','2010','2005','2000']
df = df.drop([0],axis=0)
df2.columns = ['Country','2017','2016','2015','2014','2013','2012','2011','2010','2005','2000']
df3 = df3.rename(columns={"Country Name": "Country"})
df.set_index('Country', inplace=True)
df1.set_index('WHO region', inplace=True)
df2.set_index('Country', inplace=True)
df3.set_index('Country', inplace=True)

# want to reindex years
years = ['2000','2005','2010','2011','2012','2013','2014','2015','2016','2017']
df = df.reindex(columns=years)
df1 = df1.reindex(columns=years)
df2 = df2.reindex(columns=years)
df3 = df3.reindex(columns=years)
# print(df.head())
# print(df3.head())


# merging df with df3 to create incidence by country and gdp data frame
# replacing all nan values with zeros and removing them
df_merge = pd.merge(df,df3,how='left',on='Country')
df_merge = df_merge.rename(columns={"2017_x" : "Incidence", "2017_y" : "Capita"})
df_merge['Incidence'] = df_merge['Incidence'].replace(0,np.nan)
df_merge['Capita'] = df_merge['Capita'].replace(0,np.nan)
df_main = df_merge[['Incidence','Capita']]

# dropping all nan values
df_main = df_main.dropna()

df_main = df_main.sort_values('Incidence')
# want to eliminate incidence less than 1 per 1000
df_main = df_main[df_main['Incidence'] > 1.00]
df_main = df_main.sort_values('Capita')

# scatter plots normal, logx fitted, linearly fitted
# normal
# scatter = df_main.plot.scatter('Capita', 'Incidence')
# plt.ylabel('Incidence per 1000')
# plt.title("Incidence vs Per Capita for 2017 by country")
# plt.show()
#
# # logx fitted
# ax = sns.regplot(x=df_main['Capita'], y=df_main['Incidence'],
#                  logx=True, truncate=True)
# plt.title("Incidence vs Per Capita for 2017 by country (logx fitted)")
# plt.ylabel('Incidence per 1000')
# plt.show()
# # linearly fitted
# ax = sns.regplot(x=df_main['Capita'], y=df_main['Incidence'], truncate=True)
# plt.title("Incidence vs Per Capita for 2017 by country (linearly fitted)")
# plt.ylabel('Incidence per 1000')
# plt.show()


# summary statistics for df_main
# print(df_main.describe())

#
# # incidence of malaria per 1000
# # indigenous countries
# x1 = df.loc['Angola',years].plot()
# x2 = df.loc['Burundi',years].plot()
# x3 = df.loc['Democratic Republic of the Congo',years].plot()
# x4 = df.loc['India'].plot()
# x5 = df.loc['United Republic of Tanzania'].plot()
# x6 = df.loc['Yemen'].plot()
# plt.title('Reported Malaria incidence by country')
# plt.xlabel('Years')
# plt.ylabel('Malaria incidence per 1000')
# plt.legend()
# plt.show()
#
# # incidence of malaria per 1000
# # regions
# m1 = df1.loc['Africa',years].plot()
# m2 = df1.loc['(WHO) Global',years].plot()
# m3 = df1.loc['Americas', years].plot()
# m4 = df1.loc['Europe',years].plot()
# m5 = df1.loc['Western Pacific', years].plot()
# plt.title('Malaria incidence by region')
# plt.xlabel('Years')
# plt.ylabel('Malaria Incidence per 1000')
# plt.legend()
# plt.show()
#
# # cases of malaria 2000,2005,2010-2017
# # indigenous countries
# c1 = df2.loc['Angola',years].plot()
# c2 = df2.loc['Burundi',years].plot()
# c3 = df2.loc['Democratic Republic of the Congo',years].plot()
# c4 = df2.loc['India'].plot()
# c5 = df2.loc['United Republic of Tanzania'].plot()
# c6 = df2.loc['Yemen'].plot()
# plt.title('Reported Malaria cases by country')
# plt.xlabel('Years')
# plt.ylabel('Reported cases')
# plt.legend()
# plt.show()


h1 = df2['2017']
print(h1.describe())
# plt.hist(h1,color='blue', bins=5)
# plt.show()

df_pow = h1.apply(np.sqrt)
df_pow.plot.hist(alpha=0.5, bins=15, grid=True, legend=None)
plt.xlabel("Malaria cases")
plt.title("Malaria cases 2017 by country")
plt.show()