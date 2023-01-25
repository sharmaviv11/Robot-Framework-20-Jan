import pyodbc
import pytest
import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=OLP0TAQR02;'
                      'Database=AcQuireODO;'
                      'Trusted_Connection=yes;')


# def test_sql():
#     # cursor = conn.cursor()
#     # results = cursor.execute('select * from dbo.CONTRACT;')
#     # for i in results:
#     #     print(i)
#
#     cursor = conn.cursor()
#     count = cursor.execute('select count(*) from dbo.CONTRACT;')
#     for i in count:
#         print(i)
#     rows = cursor.execute('select * from dbo.CONTRACT;')
#     for row in rows:
#         print(row)
#     # cursor.close()
#     # conn.close()
#
#
# test_sql()


# def test_export_sql():
#     sql_query = pd.read_sql_query('''
#                                 select * from AcQuireODO.dbo.DRILLTYPE
#                                 '''
#                                   , conn)
#     df = pd.DataFrame(sql_query)
#     df.to_csv(r'C:\Users\sharvive\PycharmProjects\pythonProject\python\export_data.csv', index=False)
#
#
# test_export_sql()

def test_read_csv():
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    columns = ["DRILLTYPE", "DESCRIPTION"]
    df = pd.read_csv(r'C:\Users\sharvive\PycharmProjects\pythonProject\python\export_data.csv', usecols=columns)
    print("Contents in csv file:", df)
    plt.plot(df.DRILLTYPE, df.DESCRIPTION)
    # plt.plot(df.CONTRACTCODE, df.DESCRIPTION, df.COMPANYCODE, df.EXPIRYDATE, df.STARTDATE)
    # plt.plot(df.astype({"CONTRACTCODE": int, "COMPANYCODE": int}))
    plt.show()


test_read_csv()
# def test_sql_list():
#     cursor = conn.cursor()
#     list = []
#     select_query = "select * from dbo.CONTRACT where CONTRACTCODE= "
#     ids = ["CONTRACTCODE", "DESCRIPTION", "COMPANYCODE"]
#     for x in ids:
#         var = select_query + x
#         cursor.execute(var)
#         list.extend(cursor.fetchall())
#     print(list[23])
#
#
# test_sql_list()
