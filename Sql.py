from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn
import pyodbc


@library
class Sql:

    def __init__(self):
        self.builtin_lib = BuiltIn().get_library_instance("BuiltIn")
        self.string_lib = BuiltIn().get_library_instance("String")
        self.db_lib = BuiltIn().get_library_instance("DatabaseLibrary")


    @keyword
    def database(self):
        con = pyodbc.connect('Driver={SQL Server};'
                             'Server=OLP0TAQR02;'
                             'Database=AcQuireODO;'
                             'Trusted_Connection=yes;')
        cursor = con.cursor()
        results = cursor.execute("select * from dbo.CONTRACT;")
        for i in results:
            print(i)

    @keyword
    def database_list(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                             'Server=OLP0TAQR02;'
                             'Database=AcQuireODO;'
                             'Trusted_Connection=yes;')
        cursor = conn.cursor()
        list = []
        select_query = "select * from dbo.CONTRACT where DESCRIPTION = "
        ids = ["CONTRACTCODE", "DESCRIPTION", "COMPANYCODE"]
        for x in ids:
            var = select_query + x
            cursor.execute(var)
            list.extend(cursor.fetchall())

        print(list)

