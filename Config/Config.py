# SX_IM_API="http://192.168.100.69:31200"

SX_IM_API = "http://test.gateway.sunxing.net/sunxing-im"

SX_PC_kf_API= "http://192.168.100.209:8300"

SX_PC_kf_IM_API = "http://test.gateway.sunxing.net/sunxing-im"

Excel_Path = "/Users/liuchengxu/work/sunxing/IM/Config/Customer_Service_Center.xlsx"

sx_zs_api = "http://test.gateway.sunxing.net/sunxing-service-merchants"

SX_PC_IM_headers = {
    "Content-Type": "application/json",
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IntcInJvbGVzXCI6W3tcInBhZ2VOdW1cIjoxLFwicGFnZVNpemVcIjoxMCxcImlkXCI6MjQ1OCxcInJvbGVJZFwiOlwiOGVlMjgzYzQtMzUzNi00NjJmLTkzZGYtODU2NDUwMDQxZjZjXCIsXCJkaW5UYWxrUm9sZUlkXCI6XCI3OTUzNjU1MDhcIixcInJvbGVOYW1lXCI6XCLlrZDnrqHnkIblkZhcIixcImRpc2FibGVkXCI6MCxcImNyZWF0ZUJ5XCI6XCJkaW5UYWxrXCIsXCJjcmVhdGVUaW1lXCI6XCIyMDIwLTAzLTE0VDA0OjQ0OjMxLjAwMCswODAwXCJ9LHtcInBhZ2VOdW1cIjoxLFwicGFnZVNpemVcIjoxMCxcImlkXCI6MjQ4MCxcInJvbGVJZFwiOlwiMWMxMDk3NGUtZjgxOS00MzljLTk5OWYtMzcwZmE3NGZkYWY1XCIsXCJkaW5UYWxrUm9sZUlkXCI6XCI5NDc2ODQxMTVcIixcInJvbGVOYW1lXCI6XCJWUFwiLFwiZGlzYWJsZWRcIjowLFwiY3JlYXRlQnlcIjpcImRpblRhbGtcIixcImNyZWF0ZVRpbWVcIjpcIjIwMjAtMDMtMTRUMDQ6NDQ6MzMuMDAwKzA4MDBcIn1dfSIsIm5hbWUiOiLkuKXkuq4oWWFuLExpYW5nKSIsImNoYW5uZWwiOiJOWS1QQyIsImRlcGFydG1lbnQiOiIyMjI5OTQ5MTgiLCJleHAiOjE2MTE1NTcwNzgsInVzZXJpZCI6IjI4MzczMTAxMzYxNjMxMDY1MTM3In0.LtzcnqDhlLNknmKWx_Mg2UxAQ9MWkKmNzJIErGdoPrk"
}

Login_Headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IntcInJvbGVzXCI6W3tcImlkXCI6MjEzMixcInJvbGVJZFwiOlwiYWU3MWEyOTQtZGY4My00YWI4LTk2MzgtNTE5M2YxZTE4YmFlXCIsXCJkaW5UYWxrUm9sZUlkXCI6XCI5NDc2ODQxMTVcIixcInJvbGVDb2RlXCI6bnVsbCxcInJvbGVOYW1lXCI6XCJWUFwiLFwicm9sZUNvbnRlbnRcIjpudWxsLFwicm9sZURlcHRpZFwiOm51bGwsXCJyb2xlRGVwdG5hbWVcIjpudWxsLFwiZGlzYWJsZWRcIjowfV19IiwibmFtZSI6IuS4peS6rihZYW4sTGlhbmcpIiwiY2hhbm5lbCI6Ik5ZLVBDIiwiZGVwYXJ0bWVudCI6IlsyMjI5OTQ5MThdIiwiZXhwIjoxNTg5MjY0NDI4LCJ1c2VyaWQiOiIyODM3MzEwMTM2MTYzMTA2NTEzNyJ9.np_qoy3_BpyFPNtVzmDOWwcQSjrh1oTQad-z6zoM4bw"
}
DB_redis_host='192.168.100.70'

