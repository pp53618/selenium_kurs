import xlsx
import pandas as pd
from page_object_pattern.utils.search_data import SearchData


class ExcelReader:

    @staticmethod
    def get_data():
        wb = pd.read_excel(r"C:\Users\paula\PycharmProjects\selenium_kurs\page_object_pattern\utils\Dane.xlsx",
                           engine='openpyxl')
        data = []
        print(wb.values)
        for i in range(len(wb.index)):
            search_data = SearchData
            data.append(search_data)
        return wb
