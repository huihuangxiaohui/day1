import unittest
import requests
import json
import HTMLTestRunnerNew
from datetime import *
class Sunpeople_test(unittest.TestCase):
    head = {"Authorization": "Bearer e76e4c67585ff33d7021bead50b9fbc4"}
    base_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all"

    def setUp(self):
        self.url="https://uat-sunpeopleprx-2.scgdomain.com/usercenter/token"

    def test_Login1(self):
        '''测试错误的密码'''
        data={"grant_type": "password",
	"client_id": "295d82a74c456c89d9110cee290ab915",
	"device_id": "web_signin",
	"identity": "cfruit.hyx02",
	"password": "S_sp0br"}
        r=requests.post(url=self.url,data=data)
        self.assertNotEqual(json.loads(r.text)["code"],0)

        print(self.url)


    def test_Login(self):
        '''测试输入正确的账号与密码'''
        date = {"grant_type": "password",
                "client_id": "295d82a74c456c89d9110cee290ab915",
                "device_id": "web_signin",
                "identity": "cfruit.mxn01",
                "password": "S_sp0br5"}
        r = requests.post(url=self.url, data=date)
        self.assertEqual(json.loads(r.text)["code"],0)
        print("测试地址为："+self.url)
    def test_Login3(self):
        '''测试密码为空'''
        data={"grant_type": "password",
	"client_id": "295d82a74c456c89d9110cee290ab915",
	"device_id": "web_signin",
	"identity": "cfruit.mxn01",
	"password": ""}
        r=requests.post(url=self.url,data=data)
        self.assertEqual(json.loads(r.text)["error"],"identity or password required.")
        print("测试地址为：" + self.url)
    def test_dialog4(self):
        '''测试增量会话列表是否正常'''
        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/v2.3/sync_dialogs?since=0"
        head = {"Authorization": "Bearer 2bb8add6a7925d90d350feda5b66c8fe"}
        r=requests.get(url=test_url,headers=self.head)
        self.assertEqual(json.loads(r.text)["code"],0)#如果接口返回的code=0则测试通过
        print("888")
    def test_eventlog5(self):
        '''返回的next时间进行增量拉取'''
        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/v2.2/sync_eventlogs?since=1554871889706"
        head={"Authorization": "Bearer 2bb8add6a7925d90d350feda5b66c8fe"}
        r=requests.get(url=test_url,headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print("测试地址为：" + test_url)
    def test_NoCrm6(self):
        '''crm 类型的机器人 since 不影响查询数据的结果'''
        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/v2.3/sync_eventlogs_robots?since=1560336168781"
        head = {"Authorization": "Bearer 2bb8add6a7925d90d350feda5b66c8fe"}
        r = requests.get(url=test_url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print("测试地址为：" + test_url)

    def test_channels(self):
        '''测试获取群组相关信息与人数'''
        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/v2.3/sync_eventlogs_channels?since=1560339735837"

        r = requests.get(url=test_url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print("测试地址为：" + test_url)
    def test_dialog8(self):
        '''是否新增了返回 result 中 新增了 preference 会话相关参数、has_star 是否包含标星消息、avatar_url 用户头像相关内容'''
        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/v2.4/sync_dialogs？since=1559210792922"
        head={"Authorization": "Bearer 2bb8add6a7925d90d350feda5b66c8fe"}
        r=requests.get(url=test_url,headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 404)
        print("测试地址为：" + test_url)
    def test_boards9(self):
        "是否根据 since 时间增量获取， 后端逻辑是获取该用户收到公告消息创建时间大于 since 的消息所在的公告板 然后把对应的增量公告板返回"
        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/v2.3/sync_eventlogs_boards?since=1563254964405"
        head = {"Authorization": "Bearer 2bb8add6a7925d90d350feda5b66c8fe"}
        r = requests.get(url=test_url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print("测试地址为：" + test_url)

    def test_members25(self):
        '''是否添加 members 总人数数据'''
        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/sync_members?since=1563254964405"
        head = {"Authorization": "Bearer 2bb8add6a7925d90d350feda5b66c8fe"}
        r=requests.get(url=test_url,headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print("测试地址为："+test_url)
    def test_messages23(self):
        '''输入错误的群组ID，查询群组信息数量'''

        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/v2.2/sync_messages"
        head = {"Authorization": "Bearer 2bb8add6a7925d90d350feda5b66c8fe"}
        date=date={"query": [
	{
            "vchannel_id": "=bG9JyIMh",
            "start_ts": 1520391042384
        }],"size":20}
        r=requests.post(url=test_url,headers=self.head,data=date)
        self.assertEqual(json.loads(r.text)["code"], 3)
        print("测试地址为:"+test_url)
    def test_checkdevice13(self):
        '''测试更新设备接口是否正常使用'''
        test_url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/check_device?device_id=0"
        head={"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r=requests.get(url=test_url,headers=self.head)
        self.assertEqual(json.loads(r.text)["code"],0)
        print(test_url)

    def test_checkdevice1(self):
        '''测试更新设备接口未传device_id参数'''
        test_url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/check_device?device_id="
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=test_url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 2)
        print(test_url)
    def test_connetcion(self):
        """测试连接信息是否正常"""
        test_url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/connection_info"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=test_url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(test_url)
    def test_menbers10(self):
        '''web端专用，获取通讯录人数，对应数据库查询语句，参数非必传'''
        test_url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/members?offset=0&size=2"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=test_url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(test_url)

    def test_menbers2(self):
        '''web端专用，获取通讯录人数，未传入size参数，查询通讯录所有人员'''
        test_url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/members?offset=3"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=test_url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(test_url)

    def tets_message12(self):
        '''测试转发'''
        test_url = "https://uat-sunpeopleprx-2.scgdomain.com/api/rtm/message"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        date = {
            "token": "4f022cc8c8b0cb221f4082b7cb2d750a",
            "sender": "bearychat.test07@suncity-group.com",
            "text": '''这条才是长文本. \n 週期：2018-03
        飯局比例：0 / 41 (0%)
        未有飯局戶口
        [(AA) 001組 2079](rollsmary://9500026673) 龔俊龍(龔生)
        [(AA) 001組 560789](rollsmary://7000031018) 周金輝(周總)
        [(AA) 001組 6208](rollsmary://9000030727) 鍾美財(財哥)
        [(AA) 001組 803](rollsmary://9000013298) 龍瑞明(龍少)
        [(AA) 001組 9223](rollsmary://2800020462) 龍富勇(小龍)(小龍哥)
        [(AAH) 029組 88](rollsmary://7000013549) 涂億萬(塗總)
        [(EO) 999組 1202](rollsmary://9500028863) WANG XIAOPEI(RAY)
        [(EO) 999組 1333](rollsmary://3100020068) 任嘉(任總)
        [(EO) 999組 6677](rollsmary://5100020313) 和勇(勇哥)
        [(JJ) 456組 123](rollsmary://3700020247) 許良彪(彪哥)
        [(JJ) 456組 6609](rollsmary://9500028942) ZENG BAO CHENG(成哥)
        [(XX) 345組 16018](rollsmary://5000036063) 王玉龍(龍哥)
        [(XX) 345組 16269](rollsmary://5000034855) 周行方(幕)
        [(XX) 345組 17789](rollsmary://5000032732) 胡榮利(胡總)''',

            "title": "send to channel and 04 09",
            "emails": "cfruit.lx01@suncity-group.com",
            "group_id": "",
            "bubble_color": "#FFFFFF",
            "text_color": "#FFFFFF",
            "ts_color": "#FFFFFF"
        }
        r = requests.post(url=test_url, headers=self.head, data=date)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(test_url)

    def test_current(self):
        '''测试当前当前用户的信息，传入token为mxn01'''
        test_url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/current_user"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=test_url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(test_url)
    def test_preference(self):
        '''这个接口目前只知道是控制web端口权限的开启和关闭，具体参数不是很了解'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/current_user/preference"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        data = {"web_notification": "on"}
        r=requests.patch(url=url,headers=self.head,data=data)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_robotes(self):
        '''测试是否能获取到全部的可用机器人'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/robots"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}

        r = requests.get(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_ess(self):
        '''测试能否获取ESS现有的功能列表'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/ess"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}

        r = requests.get(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_markReadDialog(self):
        '''是否按照时间节点把ID==bGE0dHi0的对话设置为已读'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/vchannels/=bGE0dHi0/mark_read"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}

        date = {"ts": "1508387709380"}
        r = requests.post(url=url, headers=self.head, data=date)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_MakeUnRead(self):
        """是否将ID=bGE0dHi0的对话设置为未读"""
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/vchannels/=bGE0dHi0/mark_unread"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}

        date = {"ts": "1508387709380"}
        r = requests.post(url=url, headers=self.head, data=date)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_MessageRead(self):
        '''是否将对话里的消息编辑为已读'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/vchannels/=bG9JyIMh/messages/1476439065659.0127/mark_read"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}

        r = requests.post(url=url, headers=self.head, data=None)
        self.assertEqual(json.loads(r.text)["code"], 6)
        print(url)
    def test_StarMessage(self):
        "测试是否可以标注信息"
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/stars"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        data={"key":"1476439142167.0002","vchannel_id":"=bG0wdX8m"}
        r = requests.post(url=url, headers=self.head, data=data)
        self.assertEqual(json.loads(r.text)["code"], 6)
        print(url)
    def test_Preference(self):
        """测试设置群组功能是否生效"""
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/vchannels/=bGE0dHi0/preference"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        date = {"sound": "test", "notification": "off", "pin": "on"}
        r = requests.patch(url=url, headers=self.head, data=date)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_DeleteMember(self):
        '''测试删除群组成员是否生效'''
        url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/channels/=bw5Cs/members"
        data={"user_id":"=bw5Ph"}
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r=requests.delete(url=url,headers=self.head,data=data)
        self.assertEqual(json.loads(r.text)["code"], 4)
        print(url)
    def test_AddMember(self):
        '''测试添加群组成员功能是否生效'''
        url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/channels/=bw5Cs/members"
        data={"user_ids":"=bw5R1"}
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r=requests.post(url=url,headers=self.head,data=data)
        self.assertEqual(json.loads(r.text)["code"],4 )
        print(url)
    def test_Preferbnce(self):
        '''测试修改群组的权限'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/vchannels/=bGE0dHi0/preference"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        date = {"sound": "test", "notification": "off", "pin": "on"}
        r = requests.patch(url=url, headers=self.head, data=date)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_DeleteMember(self):
        """测试删除群组成员"""
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/channels/=bw5Cs/members"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        date = {"user_id": "=bw5Ph"}
        r = requests.delete(url=url, headers=self.head, data=date)
        self.assertEqual(json.loads(r.text)["error"],"沒有權限" )
        print(url)
    def test_AddUsers(self):
        '''测试根据ID群组成员'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/channels/=bw5Cs/members"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        date = {"user_id": "=bw5Ph"}
        r = requests.post(url=url, headers=self.head, data=date)
        self.assertEqual(json.loads(r.text)["error"], "沒有權限")
        print(url)
    def test_Starred(self):
        """是否可查询标注信息的总数"""
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/stars?start=0&limit=20"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"],0)
        print(url)
    def test_Mentionme(self):
        '''是否可查询@当前用户信息的数量'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/mentions?start=0&limit=20"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_ReadUser(self):
        '''查询发送消息的用户读取数量'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/vchannels/=bw5Jq/messages/1551690554168.0131/read_users"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_AggSeach(self):
        '''测试群组中zu88的数量'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/search_agg?query=zu88&size=1000"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_Addbaiqqing(self):
        '''测试添加服务端表情'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/current_user/stickers"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        data = {'width': '100',
                'height': '100',
                "url": "http://www.baidu.com",
                "size": "100.0",
                "source_url": "http://www.baidu.com",
                "uuid": "d5f48de7-8439-48c6-8a63-54f5ea0e9142"
                }

        r = requests.post(url=url, headers=self.head, data=data)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_Delbiaoqiang(self):
        '''测试删除服务端表情'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/current_user/stickers/d5f48de7-8439-48c6-8a63-54f5ea0e9142"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.delete(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_LatestMessage(self):
        """测试是否可以获取对话最新消息"""
        url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/vchannels/=bw53i/messages/query"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        data={
  "query": {
    "latest": {
      "limit": 20
    }
  }
}
        r = requests.post(url=url, headers=self.head, data=data)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url,"接口返回："+r.text)
    def test_GetSos(self):
        '''测试是否可以新建或者更新SOS状态'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/sos"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        data = {
            "message": "help me!",
            "lat": 22.202002,
            "lng": 113.55784,
            "type": "baidu"
        }

        r = requests.post(url=url, headers=self.head, data=data)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_Sos(self):
        """测试是否可以获取SOS状态"""
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/sos"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.get(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_DelSos(self):
        '''测试是否可以停止SOS求救'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/sos/0"
        r=requests.delete(url,headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_KickWeb(self):
        '''测试web端推送'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/web/offline"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.post(url=url, headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_RTM(self):
        '''RMT自定义颜色测试'''
        data = {
            "token": "4f022cc8c8b0cb221f4082b7cb2d750a",
            "text_list": [
                {
                    "ts_color": "#0000FF",
                    "bubble_color": "#DBE8FF",
                    "text_color": "#FF0000",
                    "text": "气泡颜色文字颜色时间戳颜色均修改",
                    "send_seq": 1
                },
                {
                    "ts_color": "#00FFFF",
                    "bubble_color": "#00ACED",
                    "text_color": "#FF0000",
                    "text": "三个样式都修改，同时测试链接和 AT 样式\n[(AA) 001組 2079](rollsmary://9500026673) 龔俊龍(龔生)\nRollsmary\n@{==bw52O=}AT@<==bw52O=>\nTEXT\nMSG ...",
                    "send_seq": 2
                },
                {
                    "text_color": "#0000FF",
                    "text": "只修改文字颜色对比测试的时候确认 iOS Android 和 Web 样式都一致",
                    "send_seq": 3

                },
                {
                    "bubble_color": "#00ACED",
                    "text": "只修改气泡颜色对比测试的时候确认 iOS Android 和 Web 样式都一致",
                    "send_seq": 4

                },
                {
                    "ts_color": "#00ACED",
                    "text": "只修改时间戳颜色对比测试的时候确认 iOS Android 和 Web 样式都一致",
                    "send_seq": 5

                },
                {
                    "bubble_color": "#00ACED",
                    "text_color": "#00ACED",
                    "ts_color": "#00ACED",
                    "text": "三个字段都传 null，测试崩溃",
                    "send_seq": 7

                },
                {
                    "bubble_color": "#00ACED",
                    "text_color": "#00ACED",
                    "ts_color": "#00ACED",
                    "text": "测试参数全传",
                    "send_seq": 8

                }
            ],
            "names": "",
            "sender": "cfruit.yhg01@suncity-group.com",
            "group_id": "=bw5LN",
            "emails": ""
        }
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/rtm/messages"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r = requests.post(url, headers=self.head, data=data)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_Forward(self):
        '''测试转发编辑消息'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/messages/template"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        data = {"msg_key": "1545274557175.0101", "origin_vchannel_id": "=bw53a", "vchannel_ids": ["=bw5Ha"],
                "text": " – wcg02Cfruit已由系統關閉求助信息。"}
        r = requests.post(url=url, headers=self.head, data=data)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_Channels(self):
        '''测试是否可以管理群历史消息'''
        url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/channels/=bw5Cs/info_history"
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r=requests.get(url=url,headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_consultants(self):
        ''''''
        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/consultants?types=text"
        r=requests.get(url=url,headers=self.head)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)
    def test_GoogleTranslate(self):
        '''翻译功能是否可用'''
        date={
  "source": "zh-TW",
  "target": "en",
  "text_list": [
    {
      "text": "地點：馬尼拉晨麗1太陽城"
    },
    {
      "text": "交易編號：YTA500383"
    },
    {
      "text": "出碼戶：(BB) 003組 1 施閩"
    }


  ]
}

        head = {"Authorization": "Bearer 2a0503e739e719c8d2f5c69334a3e565"}
        r=requests.post(url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/google/translation/translate",headers=self.head,data=date)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print()
    def test_ESSGetEntry(self):
        '''测试是否可以获取ESS列表'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/ess/get_entry"
        r=requests.post(url=url,headers=self.head)
        self.assertEqual(r.json()["code"],0)
        print(url)
    def test_SearchMessage(self):
        '''测试搜索群组对话'''
        url="https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/search/message?query=zu88&vchannel_id==bw5Dx&start=0&limit=5"
        r = requests.post(url=url, headers=self.head)
        self.assertEqual(r.json()["code"], 0)
        print(url,r.text)
    def test_Rollsmary(self):
        '''群组是否可以获取rellsmary信息'''
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/rollsmary/customer_report/1000010855"
        r = requests.post(url=url, headers=self.head)
        self.assertEqual(r.json()["code"], 0)
        print(url)
    def test_channels(self):
        '''测试新建群组功能'''
        url=self.base_url+"/channels"
        data={
            "name": "test_channel_role",
            "mode": "admin_off",
            "user_ids":["=bwNyv", "=bwNzH"]
        }
        r=requests.get(url=url,headers=self.head,data=data)
        r = requests.post(url=url, headers=self.head)
        self.assertEqual(r.json()["code"], 0)

    def test_Assistant(self):
        '''是否可以获取当前用户的跟进记录未读数量'''
        url = self.base_url+"/assistant/badge"
        r=requests.get(url=url,headers=self.head)
        self.assertEqual(r.json()["code"],0)
        print(url)
    def test_xiugaijiaobiao(self):
        '''测试是否可以修改跟进记录未读数量'''
        url=self.base_url+"/assistant/badge"
        data={
    "functions": [
    	{
    		"function": "REQUEST",
    		"value": 3
    	},
    	{
    		"function": "COMPLAINT",
    		"value": 4
    	}
    ]
}
        r=requests.patch(url=url,headers=self.head,data=data)
        self.assertEqual(r.json()["code"],0)
        print(url)
    def test_MessagesBackward(self):
        '''测试群组消息上滑20条'''
        url=self.base_url+"/vchannels/=bw5LN/messages?backward=20"
        r=requests.get(url=url,headers=self.head)
        self.assertEqual(r.json()["code"], 0)
        print(url)
    def test_LatestMessage(self):
        """测试是否可以获取对话最新消息"""
        url = "https://uat-sunpeopleprx-2.scgdomain.com/api/teams/all/vchannels/=bw53i/messages/query"
        data = {
            "query": {
                "latest": {
                    "limit": 20
                }
            }
        }
        r = requests.post(url=url, headers=self.head, data=data)
        self.assertEqual(json.loads(r.text)["code"], 0)
        print(url)

def suite():
    logintestcase=unittest.makeSuite(Sunpeople_test)



    return logintestcase


f=open(str(datetime.now().date())+"接口测试.html","wb")
runner=HTMLTestRunnerNew.HTMLTestRunner(stream=f,title="测试报告",description="测试详情")
runner.run(suite())






