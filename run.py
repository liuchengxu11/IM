import pytest
from Utils import shell_tool


if __name__=="__main__":
    test_case1="TestSuite/im_select_dept_role/test_select_dept_role.py"
    xml_allure = './allure/xml/'
    html_allure = './allure/html/'
    pytest.main(["-v", "-s","-n","6",'--alluredir', xml_allure, html_allure, test_case1])
    cmd1 = 'allure generate %s -o %s --clean' % (
        xml_allure, html_allure)
    cmd2 = 'allure serve %s' % (xml_allure)

    shell_tool.invoke(cmd1)
    shell_tool.invoke(cmd2)