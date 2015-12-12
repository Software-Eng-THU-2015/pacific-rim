# coding=utf-8
from django.shortcuts import render
from django.core.exceptions import *
# from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
import json
from apis.models import BandUser, Step, TagContent, Tag, Plan, Health, Sleep

# Create your views here.
# from xml.etree import ElementTree
# import json
                                                         
# from django.utils.encoding import smart_str
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse                     
# from django.contrib.auth.models import User
# import wechatpy
# import hashlib
import urllib2
import os


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

'''
def insert_band_user_test(request):
    if request.method == 'POST':
        bu = BandUser()
        bu.bu_band = request.POST.get('BU_Band')
        bu.bu_openid = request.POST.get('BU_WechatId')
        bu.bu_gender = request.POST.get('BU_Gender')
        bu.bu_birthday = request.POST.get('BU_Birthday')
        bu.bu_height = request.POST.get('BU_Height')
        bu.bu_weight = request.POST.get('BU_Weight')
        bu.save()
        return HttpResponse('success')
    else:
        return HttpResponse('fail')
'''

def insert_band_user_test(request):
    if request.method == 'GET':
        bu = BandUser()
        bu.bu_openid = request.GET.get('BU_WechatId')
        bu.save()
        return HttpResponse('yes')
    else:
        return HttpResponse('fail')


def insert_band_user(BU_WechatId):
    bu = BandUser()
    bu.bu_openid = BU_WechatId
    bu.save()
    return True


def insert_step(request):
    if request.method == 'POST':
        st = Step()
        st.st_user = request.POST.get('openid')
        st.st_time = request.POST.get('ST_Time')
        st.st_step_number = request.POST.get('ST_StepNumber')
        st.st_calorie = request.POST.get('ST_Calorie')

        st.save()
        return HttpResponse('')
    else:
        return HttpResponse('')


def insert_tag_content(request):
    if request.method == 'POST':
        tc = Step()
        tc.tc_user = request.POST.get('openid')
        tc.tc_content = request.POST.get('TC_Content')

        tc.save()
        return HttpResponse('')
    else:
        return HttpResponse('')


def insert_tag(request):
    if request.method == 'POST':
        tg = Step()
        tg.tg_user = request.POST.get('openid')
        tg.tg_time_from = request.POST.get('TG_TimeFrom')
        tg.tg_time_to = request.POST.get('TG_TimeTo')
        tg.tg_content = request.POST.get('TG_Content')
        tg.save()
        return HttpResponse('')
    else:
        return HttpResponse('')


def insert_plan(request):
    if request.method == 'POST':
        pl = Step()
        pl.pl_user = request.POST.get('openid')
        pl.pl_time_from = request.POST.get('PL_TimeFrom')
        pl.pl_time_to = request.POST.get('PL_TimeTo')
        pl.pl_time = request.POST.get('PL_Time')
        pl.pl_goal = request.POST.get('PL_Goal')
        pl.pl_descriptiont.POST.get('PL_Description')

        pl.save()
        return HttpResponse('')
    else:
        return HttpResponse('')


def insert_health(request):
    if request.method == 'POST':
        he = Step()
        he.he_user = request.POST.get('openid')
        he.he_time = request.POST.get('HE_Time')
        he.he_pressure = request.POST.get('HE_Pressure')
        he.he_heart_rate = request.POST.get('HE_HeartRate')

        he.save()
        return HttpResponse('')
    else:
        return HttpResponse('')


def insert_sleep(request):
    if request.method == 'POST':
        sl = Step()
        sl.sl_user = request.POST.get('openid')
        sl.sl_time_from = request.POST.get('TG_TimeFrom')
        sl.sl_time_to = request.POST.get('TG_TimeTo')
        sl.sl_length = request.POST.get('TG_Length')
        sl.sl_deep_length = request.POST.get('TG_DeepLength')

        sl.save()
        return HttpResponse('')
    else:
        return HttpResponse('')


def delete_band_user(request):
    user = request.user
    bu = BandUser.objects.get(bu_user=user)
    bu.delete()
    return HttpResponse('delete successfully')


