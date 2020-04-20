import pytest
from Utils import shell_tool
import os


if __name__ == "__main__":
    test_case1 = "TestSuite/im_select_dept_role/test_select_dept_role.py"
    test_case2 = "TestSuite/im_select_dept_role/test_regression.py"
    kf_pc_case = "TestSuite/pc_customer_service_center/test_im.py"
    xml_allure = './allure/xml/'
    html_allure = './allure/html/'

    def del_file(path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                del_file(c_path)
            else:
                os.remove(c_path)
    del_file(xml_allure)
    pytest.main(["-s", "-n", "6", '--alluredir',
                 xml_allure, html_allure, kf_pc_case])
    # pytest.main(["-s", '--alluredir',
    #              xml_allure, html_allure, test_case2])
    cmd1 = 'allure generate %s -o %s --clean' % (
        xml_allure, html_allure)
    cmd2 = 'allure serve %s' % (xml_allure)
    shell_tool.invoke(cmd1)
    shell_tool.invoke(cmd2)