DB_redis_pwd='Sunxing321'

DB_redis_port=6379

SX_DB_HOST="47.102.193.100"

SX_DB_USER="sunxing_ccs"

SX_DB_PASS="DPNLRMaZPZdX3WHk"

login_headers = {
    'content-type': 'application/json',
}





IM_json = [
    (
        "1",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487",
        "鲶鱼pc发给钉钉 工作类型：工作通知 有接收人和部门id"),
    (
        "NY-PC",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909,240450889,241974895",
        "061052015035430487",
        "鲶鱼pc发给钉钉 传多个部门"),
    (
        "NY-PC",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487,28373101361631065137,manager2564",
        "鲶鱼pc发给钉钉 传多个接收人"),
    (
        "NY-PC",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅！",
        "236295909,240450889,241974895",
        "061052015035430487,28373101361631065137,manager2564",
        "鲶鱼pc发给钉钉 传多个部门多个接收人"),
    (
        "NY-PC",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "",
        "鲶鱼pc发给钉钉 工作类型：工作通知 有部门id没有接收人id"),
    (
        "NY-PC",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "",
        "061052015035430487",
        "鲶鱼pc发给钉钉 工作类型：工作通知 有接收人id没有部门id"),
    (
        "NY-APP",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487",
        "鲶鱼APP发给钉钉 工作类型：工作通知 有接收人和部门id"),
    (
        "NY-APP",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909,240450889,241974895",
        "061052015035430487",
        "鲶鱼APP发给钉钉 传多个部门"),
    (
        "NY-APP",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487,28373101361631065137,manager2564",
        "鲶鱼APP发给钉钉 传多个接收人"),
    (
        "NY-APP",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909,240450889,241974895",
        "061052015035430487,28373101361631065137,manager2564",
        "鲶鱼APP发给钉钉 传多个部门多个接收人"),
    (
        "NY-APP",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "",
        "061052015035430487",
        "鲶鱼APP发给钉钉 工作类型：工作通知 有接收人id没有部门id"),
    (
        "NY-APP",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "",
        "鲶鱼APP发给钉钉 工作类型：工作通知 有部门id没有接收人id"),
    (
        "",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487",
        "必传字段有一个没传"),
    (
        "NY-PC",
        "",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487",
        "必传字段有一个没传"),
    (
        "NY-PC",
        "1",
        "",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487",
        "必传字段有一个没传"),
    (
        "NY-PC",
        "1",
        "1",
        "",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487",
        "必传字段有一个没传"),
    (
        "NY-PC",
        "1",
        "1",
        "1",
        "",
        "哈哈哈刘程旭好帅",
        "236295909",
        "061052015035430487",
        "必传字段有一个没传"),
    (
        "NY-PC",
        "1",
        "1",
        "1",
        "061052015035430487",
        "",
        "236295909",
        "061052015035430487",
        "必传字段有一个没传"),
    (
        "NY-PC",
        "1",
        "1",
        "1",
        "061052015035430487",
        "哈哈哈刘程旭好帅",
        "",
        "",
        "部门id和接收人id是必须要传一个"),
]





app_driver ={
    'platformName':'Android',
    'appPackage':'com.baidu.searchbox',
    'appActivity':'com.baidu.searchbox.MainActivity',
    "unicodeKeyboard":"True",# appium提供的一种输入法，可以传中文。测试时直接用这个输入法
    "resetKeyboard":"True",# 程序结束时重置原来的输入法
    "noReset":"True", # 不初始化手机app信息（类似不清楚缓存）
    'automationName':'appium',
    'deviceName':'QDY4C17807005548',
    'platformVersion':'7',
    "autoGrantPermissions":"True" # 让appium自动授权app权限
}





