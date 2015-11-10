from django.shortcuts import render

# Create your views here.

#coding=utf-8
import hashlib
from xml.etree import ElementTree
import json

from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


