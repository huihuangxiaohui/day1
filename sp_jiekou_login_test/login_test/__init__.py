import requests
import json


def test_login4():
    '''该测试用例针对于账号或密码输入错误'''
    date={
        "grant_type": "password",
        "client_id": "295d82a74c456c89d9110cee290ab915",
        "device_id": "web_signin",
        "identity": "cfruit.yhg01",
    "password": "QAt$*43r1"
                       }
    r=requests.post(url="https://uat-sunpeopleprx-2.scgdomain.com/usercenter/token",data=date)
    print(type(r))
    print(type(r.text))
    res=json.loads(r.text)
    print(res['error'])
    print(type(res))
test_login4()