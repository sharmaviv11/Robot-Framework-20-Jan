import pyodbc
import pytest
from numpy.core.defchararray import splitlines

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
# test_sql()


def test_sql_list():
    cursor = conn.cursor()
    list = []
    select_query = "select * from dbo.CONTRACT where CONTRACTCODE= "
    ids = ["CONTRACTCODE", "DESCRIPTION", "COMPANYCODE"]
    for x in ids:
        var = select_query + x
        cursor.execute(var)
        list.extend(cursor.fetchall())
    print(list[23])


test_sql_list()
