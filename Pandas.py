import datacompy
import pandas as pd
# pd.options.display.max_rows = 9999

# df1=pd.read_excel(r"C:\Users\sharvive\OneDrive - BHP\TDM Project\SIT Evidence\Centric\Weekly Grade\Combined STS_Source.xlsx")
# df2=pd.read_excel(r"C:\Users\sharvive\OneDrive - BHP\TDM Project\SIT Evidence\Centric\Weekly Grade\OD_Combined_STS.xlsx")

# df1 = pd.read_csv("Combined STS_Source.csv")
# df2 = pd.read_csv("OD_Combined_STS.csv")
#
# # difference = df1[df1 != df2]
# # print(difference)
#
# comparison = datacompy.Compare(df1, df2, join_columns="Activity")
#
# print(comparison.report())

# df1=pd.read_csv(r"C:\Users\sharvive\PycharmProjects\pythonProject\python\qa.csv")

# print(df2)
# print(df2)
# print(df1.columns)
# print(sorted(df1.columns))
# print(sorted(df2.columns))
# print(df2.to_string())
# print(pd.options.display.max_rows)
# print(df1.info())
# print(df2.info())

# Remove all rows with NULL values:
# df1.dropna(inplace=True)
# # print(df2.to_string())
# print(df1.info())
# df2.dropna(inplace=True)
# # print(df2.to_string())
# print(df2.info())

# Mean = the average value (the sum of all values divided by number of values).
# raw = df1['U3O8'].mean()
# print(raw)
# qa = df2['U3O8'].mean()
# print(qa)

# Mode = the value that appears most frequently.
# raw = df1['CO2'].mode()
# print(raw)
# qa = df2['CO2'].mode()
# print(qa)

# Show the relationship between the columns:
# print(df1.corr())


# To find specific location
# print(df1.iloc[3])

# Iterate through each row
# for index, row in df1.iterrows():
#     print(index, row[['CO2','TONNES_DRY']])
#
# print("*******************************************************************")
# print("end of df1")
# print("*******************************************************************")
#
# for index, row in df2.iterrows():
#     print(index, row[['CO2', 'TONNES_DRY']])
#
# print("*******************************************************************")
# print("end of df2")
# print("*******************************************************************")
# Sorting/Describing Data
# print(df1.sort_values(['REPORTDATE', 'PERIODCODE'], ascending=False))

# Making changes to the data TONNES_DRY,TONNES_DRY_BEST,CU,U3O8,AU,AG,FE,CHL,CO2,FESIO2,SERICITE,SIDERITE,SIO2,TCM,CUS,S

# df1['Total'] = df1['TONNES_DRY'] + df1['TONNES_DRY_BEST'] + df1['CU'] + df1['U3O8'] + df1['AU'] + df1['AG'] + df1['FE'] + df1['CHL']

# df1['Total'] = df1['TONNES_DRY'] + df1['TONNES_DRY_BEST'] + df1['CU'] + df1['U3O8'] + df1['AU'] + df1['AG'] + df1['FE'] + df1['CHL']
# df2['Total'] = df2['TONNES_DRY'] + df2['TONNES_DRY_BEST'] + df2['CU'] + df2['U3O8'] + df2['AU'] + df2['AG'] + df2['FE'] + df2['CHL']
# # print(df1.head(500))
# # print(df2.head(500))
# print(df1['Total'])
# print(df2['Total'])


df1 = pd.read_csv("stope_geo_raw.csv")

print(df1.columns)
# print(sorted(df1.columns))
# print(df1.to_string())
# # print(pd.options.display.max_rows)
# print(df1.info())