def delete_step(request, step_id):
    st = Step.objects.get(st_id=step_id)
    st.delete()
    return HttpResponse('delete successfully')


def delete_tag_content(request, tagc_id):
    tc = TagContent.objects.get(tc_id=tagc_id)
    tc.delete()
    return HttpResponse('delete successfully')


def delete_tag(request, tag_id):
    tg = Tag.objects.get(tg_id=tag_id)
    tg.delete()
    return HttpResponse('delete successfully')


def delete_plan(request, plan_id):
    pl = Plan.objects.get(pl_id=plan_id)
    pl.delete()
    return HttpResponse('delete successfully')


def delete_health(request, health_id):
    he = Health.objects.get(he_id=health_id)
    he.delete()
    return HttpResponse('delete successfully')


def delete_sleep(request, sleep_id):
    sl = Sleep.objects.get(sl_id=sleep_id)
    sl.delete()
    return HttpResponse('delete successfully')


def update_band_user(request):
    if request.method == 'POST':
        user = request.user
        bu = BandUser.objects.get(bu_user=user)
        if bu:
            bu.band = request.POST.get('BU_Band')
            bu.gender = request.POST.get('BU_Gender')
            bu.birthday = request.POST.get('BU_Birthday')
            bu.height = request.POST.get('BU_Height')
            bu.weight = request.POST.get('BU_Weight')
            bu.save()
            return HttpResponse('updated successfully!')
        else:
            return HttpResponse('not found!')
    else:
        return HttpResponse('')


def update_tag_content(request, tagc_id):
    if request.method == 'POST':
        tc = BandUser.objects.get(tc_id=tagc_id)
        if tc:
            tc.content = request.POST.get('TC_Content')
            tc.save()
            return HttpResponse('updated successfully!')
        else:
            return HttpResponse('not found!')
    else:
        return HttpResponse('')


def update_tag(request, tag_id):
    if request.method == 'POST':
        tg = BandUser.objects.get(tg_id=tag_id)
        if tg:
            tg.time_from = request.POST.get('TG_TimeFrom')
            tg.time_to = request.POST.get('TG_TimeTo')
            tg.content = request.POST.get('TG_Content')
            tg.save()
            return HttpResponse('updated successfully!')
        else:
            return HttpResponse('not found!')
    else:
        return HttpResponse('')


def update_plan(request, plan_id):
    if request.method == 'POST':
        pl = BandUser.objects.get(pl_id=plan_id)
        if pl:
            pl.time_from = request.POST.get('PL_TimeFrom')
            pl.time_to = request.POST.get('PL_TimeTo')
            pl.time = request.POST.get('PL_Time')
            pl.goal = request.POST.get('PL_Goal')
            pl.description = request.POST.get('PL_Description')
            pl.save()
            return HttpResponse('updated successfully!')
        else:
            return HttpResponse('not found!')
    else:
        return HttpResponse('')


def update_sleep(request, sleep_id):
    if request.method == 'POST':
        sl = BandUser.objects.get(sl_id=sleep_id)
        if sl:
            sl.time_from = request.POST.get('SL_TimeFrom')
            sl.time_to = request.POST.get('SL_TimeTo')
            sl.length = request.POST.get('SL_Length')
            sl.deep_length = request.POST.get('SL_DeepLength')
            sl.save()
            return HttpResponse('updated successfully!')
        else:
            return HttpResponse('not found!')
    else:
        return HttpResponse('')

'''
def select_band_user(request):
    if request.method == 'GET':
        user = request.POST.get('BU_User')
        if user:
            bu = BandUser.objects.get(bu_user=user)
            if bu:
                context = list({})
                context['BU_User'] = bu.bu_user
                context['BU_Band'] = bu.bu_band
                context['BU_WechatId'] = bu.bu_wechat_id
                context['BU_Gender'] = bu.bu_gender
                context['BU_Birthday'] = bu.bu_birthday
                context['BU_Height'] = bu.bu_height
                context['BU_Weight'] = bu.bu_weight
                context['BU_Follow'] = [fo for fo in bu.bu_follow]
                return HttpResponse('')
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')
'''

