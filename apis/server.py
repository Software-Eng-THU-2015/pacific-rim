# coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response
from apis.tools import *
from django.template.loader import get_template
from django.template import Context
import json
import urllib
import urllib.parse
import urllib.request
from apis import tools
import random
from apis import views
from wechatpy import parse_message, create_reply
from wechatpy.replies import TextReply

# from wechatpy.replies import TextReply, ImageReply, VoiceReply, VideoReply, MusicReply, TransferCustomerServiceReply
#from wechatpy.replies import ArticlesReply

global sessions
sessions = dict([])

mission_detail = [
    {
        "reward_water": 5,
        "reward_fer": 0,
        "description": "双倍完成今天的运动计划",
    },
    {
        "reward_water": 5,
        "reward_fer": 5,
        "description": "跑一次3000m",
    }
]

@csrf_exempt
def handle(request):
    if request.method == "GET":
        if not tools.check_signature(request):
            return HttpResponse("invalid signature")
        else:
            return HttpResponse(request.GET["echostr"])

    msg = parse_message(request.body)
    reply = TextReply(message = msg)
    if msg.type == "event" and msg.key == "talk_with_tree":
        sessions[reply.target] = 1

    if not (reply.target in sessions):
        sessions[reply.target] = 0 
    return msg_splitter[msg.type](request)

# 对文本信息进行回复
def text_handle(request):
    msg = parse_message(request.body)
    reply = TextReply(message = msg)
    content = msg.content
    new_uid = reply.target

    if (content == "来数据"):
        views.update_database_randomly(new_uid)
        return HttpResponse(create_reply("注入了数据！", message=msg))

    elif(content == "xp好帅"):
    #    views.test2(new_uid)
        return HttpResponse(create_reply("获得了浇水次数和施肥次数！！", message=msg))

    if(new_uid in sessions and sessions[new_uid] == 1):
        if (content == "退出"):
            sessions[reply.target] = 0
            return HttpResponse(create_reply("生命之树期待与您再次相会", message=msg))
        rebot_key = "da0d72f6aacebe4301f685e2c11f22c0"
        url = "http://www.tuling123.com/openapi/api?key=%s&info=%s" % (rebot_key,urllib.parse.quote(content))
  #      return HttpResponse(create_reply(u"生命之树期待与您再次相会", message=msg))
        response = urllib.request.urlopen(url).read()         #调用urllib2向服务器发送get请求url
        reply_text = json.loads(response.decode("utf-8"))['text']
        reply_text.replace('图灵机器人','生命之树')
 #       reply_text.replace(u'图灵机器人'.encode('utf-8'),u'生命之树')
        return HttpResponse(create_reply(reply_text, message=msg))
        
    if(views.check_band_user(new_uid) == False):
        views.insert_band_user(new_uid)
        return HttpResponse(create_reply(u"太平洋手环保太平，欢迎您使用太平洋手环！", message=msg))
    else:
        return HttpResponse(create_reply(u"欢迎您重归太平洋手环！", message=msg))


# 对语音信息进行回复
def voice_handle(msg):
    return HttpResponse(create_reply("Hello World!I am voice", message=msg))


# 对图片信息进行回复
def image_handle(msg):
    return HttpResponse(create_reply("Hello World!I am image", message=msg))


# 对视频信息进行回复
def video_handle(msg):
    return HttpResponse(create_reply("Hello World!I am video", message=msg))


# 对地理位置信息进行回复
def location_handle(msg):
    return HttpResponse(create_reply("Hello World!I am location", message=msg))


# 对链接信息进行回复
def link_handle(msg):
    return HttpResponse(create_reply("Hello World!I am link", message=msg))


# 对小视频信息进行回复
def sv_handle(msg):
    return HttpResponse(create_reply("Hello World!I am short video", message=msg))


# 对事件信息进行处理
def event_handle(request):
    msg = parse_message(request.body)
    return event_splitter[msg.event](msg)


