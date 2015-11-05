from django.shortcuts import render

# Create your views here.

#coding=utf-8
import hashlib
from xml.etree import ElementTree
import json

from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

WEIXIN_TOKEN = 'write-a-value'

@csrf_exempt
def wechat_main(request):

    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("wechat_index")
    else:
        print "1"
        xml_str = smart_str(request.body)
        print "2"
        print (xml_str)
        request_xml = ElementTree.fromstring(xml_str)
        print(request_xml)
        response_xml = auto_reply_main(request_xml)
        return HttpResponse(response_xml)


def auto_reply_main(request_xml):
    content = request_xml.find("Content").text
    msg_type = request_xml.find("MsgType").text
    from_user = request_xml.find("FromUserName").text
    return createXML(from_user, 'XP', 123, 'text', 'xpxpx')


def createXML(from_user, to_user, CreateTime, MsgType, Content):
    head = """<xml></xml>"""
    root = ElementTree.fromstring(head)
    elem_fromuser = ElementTree.Element("ToUserName")
    elem_fromuser.text = "![CDATA[" + from_user + "]]"
    elem_touser = ElementTree.Element("FromUserName")
    elem_touser.text = "![CDATA[" + to_user + "]]"
    elem_createtime = ElementTree.Element("CreateTime")
    elem_createtime.text = str(CreateTime)
    elem_msgtype = ElementTree.Element("MsgType")
    elem_msgtype.text = "![CDATA[" + MsgType + "]]"
    elem_content = ElementTree.Element("Content")
    elem_content.text = "![CDATA[" + Content + "]]"

    root.append(elem_fromuser)
    root.append(elem_touser)
    root.append(elem_createtime)
    root.append(elem_msgtype)
    root.append(elem_content)
    text = ElementTree.tostring(root)
    print (text)
    return root