import hashlib
<<<<<<< HEAD
# import httplib  # for python2
import httplib2  # for python3
import os

=======
import httplib2  # for python2
>>>>>>> 6cb9daf27f8256f3b61b82508b5f92133fefc1a2
#import http
import json
import os
from wechatpy.client import WeChatClient

global APP_ID
global APP_SECRET
global TOKEN
APP_ID = os.environ.get('APP_ID')
APP_SECRET = os.environ.get('APP_SECRET')
TOKEN = os.environ.get('TOKEN')

client = WeChatClient(APP_ID, APP_SECRET)


def check_signature(request):
    try:
        sign = request.GET["signature"]
        timestamp = request.GET["timestamp"]
        nonce = request.GET["nonce"]
    except KeyError:
        return False

    token = TOKEN
    tmp = [timestamp, nonce, token]
    tmp.sort()
    tmp_str = "%s%s%s" % tuple(tmp)
    tmp_str = hashlib.sha1(tmp_str).hexdigest()
    return tmp_str == sign


def get_token():
    conn = httplib2.HTTPConnection("wx.chendaxixi.me")  # for python2
=======
<<<<<<< HEAD
    conn = httplib2.HTTPConnection("wx.chendaxixi.me")  # for python2
    # conn = http.client.HTTPConnection("wx.chendaxixi.me")  # for python3
<<<<<<< HEAD
=======
    conn = httplib.HTTPConnection("wx.chendaxixi.me")  # for python2
>>>>>>> d8f9c60f1c9dd455f6256172ec2b08b3c60719a6
    #conn = http.client.HTTPConnection("wx.chendaxixi.me")  # for python3
>>>>>>> b6cadcbdf48cd167b45f157d19aff9fbfea7dee2
=======
>>>>>>> 6cb9daf27f8256f3b61b82508b5f92133fefc1a2
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
