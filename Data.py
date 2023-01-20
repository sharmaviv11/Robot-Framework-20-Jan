import datacompy
import pandas as pd
pd.options.display.max_rows = 9999

df1=pd.read_csv(r"C:\Users\sharvive\BHP\Nonabur, Navin - ShareVivek\Centric\FACT_HAULAGE\RAW Data\HAULAGE_27 July_50481.csv")
df2=pd.read_csv(r"C:\Users\sharvive\BHP\Nonabur, Navin - ShareVivek\Centric\FACT_HAULAGE\RAW Data\src_cols.csv")

# comparison=datacompy.Compare(df1, df2, join_columns="QUARTER")
#
# print(comparison.report())

# print(df1.info())
print(pd.options.display.max_rows)

# df1.dropna(inplace=True)
print(df1.info())
