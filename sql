from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class Test:

    def __init__(self):
        self.sel_lib = BuiltIn().get_library_instance("SeleniumLibrary")
        self.builtin_lib = BuiltIn().get_library_instance("BuiltIn")
        self.string_lib = BuiltIn().get_library_instance("String")
        self.db_lib = BuiltIn().get_library_instance("DatabaseLibrary")

    @keyword
    def database(self):
        output = self.db_lib.execute_sql_string("select * from dbo.CONTRACT;")
        cur =

    @keyword
    def open_new_worksheet(self):
        # worksheet drop down menu
        self.sel_lib.wait_until_element_is_enabled(
            "css:#sleet-component-1187 > div > div > div.style__tab-bar___gp1ot > div.style__control___WWaOg > div.style__control-child___KuDMk.style__control-dropdown___NkvU2 > div.inline-icon-button")
        self.sel_lib.click_element(
            "css:#sleet-component-1187 > div > div > div.style__tab-bar___gp1ot > div.style__control___WWaOg > div.style__control-child___KuDMk.style__control-dropdown___NkvU2 > div.inline-icon-button")
        # click on open new worksheet
        self.sel_lib.wait_until_element_is_enabled(
            "css:#sleet-component-1187 > div > span > div > div > div > div > div:nth-child(1)")
        self.sel_lib.click_element("css:#sleet-component-1187 > div > span > div > div > div > div > div:nth-child(1)")






