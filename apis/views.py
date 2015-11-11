from django.shortcuts import render

# Create your views here.
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
        xml_str = smart_str(request.body)                
        print (xml_str)                                  
        request_xml = ElementTree.fromstring(xml_str)    
        print(request_xml)                               
        response_xml = auto_reply_main(request_xml)      
        return HttpResponse(response_xml)

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
