import datacompy
import pandas as pd
# pd.options.display.max_rows = 9999

df1=pd.read_csv(r"C:\Users\sharvive\BHP\Nonabur, Navin - ShareVivek\COAL\RAW_596.csv")
df2=pd.read_csv(r"C:\Users\sharvive\BHP\Nonabur, Navin - ShareVivek\COAL\QA_596.csv")


# comparison=datacompy.Compare(df1, df2, join_columns="DAY")
#
# print(comparison.report())

print(df1)
print(df2)