# 用户关注事件
def sub_event(msg):
    return HttpResponse(create_reply("1！", message=msg))
    reply = TextReply(message = msg)
    new_uid = reply.target
    if(views.check_band_user(new_uid) == False):
        return HttpResponse(create_reply("2！", message=msg))
        views.insert_band_user(new_uid)
        return HttpResponse(create_reply("太平洋手环保太平，欢迎您使用太平洋手环！", message=msg))
    else:
        return HttpResponse(create_reply("欢迎您重归太平洋手环！", message=msg))


# 对用户取消关注事件
def unsub_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 用户取关事件", message=msg))


# 未关注用户扫描带参数二维码事件
def subscan_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 未关注用户扫描带参数二维码事件", message=msg))


# 已关注用户扫描带参数二维码事件
def scan_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 已关注用户扫描带参数二维码事件", message=msg))


# 上报地理位置事件
def location_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 上报地理位置事件", message=msg))


# 点击菜单拉取消息事件
def click_event(request):
    if request.key == 'ranklist':     #排行榜
        reply = TextReply(message = request)
        t = get_template('ranklist.xml')
        html = t.render(Context({'to_user': reply.target, 'from_user': reply.source, "create_time": reply.time}))
        return HttpResponse(html, content_type="application/xml")
    elif request.key == "talk_with_tree":
        # request.session["talk_flag"] = True
        return HttpResponse(create_reply(u"你好，我是你粗大的生命之树。能和你聊聊天真好。\n\n回复‘退出’可退出交谈模式", message=request))
    elif request.key == "get_today_mission":
        i = random.uniform(0, 2)
        if i < 1:
            i = 1
        else:
            i = 0
        str = "欢迎您领取每日任务。完成每日任务可获得大量肥料与水的奖励。\n\n您今天的任务是【" + mission_detail[i]["description"] + "】"
        return HttpResponse(create_reply(str.decode("utf-8"), message=request))
    elif request.key == "hit_card":
        return HttpResponse(create_reply(u"本日打卡成功！", message=request))

# 点击菜单跳转链接事件
def view_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单跳转链接事件", message=msg))


# 群发消息发送任务完成事件
def masssend_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 群发消息发送任务完成事件", message=msg))


# 模板消息发送任务完成事件
def templatesend_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 模板消息发送任务完成事件", message = msg))


# 扫码推事件
def sc_push_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 扫码推事件", message=msg))


# 扫码推事件且弹出“消息接收中”提示框
def sc_wait_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 扫码推事件且弹出“消息接收中”提示框", message=msg))


# 弹出系统拍照发图事件
def pic_photo_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出系统拍照发图事件", message=msg))


# 弹出拍照或者相册发图事件
def pic_photo_album_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出拍照或者相册发图事件", message=msg))


# 弹出微信相册发图器事件
def pic_wechat_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出微信相册发图器事件", message=msg))


# 弹出地理位置选择器事件
def select_location_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出地理位置选择器事件", message=msg))


def get_rank_list(msg):
    return render_to_response("ranklist.xml", mimetype="application/xml")

msg_splitter = {
    "text": text_handle,
    "voice": voice_handle,
    "image": image_handle,
    "video": video_handle,
    "location": location_handle,
    "link": link_handle,
    "short_video": sv_handle,
    "event": event_handle,
}

event_splitter = {
    "subscribe": sub_event,
    "un_subscribe": unsub_event,
    "subscribe_scan": subscan_event,
    "scan": scan_event,
    "location": location_event,
    "click": click_event,
    "view": view_event,
    "mass_send_job_finish": masssend_event,
    "template_send_job_finish": templatesend_event,
    "scan_code_push": sc_push_event,
    "scan_code_wait_msg": sc_wait_event,
    "pic_sys_photo": pic_photo_event,
    "pic_photo_or_album": pic_photo_album_event,
    "pic_weixin": pic_wechat_event,
    "location_select": select_location_event,
}

key_splitter = {
    "ranklist": get_rank_list,
}
