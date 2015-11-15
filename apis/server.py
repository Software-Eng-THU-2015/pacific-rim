# -*- coding: UTF-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from apis.tools import *

from apis import tools
from wechatpy import parse_message, create_reply
# from wechatpy.replies import TextReply, ImageReply, VoiceReply, VideoReply, MusicReply, TransferCustomerServiceReply
from wechatpy.replies import ArticlesReply


@csrf_exempt
def handle(request):
    if request.method == "GET":
        if not tools.check_signature(request):
            return HttpResponse("invalid signature")
        else:
            return HttpResponse(request.GET["echostr"])
    menu_file = file("apis/menu.json")
    menu_json = json.load(menu_file)
    print(menu_json)
    tools.menu_create(menu_json)
    msg = parse_message(request.body)
    return msg_splitter[msg.type](msg)


# 对文本信息进行回复
def text_handle(msg):
    return HttpResponse(create_reply("Hello World!I am text", message=msg))


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
def event_handle(msg):
    return event_splitter[msg.event](msg)


# 用户关注事件
def sub_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 用户关注事件", message=msg))


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
def click_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单拉取消息事件", message=msg))


# 点击菜单跳转链接事件
def view_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单跳转链接事件", message=msg))


# 群发消息发送任务完成事件
def masssend_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 群发消息发送任务完成事件", message=msg))


# 模板消息发送任务完成事件
def templatesend_event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 模板消息发送任务完成事件", message=msg))


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


msg_splitter = {
    "text": text_handle,
    "voice": voice_handle,
    "image": image_handle,
    "video": video_handle,
    "location": location_handle,
    "link": link_handle,
    "shortvideo": sv_handle,
    "event": event_handle,
}

event_splitter = {
    "subscribe": sub_event,
    "unsubscribe": unsub_event,
    "subscribe_scan": subscan_event,
    "scan": scan_event,
    "location": location_event,
    "click": click_event,
    "view": view_event,
    "masssendjobfinish": masssend_event,
    "templatesendjobfinish": templatesend_event,
    "scancode_push": sc_push_event,
    "scancode_waitmsg": sc_wait_event,
    "pic_sysphoto": pic_photo_event,
    "pic_photo_or_album": pic_photo_album_event,
    "pic_weixin": pic_wechat_event,
    "location_select": select_location_event,
}
