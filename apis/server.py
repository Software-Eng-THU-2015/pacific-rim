# -*- coding: UTF-8 -*-
__author__ = 'XP'


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from apis import tools
from wechatpy import parse_message, create_reply

@csrf_exempt

def handle(request):
    menu_file = file("apis/menu.json")
    menu_json = json.load(menu_file)
    tools.menuCreate(menu_json);
    if request.method == "GET":
        if not tools.checkSignature(request):
            return HttpResponse("invalid signature")
        else:
            print "xp"
            return HttpResponse(request.GET["echostr"])
    msg = parse_message(request.body)
    return msg_splitter[msg.type](msg)

def textHandle(msg):
    return HttpResponse(create_reply("Hello World!I am text", message=msg))


def voiceHandle(msg):
    return HttpResponse(create_reply("Hello World!I am voice", message=msg))


def imageHandle(msg):
    return HttpResponse(create_reply("Hello World!I am image", message=msg))


def videoHandle(msg):
    return HttpResponse(create_reply("Hello World!I am video", message=msg))


def locationHandle(msg):
    return HttpResponse(create_reply("Hello World!I am location", message=msg))


def linkHandle(msg):
    return HttpResponse(create_reply("Hello World!I am link", message=msg))


def svHandle(msg):
    return HttpResponse(create_reply("Hello World!I am short video", message=msg))


def eventHandle(msg):
    return event_splitter[msg.event](msg)


def subEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 用户关注事件", message=msg))


def unsubEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 用户取关事件", message=msg))


def subscanEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 未关注用户扫描带参数二维码事件", message=msg))


def scanEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 已关注用户扫描带参数二维码事件", message=msg))


def locationEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 上报地理位置事件", message=msg))


def clickEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单拉取消息事件", message=msg))


def viewEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单跳转链接事件", message=msg))


def masssendEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 群发消息发送任务完成事件", message=msg))


def templatesendEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 模板消息发送任务完成事件", message=msg))


def sc_pushEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 扫码推事件", message=msg))


def sc_waitEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 扫码推事件且弹出“消息接收中”提示框", message=msg))


def pic_photo_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出系统拍照发图事件", message=msg))


def pic_photo_album_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出拍照或者相册发图事件", message=msg))


def pic_wechat_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出微信相册发图器事件", message=msg))


def select_location_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出地理位置选择器事件", message=msg))

msg_splitter = {
  "text": textHandle,
  "voice": voiceHandle,
  "image": imageHandle,
  "video": videoHandle,
  "location": locationHandle,
  "link": linkHandle,
  "shortvideo": svHandle,
  "event": eventHandle,
}

event_splitter = {
  "subscribe": subEvent,
  "unsubscribe": unsubEvent,
  "subscribe_scan": subscanEvent,
  "scan": scanEvent,
  "location": locationEvent,
  "click": clickEvent,
  "view": viewEvent,
  "masssendjobfinish": masssendEvent,
  "templatesendjobfinish": templatesendEvent,
  "scancode_push": sc_pushEvent,
  "scancode_waitmsg": sc_waitEvent,
  "pic_sysphoto": pic_photo_Event,
  "pic_photo_or_album": pic_photo_album_Event,
  "pic_weixin": pic_wechat_Event,
  "location_select": select_location_Event,
}
