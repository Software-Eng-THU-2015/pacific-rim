import hashlib
# import httplib2  # for python2
import http.client  # for python3
import json
from wechatpy.client import WeChatClient

APP_ID = "wx86b31512dc59cccf"
APP_SECRET = "d4624c36b6795d1d99dcf0547af5443d"
TOKEN = "maxipeng"
client = WeChatClient(APP_ID, APP_SECRET)


def check_signature(request):
    print("hi")
    try:
        sign = request.GET["signature"]
        timestamp = request.GET["timestamp"]
        nonce = request.GET["nonce"]
    except KeyError:
        return False

    token = TOKEN
    print(token)
    tmp = [timestamp, nonce, token]
    tmp.sort()
    print(tmp)
    res = tmp[0] + tmp[1] + tmp[2]
    '''print(hashlib.sha1('cao').hexdigest())
    m = hashlib.sha1(res)
    print(m)'''
    return True


def get_token():
    # conn = httplib.HTTPConnection("wx.chendaxixi.me")  # for python2
    conn = http.client.HTTPConnection("wx.chendaxixi.me")  # for python3
    conn.request("GET", "/token")
    return conn.getresponse().read()


def menu_create(body):
    client.menu.delete()
    return client.menu.create(body)


def menu_query():
    return client.menu.get()


def menu_delete():
    return client.menu.delete()


def custom_send_text(user, content):
    return client.message.send_text(user, content)


def custom_send_image(user, filename):
    f = open(filename)
    res = client.media.upload("image", f)
    f.close()
    data = json.loads(res)
    try:
        return client.message.send_image(user, data["media_id"])
    except NameError:
        return res


def get_stat(deviceid):
    _client = WeChatClient(APP_ID, APP_SECRET, get_token())
    return _client.device.get_stat(deviceid)


def get_open_id(devicetype, deviceid):
    _client = WeChatClient(APP_ID, APP_SECRET, get_token())
    return _client.device.get_user_id(devicetype, deviceid)


def trans_msg(devicetype, deviceid, user, content):
    _client = WeChatClient(APP_ID, APP_SECRET, get_token())
    return _client.device.send_message(devicetype, deviceid, user, content)


def create_qr_by_device_id(deviceid):
    _client = WeChatClient(APP_ID, APP_SECRET, get_token())
    res = _client.device.create_qrcode([deviceid])
    try:
        ticket = json.loads(res)["code_list"][0]["ticket"]
        # to do
        return ticket
    except NameError:
        return res
