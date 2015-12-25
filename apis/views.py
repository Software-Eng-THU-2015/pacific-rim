# coding=utf-8
from django.shortcuts import render
from django.core.exceptions import *
# from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
import ujson
import json
from apis.models import *
from datetime import timedelta, time, datetime
from django.views.decorators.csrf import csrf_exempt
import codecs
from django.utils import timezone
from django.forms.models import model_to_dict

# Create your views here.
# from xml.etree import ElementTree
# import json

# from django.utils.encoding import smart_str
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from django.contrib.auth.models import User
# import wechatpy
# import hashlib
import urllib
import os


plan_detail = [
    {
        "lv": 0,
        "steps": 100,
        "description": "hi",
    },
    {
        "lv": 1,
        "steps": 200,
        "description": "no",
    }
]

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def get_plan_list(request):
    if request.method == 'GET':
        res = {'error': 'ok'}
        openid = request.GET.get('openid')
        try:
            user = BandUser.objects.get(bu_openid=openid)
        except ObjectDoesNotExist:
            res['error'] = "invalid user"
            return HttpResponse(ujson.dumps(res),
                    content_type="application/json")
        today = django.utils.timezone.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        res['data'] = []
        try: 
            plans = user.plans.filter(pl_user=user,
                    pl_time_from__gte=today_start, 
                    pl_time_to__lte=today_end)
            for item in plans:
                res['data'].append(model_to_dict(item))
        except ObjectDoesNotExist:
            res['data'] = []

        return HttpResponse(json.dumps(res, default=date_handler),
                content_type="application/json")

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


def get_plan(request):
    if request.method == 'GET':
        openid = request.GET["openid"]
        user = BandUser.objects.get(bu_openid=openid)
        planid = request.GET["planid"]
        if user:
            return JsonResponse(plan_detail[planid])
        else:
            return HttpResponse('user not found!')
    return HttpResponse('')

def update_database(request):
    if request.method == "GET":
        start_year = request.GET["start_year"]  # like 2015
        start_month = request.GET["start_month"]  # like 11
        start_day = request.GET["start_day"]  # like 19
        start_time = request.GET["start_time"]  # like 00:00:00 or 20:00:00
        end_year = request.GET["end_year"]
        end_month = request.GET["end_month"]
        end_day = request.GET["end_day"]
        end_time = request.GET["end_time"]
        openid = request.GET["openid"]
        user = int(openid) % 100  # from 0 to 99
        url = "http://wrist.ssast2015.com/bongdata/?startTime="+ start_year +"-"+ start_month +"-"+ start_day +"%20"+ start_time +"&endTime="+ end_year +"-"+ end_month +"-"+ end_day +"%20"+ end_time +"&user=" + str(user)
        print(url)
        response = urllib.urlopen(url)         #调用urllib2向服务器发送get请求
        js = json.loads(response.read())

        for element in js:
            if element["type"] == str(1):  # for sleeping
                sl = Sleep()
                sl.sl_user = element['user']  # from 0 to 99
                sl.sl_time_from = element['startTime']  # like "2015-11-19 00:00:00"
                sl.sl_time_to = element['endTime']  # like "2015-11-19 00:00:00"
                sl.sl_length = element['lsNum'] + element['wakeNum']  # minutes
                sl.sl_deep_length = element['dsNum']  # minutes
                sl.save()
            elif element["type"] == 2 or element["type"] == 3:  # for bong or not bong
                try:
                    st = Step.objects.get(st_user_id=user)
                except ObjectDoesNotExist:
                    st = Step()
                    st.st_user_id = element['user']  # from 0 to 99
                    st.st_date = element['date']  # like 20151119
                    st.st_step_number = element['steps']
                    st.st_calorie = element['calories']
                    st.st_distance = element['distance']
                    st.save()
                st.st_step_number += element['steps']
                st.st_calorie += element['calories']
                st.save()
            else:  # for other situations
                continue

        return HttpResponse("^-^")                     #获取服务器返回的页面信息

def insert_band_user(request):
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


def get_steps(request, user):
    if request.method == 'GET':
        user = BandUser.objects.get(bu_openid = user)
        start_time = request.GET.get('start_time', timezone.now().date())
        end_time = request.GET.get('end_time', timezone.now().date() + timedelta(1))
        steps = user.steps.filter(st_time__lte=end_time,
                st_time__gte=start_time)
        res = {}
        res['data'] = []
        for step in steps:
            res['data'].append(model_to_dict(step))
        return HttpResponse(json.dumps(res,
            default=date_handler),content_type='application/json')
        


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

