from Config.excel_config.get_excel import Get_excel
import json



class Sheet():

    def dingding_userid(self,row_id,column_id):
        excel=Get_excel()
        set=excel.get_excel("dingding")
        parameter=set.cell(row=row_id, column=column_id).value
        return eval(parameter)