def check_band_user(uid):    # 检查是否存在
    try:
        bu = BandUser.objects.get(bu_openid = uid)
    except ObjectDoesNotExist:
        return False
    return True

def select_step(request):
    if request.method == 'GET':
        step_id = request.POST.get('ST_ID')
        if step_id:
            st = BandUser.objects.get(st_id=step_id)
            if st:
                context = list({})
                context['ST_User'] = st.st_user
                context['ST_Time'] = st.st_time
                context['ST_StepNumber'] = st.st_step_number
                context['ST_Calorie'] = st.st_calorie

                return HttpResponse('')
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')


def select_step_range(request):
    from_time = request.GET["from_time"]
    to_time = request.GET["to_time"]
    entries = request.user.st_user.filter(st_time__range=(from_time, to_time))
    return JsonResponse({'entries': entries})


def select_tag_content(request):
    if request.method == 'GET':
        tagc_id = request.POST.get('TC_ID')
        if id:
            tc = BandUser.objects.get(tc_id=tagc_id)
            if tc:
                context = list({})
                context['TC_User'] = tc.tc_user
                context['TC_Content'] = tc.tc_content

                return HttpResponse('')
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')


def select_tag(request):
    if request.method == 'GET':
        tag_id = request.POST.get('TG_ID')
        if tag_id:
            tg = BandUser.objects.get(tg_id=tag_id)
            if tg:
                context = list({})
                context['TG_User'] = tg.tg_user
                context['TG_TimeFrom'] = tg.tg_time_from
                context['TG_TimeTo'] = tg.tg_time_to
                context['TG_Content'] = tg.tg_content

                return HttpResponse('')
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')


def select_plan(request):
    if request.method == 'GET':
        plan_id = request.POST.get('PL_ID')
        if plan_id:
            pl = BandUser.objects.get(pl_id=plan_id)
            if pl:
                context = list({})
                context['PL_User'] = pl.pl_user
                context['PL_TimeFrom'] = pl.pl_time_from
                context['PL_TimeTo'] = pl.pl_time_to
                context['PL_Time'] = pl.pl_time
                context['PL_Goal'] = pl.pl_goal
                context['PL_Description'] = pl.pl_description

                return HttpResponse('')
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')


def select_health(request):
    if request.method == 'GET':
        health_id = request.POST.get('HE_ID')
        if health_id:
            he = BandUser.objects.get(he_id=health_id)
            if he:
                context = list({})
                context['HE_User'] = he.he_user
                context['HE_Time'] = he.he_time
                context['HE_Pressure'] = he.he_pressure
                context['HE_HeartRate'] = he.he_heart_rate

                return HttpResponse('')
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')


def select_sleep(request):
    if request.method == 'GET':
        sleep_id = request.POST.get('SL_ID')
        if sleep_id:
            sl = BandUser.objects.get(sl_id=sleep_id)
            if sl:
                context = list({})
                context['SL_User'] = sl.sl_user
                context['SL_TimeFrom'] = sl.sl_time_from
                context['SL_TimeTo'] = sl.sl_time_to
                context['SL_Length'] = sl.sl_length
                context['SL_DeepLength'] = sl.sl_deep_length

                return HttpResponse('')
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')


def get_openid(request):
    if request.method == "GET":
        code = request.GET["code"]
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=" + os.environ.get('APP_ID')+ "&secret=" + os.environ.get('APP_SECRET') + "&code=" + code + "&grant_type=authorization_code"
        # url = "xp"
        response = urllib2.urlopen(url)         #调用urllib2向服务器发送get请求
        js = json.loads(response.read())
        openid = js["openid"]
        print openid
        return openid                  #获取服务器返回的页面信息


def tag_main(request):
    if request.method == 'GET':
        openid = get_openid(request)
        # return HttpResponse('xxxx')
        return render(request, 'index.html')
