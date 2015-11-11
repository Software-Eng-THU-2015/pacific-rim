from django.shortcuts import render

# Create your views here.

#coding=utf-8
import hashlib
from xml.etree import ElementTree
import json

from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User


def get_distance(request):
    from_time = request.GET["from_time"]
    to_time = request.GET["to_time"]
    entries = request.user.st_user.filter(st_time__range=(from_time, to_time))
    return JsonResponse({'entries': entries})

@csrf_exempt
