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

    # @keyword
    # def search_worksheet(self):
    #     self.sel_lib.wait_until_element_is_enabled(
    #         "css:#ext-element-1 > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div.SideTabPanel__container____Dek6.styles__container___oj4Qq > div.SideTabPanel__active-panel___nHvuD.styles__active-panel____TVAp > div > div > div > div.DataTable__table-config-no-edge___eAdpq > div.DataTable__input-container___xSdJ5 > input")
    #     self.sel_lib.click_element(
    #         "css:#ext-element-1 > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div.SideTabPanel__container____Dek6.styles__container___oj4Qq > div.SideTabPanel__active-panel___nHvuD.styles__active-panel____TVAp > div > div > div > div.DataTable__table-config-no-edge___eAdpq > div.DataTable__input-container___xSdJ5 > input")
    #     # self.sel_lib.input_text(
    #     #     "css:#ext-element-1 > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div.SideTabPanel__container____Dek6.styles__container___oj4Qq > div.SideTabPanel__active-panel___nHvuD.styles__active-panel____TVAp > div > div > div > div.DataTable__table-config-no-edge___eAdpq > div.DataTable__input-container___xSdJ5 > input")(PH_DIM_ACTIVITY_QA_UAT)
    #
    # @keyword
    # def enter_sql(self):
    #     self.sel_lib.input_text(
    #         "css:#ext-element-1 > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div.SideTabPanel__container____Dek6.styles__container___oj4Qq > div.SideTabPanel__active-panel___nHvuD.styles__active-panel____TVAp > div > div > div > div.DataTable__table-config-no-edge___eAdpq > div.DataTable__input-container___xSdJ5 > input")
    #
    # @keyword
    # def select_worksheet(self):
    #     self.sel_lib.wait_until_element_is_enabled(
    #         'xpath://*[@id="ext-element-1"]/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/span')
    #     self.sel_lib.click_element(
    #         'xpath://*[@id="ext-element-1"]/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/span')
    #
    # @keyword
    # def open_worksheet(self):
    #     # click on open button
    #     self.sel_lib.wait_until_element_is_enabled(
    #         "css:#ext-element-1 > div:nth-child(3) > div > div > div > div.footer_1g8ixvv-o_O-absoluteFooter_ay4wjb-o_O-footer_d1fb1e > div:nth-child(1) > div:nth-child(1) > button")
    #     self.sel_lib.click_element(
    #         "css:#ext-element-1 > div:nth-child(3) > div > div > div > div.footer_1g8ixvv-o_O-absoluteFooter_ay4wjb-o_O-footer_d1fb1e > div:nth-child(1) > div:nth-child(1) > button")
    #
    # @keyword
    # def run_worksheet(self):
    #     # click in the worksheet
    #     self.sel_lib.wait_until_element_is_enabled(
    #         'xpath://*[@id="sleet-component-1187"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div/pre')
    #     self.sel_lib.click_element(
    #         'xpath://*[@id="sleet-component-1187"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div/pre')
    #     self.builtin_lib.sleep("2s")
    #     # click on Run button to execute SQL
    #     self.sel_lib.wait_until_element_is_enabled(
    #         'xpath://*[@id="sleet-component-1187"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[2]/button/img')
    #     self.sel_lib.click_element(
    #         'xpath://*[@id="sleet-component-1187"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[2]/button/img')
    #
    # @keyword
    # def download_csv(self):
    #     # click on download button
    #     self.sel_lib.wait_until_element_is_enabled(
    #         'xpath://*[@id="sql-worksheet-result-pane-content"]/div[3]/div/div[1]/div[2]/button')
    #     self.sel_lib.click_element('xpath://*[@id="sql-worksheet-result-pane-content"]/div[3]/div/div[1]/div[2]/button')
    #     self.builtin_lib.sleep("2s")
    #     # select CSV radio button
    #     self.sel_lib.click_element(
    #         'xpath://*[@id="ext-element-1"]/div[5]/div/div/div/div[2]/div/div[3]/div[2]/div/div[2]/input')
    #     self.builtin_lib.sleep("2s")
    #     # show in dialog
    #     self.sel_lib.wait_until_element_is_enabled(
    #         'xpath://*[@id="ext-element-1"]/div[5]/div/div/div/div[2]/div/div[1]/button')
    #     self.sel_lib.click_element('xpath://*[@id="ext-element-1"]/div[5]/div/div/div/div[2]/div/div[1]/button')

    # qa_results = self.sel_lib.get_text('xpath://*[@id="ext-element-1"]/div[5]/div/div/div/div[2]/div')
    # qa_results_list = [qa_results]

    # @keyword
    # def copy_csv(self):
    #     # click into text area and copy resultssplit
    #     scroll_locator = 'xpath://*[@id="ext-element-1"]/div[5]/div/div/div/div[2]/div'
    #     self.sel_lib.scroll_element_into_view(scroll_locator)
    #     self.sel_lib.set_focus_to_element(scroll_locator)
    #     self.sel_lib.wait_until_element_is_enabled(scroll_locator)
    #     self.sel_lib.click_element(scroll_locator)
    #     qa_results = self.sel_lib.get_text(scroll_locator)
    #     integer = self.builtin_lib.convert_to_integer(qa_results)
    #     # split_lines = "\n".splitlines(integer)
    #     # qa_results_list = self.builtin_lib.create_list("\n".splitlines(qa_results))
    #     # splitlines = self.string_lib.split_to_lines(qa_results_list)
    #     # get_qa_results_lines = self.string_lib.get_line_count(split_lines)
    #     self.builtin_lib.sleep("2s")
    #     # close dialog box
    #     dialog_box_locator = 'xpath://*[@id="ext-element-1"]/div[5]/div/div/div/div[3]/div/div[1]/button'
    #     self.sel_lib.wait_until_element_is_enabled(dialog_box_locator)
    #     self.sel_lib.click_button(dialog_box_locator)
    #     self.builtin_lib.sleep("4s")

        # split = splitlines.qa_results_list
        # # split = self.string_lib.split_to_lines(qa_results_list)
        # get_qa_results_lines = self.string_lib.get_line_count(split)