@csrf_exempt
def insert_tag(request):
    if request.method == 'POST':
        data = ujson.loads(request.body)
        tg = Tag()
        openid = data.get('openid')
        user = BandUser.objects.get(bu_openid = openid)
        tg.tg_user = user
        tg.tg_time_from = data.get('TG_TimeFrom')
        tg.tg_time_to = data.get('TG_TimeTo')
        content = data.get('TG_Content')
        tg_content = TagContent(tc_user = user, tc_content=content)
        tg_content.save()
        tg.tg_content = tg_content
        tg.save()
        return HttpResponse(ujson.dumps({'res':'ok'}),
                content_type="application/json")

@csrf_exempt
def insert_plan(request):
    if request.method == 'POST':
        data = ujson.loads(request.body)
        pl = Plan()
        openid = data.get('openid')
        user = BandUser.objects.get(bu_openid = openid)
        pl.pl_user = user
        pl.pl_time_from = data.get('PL_TimeFrom')
        pl.pl_time_to = data.get('PL_TimeTo')
        pl.pl_time = data.get('PL_Time')
        pl.pl_goal = data.get('PL_Goal')
        pl.pl_description = data.get('PL_Description')

        pl.save()
        return HttpResponse(ujson.dumps({'res':'ok'}),
                content_type="application/json")


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
        sl = Sleep()
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

@csrf_exempt
def update_plan(request, plan_id):
    if request.method == 'POST':
        print(plan_id)
        data = ujson.loads(request.body)
        try:
            pl = Plan.objects.filter(pl_id = plan_id).update(**data)
            return HttpResponse(json.dumps({'res':'ok'}),
                    content_type='application/json')
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps({'err': 'invalid pid'}),
                    content_type='application/json')

# def update_plan(request, plan_id):
#     if request.method == 'POST':
#         pl = BandUser.objects.get(pl_id=plan_id)
#         if pl:
#             pl.time_from = request.POST.get('PL_TimeFrom')
#             pl.time_to = request.POST.get('PL_TimeTo')
#             pl.time = request.POST.get('PL_Time')
#             pl.goal = request.POST.get('PL_Goal')
#             pl.description = request.POST.get('PL_Description')
#             pl.save()
#             return HttpResponse('updated successfully!')
#         else:
#             return HttpResponse('not found!')
#     else:
#         return HttpResponse('')


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
    if request.method == 'GET':
        open_id = request.GET["openid"]
        user = BandUser.objects.get(openid=open_id)
        if user:
            from_time = request.GET["from_time"]
            to_time = request.GET["to_time"]
            entries = request.user.st_user.filter(st_time__range=(from_time, to_time))
            return JsonResponse({'entries': entries})
        else:
            return HttpResponse('not found!')
    else:
        return HttpResponse('')


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
        response = urllib.urlopen(url)         #调用urllib2向服务器发送get请求
        js = json.loads(response.read())
        openid = js["openid"]
        print (openid)
        return openid                  #获取服务器返回的页面信息


def check_plan(open_id):
    user = BandUser.objects.get(openid=open_id)
    total = 0
    if user:
        today = date.today()
        entries = user.st_user.filter(st_time__year=today.year, st_time__month=today.month, st_time__day=today.day)
        for x in entries:
            total += x.st_step_number
        if total >= plan_detail[user.bu_plan]:
            return True
        else:
            return False
    return False


def update_plan_history(open_id):
    user = BandUser.objects.get(openid=open_id)
    if user.bu_today_done:
        hp = HistoryPlan()
        hp.hp_user = user
        hp.hp_date = date.today()
        hp.hp_plan = user.bu_plan
        hp.save()
    user.bu_today_done = False
    user.save()
    return


def get_plan_history(request):
    if request.method == 'GET':
        open_id = request.GET['openid']
        month = request.GET['month']
        try:
            user = BandUser.objects.get(openid=open_id)
            entries = user.hp_user.filter(hp_date__month=month)
            return JsonResponse({'entries': entries})
        except ObjectDoesNotExist:
            return JsonResponse({'entries': {}})


def tag_main(request):
    if request.method == 'GET':
        openid = get_openid(request)
        # return HttpResponse('xxxx')
        return render(request, 'index.html')
