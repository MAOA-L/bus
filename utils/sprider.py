# -*- coding: utf-8 -*-
"""
 @Time    : 19/8/22 10:31
 @Author  : CyanZoy
 @File    : sprider.py
 @Software: PyCharm
 @Describe: 
 """
import re

import django
import os

from django.db import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bus.settings')
django.setup()
from bus_info.models import BusInfo
import requests
from django.conf import settings
from lxml import etree


def api_post(url, data, cert=None):
    """发送post请求"""
    req = requests.post(url=url, data=data, cert=cert).content.decode("utf-8")
    return req


def api_get(url, file=False, code='utf-8'):
    """发送get请求"""
    if not file:
        req = requests.get(url=url).content.decode(code)
    else:
        req = requests.get(url=url).content
    return req


class Sp:
    def __init__(self):
        self.url_search = settings.BUS_URL_SEARCH

    def get_bus_number(self):
        # 搜索0-9的数字, 获取所有公交车number
        for i in range(0, 10):
            raw_html = api_get(self.url_search.format(i))
            parse_html = etree.HTML(raw_html)
            a_list = parse_html.xpath('//ul[@class="list borderNone mbNone"]/li/a')

            for j in a_list:
                code = re.match(".*num=(.*)", str(j.xpath('./@href')[0]))
                if code:
                    try:
                        BusInfo.objects.create(name=j.text, code=code.group(1))
                    except IntegrityError:
                        pass


bus_sp = Sp()
bus_sp.get_bus_number()
