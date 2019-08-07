import unittest
import requests
import time
class Sostest(unittest.TestCase):
    head={"Authorization": "Bearer 9d98dd71f0ab7e3de06d69099a3a403f"}
    url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all"
    def testMakeSos(self):
        """测试开启SOS"""
        data={
  "message": "请求帮助!",
  "lat": 22.202002,
  "lng": 113.55784,
  "type":"baidu"
}
        r=requests.post(url=self.url+"/sos",headers=self.head,data=data)

        self.assertEqual(r.json()["code"],0)
    def testdelSos(self):
        '''测试删除sos'''
        r=requests.delete(url=self.url+"/sos/0",headers=self.head)
        self.assertEqual(r.json()["code"], 0)
def suite():
    logintestcase=unittest.makeSuite(Sostest)

    return logintestcase

print(suite())

