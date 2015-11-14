# coding=utf-8
from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
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


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def insert_band_user(request):
    if request.method == 'POST':
        bu = BandUser()
        bu.bu_user = request.user
        bu.bu_band = request.POST.get('BU_Band')
        bu.bu_wechat_id = request.POST.get('BU_WechatId')
        bu.bu_gender = request.POST.get('BU_Gender')
        bu.bu_birthday = request.POST.get('BU_Birthday')
        bu.bu_height = request.POST.get('BU_Height')
        bu.bu_weight = request.POST.get('BU_Weight')

        bu.save()
        return HttpResponse('')
    else:
        return HttpResponse('fail')


def insert_step(request):
    if request.method == 'POST':
        st = Step()
        st.st_user = request.user
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
        tc.tc_user = request.user
        tc.tc_content = request.POST.get('TC_Content')

        tc.save()
        return HttpResponse('')
    else:
        return HttpResponse('')


def insert_tag(request):
    if request.method == 'POST':
        tg = Step()
        tg.tg_user = request.user
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
        pl.pl_user = request.user
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
        he.he_user = request.user
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
        sl.sl_user = request.user
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


def delete_step(request, id):
    st = Step.objects.get(st_id=id)
    st.delete()
    return HttpResponse('delete successfully')


def delete_tag_content(request, id):
    tc = TagContent.objects.get(tc_id = id)
    tc.delete()
    return HttpResponse('delete successfully')


def delete_Tag(request, id):
    tg = Tag.objects.get(tg_id = id)
    tg.delete()
    return HttpResponse('delete successfully')


def delete_plan(request, id):
    pl = Plan.objects.get(pl_id = id)
    pl.delete()
    return HttpResponse('delete successfully')


def delete_health(request, id):
    he = Health.objects.get(he_id = id)
    he.delete()
    return HttpResponse('delete successfully')


def delete_sleep(request, id):
    sl = Sleep.objects.get(sl_id = id)
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


def update_tag_content(request, id):
    if request.method == 'POST':
        tc = BandUser.objects.get(tc_id=id)
        if tc:
            tc.content = request.POST.get('TC_Content')
            tc.save()
            return HttpResponse('updated successfully!')
        else:
            return HttpResponse('not found!')
    else:
        return HttpResponse('')


def update_tag(request, id):
    if request.method == 'POST':
        tg = BandUser.objects.get(tg_id=id)
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


def update_plan(request, id):
    if request.method == 'POST':
        pl = BandUser.objects.get(pl_id=id)
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


def update_sleep(request, id):
    if request.method == 'POST':
        sl = BandUser.objects.get(sl_id=id)
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


def select_band_user(request):
    if request.method == 'GET':
        user = request.POST.get('BU_User')
        if user:
            bu = BandUser.objects.get(bu_user=user)
            if bu:
                context = {}
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


def select_step(request):
    if request.method == 'GET':
        ID = request.POST.get('ST_ID')
        if ID:
            st = BandUser.objects.get(st_id=ID)
            if st:
                context = {}
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
        ID = request.POST.get('TC_ID')
        if ID:
            tc = BandUser.objects.get(tc_id=ID)
            if tc:
                context = {}
                context['TC_User'] = tc.tc_user
                context['TC_Content'] = tc.tc_content

                return HttpResponse('')
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')


def select_tag(request):
    if request.method == 'GET':
        ID = request.POST.get('TG_ID')
        if ID:
            tg = BandUser.objects.get(tg_id=ID)
            if tg:
                context = {}
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
        ID = request.POST.get('PL_ID')
        if ID:
            pl = BandUser.objects.get(pl_id=ID)
            if pl:
                context = {}
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
        ID = request.POST.get('HE_ID')
        if ID:
            he = BandUser.objects.get(he_id=ID)
            if he:
                context = {}
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
        ID = request.POST.get('SL_ID')
        if ID:
            sl = BandUser.objects.get(sl_id=ID)
            if sl:
                context = {}
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


