# -*- coding: UTF-8 -*-
__author__ = 'XP'


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from apis import tools
from wechatpy import parse_message, create_reply
from wechatpy.replies import TextReply, ImageReply, VoiceReply, VideoReply, MusicReply, ArticlesReply, TransferCustomerServiceReply

@csrf_exempt
def handle(request):
    if request.method == "GET":
        if not tools.checkSignature(request):
            return HttpResponse("invalid signature")
        else:
            return HttpResponse(request.GET["echostr"])
    msg = parse_message(request.body)
    return msg_splitter[msg.type](msg)

#对文本信息进行回复
def textHandle(msg):
    tools.customSendText(msg.source, u"我是主动发送的信息") #主动回复文本
    if tools.tmp_media_id:
        tools.customSendImage(msg.source, None, tools.tmp_media_id)
    else:
        tools.tmp_media_id = tools.uploadMedia("image", "test.jpg")["media_id"]
        tools.customSendImage(msg.source, None, tools.tmp_media_id)  #主动回复图片
    #tools.customSendImage(msg.source, "test.jpg")  #主动回复图片也可直接这样用，但不推荐，会造成重复素材的大量累积
    #回复图文信息
    tools.customSendArticle(msg.source, u"我是单条的文章", u"圣光会制裁你的!", "http://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=http%3A%2F%2Fimg1.91.com%2Fuploads%2Fallimg%2F141208%2F723-14120P95G23Q.jpg", "http://www.hearthstone.com.cn/landing")
    #回复多条图文信息
    articles = []
    articles.append({"title":u"我是多条文章_0", "description":u"过来好好打一架，胆小鬼!", "image":"http://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=http%3A%2F%2Fdynamic-image.yesky.com%2F300x-%2FuploadImages%2F2014%2F014%2F9N1OO1139Y57_big_500.png", "url":"http://www.hearthstone.com.cn/landing"})
    articles.append({"title":u"我是多条文章_1", "description":u"信仰圣光吧！", "image":"http://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=http%3A%2F%2Fdb.hs.tuwan.com%2Fcard%2Fpremium%2FEX1_383.png", "url":"http://www.hearthstone.com.cn/landing"})
    articles.append({"title":u"我是多条文章_2", "description":u"你～需要我的帮助么", "image":"http://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=http%3A%2F%2Fimg.douxie.com%2Fupload%2Fupload%2F2014%2F02%2F12%2Ftb_52fadff8ed62f.jpg", "url":"http://www.hearthstone.com.cn/landing"})
    tools.customSendArticles(msg.source, articles)
    #生成文本回复
#    reply = TextReply(content="Hello World!I am text\nyour openid is :%s" % msg.source, message=msg)
    #生成图片回复
#    reply = ImageReply(image=tools.tmp_media_id, message=msg)
    #生成语音回复
#    reply = VoiceReply(voice=your media id, message=msg)
    #生成视频回复
#    reply - VideoReply(video={"media_id":*,"title":*,"description":*}, message=msg)
    #生成音乐回复
#    reply = MusicReply(music={"thumb_media_id":*,"title":*,"description":*,"music_url":*,"hq_music_url":*}, message=msg)
    #生成图文回复
    reply = ArticlesReply(articles=articles, message=msg)
    return HttpResponse(reply)

#对语音信息进行回复
def voiceHandle(msg):
    return HttpResponse(create_reply("Hello World!I am voice", message=msg))

#对图片信息进行回复
def imageHandle(msg):
    return HttpResponse(create_reply("Hello World!I am image", message=msg))

#对视频信息进行回复
def videoHandle(msg):
    return HttpResponse(create_reply("Hello World!I am video", message=msg))

#对地理位置信息进行回复
def locationHandle(msg):
    return HttpResponse(create_reply("Hello World!I am location", message=msg))

#对链接信息进行回复
def linkHandle(msg):
    return HttpResponse(create_reply("Hello World!I am link", message=msg))

#对小视频信息进行回复
def svHandle(msg):
    return HttpResponse(create_reply("Hello World!I am short video", message=msg))

#对事件信息进行处理
def eventHandle(msg):
    return event_splitter[msg.event](msg)

#用户关注事件
def subEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 用户关注事件", message=msg))

#对用户取消关注事件
def unsubEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 用户取关事件", message=msg))

#未关注用户扫描带参数二维码事件
def subscanEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 未关注用户扫描带参数二维码事件", message=msg))

#已关注用户扫描带参数二维码事件
def scanEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 已关注用户扫描带参数二维码事件", message=msg))

#上报地理位置事件
def locationEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 上报地理位置事件", message=msg))

#点击菜单拉取消息事件
def clickEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单拉取消息事件", message=msg))

#点击菜单跳转链接事件
def viewEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 点击菜单跳转链接事件", message=msg))

#群发消息发送任务完成事件
def masssendEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 群发消息发送任务完成事件", message=msg))

#模板消息发送任务完成事件
def templatesendEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 模板消息发送任务完成事件", message=msg))

#扫码推事件
def sc_pushEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 扫码推事件", message=msg))

#扫码推事件且弹出“消息接收中”提示框
def sc_waitEvent(msg):
    return HttpResponse(create_reply(u"Hello World!I am 扫码推事件且弹出“消息接收中”提示框", message=msg))

#弹出系统拍照发图事件
def pic_photo_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出系统拍照发图事件", message=msg))

#弹出拍照或者相册发图事件
def pic_photo_album_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出拍照或者相册发图事件", message=msg))

#弹出微信相册发图器事件
def pic_wechat_Event(msg):
    return HttpResponse(create_reply(u"Hello World!I am 弹出微信相册发图器事件", message=msg))

#弹出地理位置选择器事件
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