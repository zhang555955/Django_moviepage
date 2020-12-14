#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : testUrllib.py
# @Author: 橘子
# @Date  : 2020/11/30
# @Desc  : execise
import re
import urllib.request
import ssl
from time import sleep

from lxml import etree

from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
def getURL(url,refer):

    headers = {
        "Referer": refer,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    # li_all = soup.find_all('li')
    # for li_all in li_all:
    #     print('--------')
    #     print('匹配到的li:',li_all)
    #     print('li的内容:',li_all.text)
    #     print('li的属性:',li_all.attrs)

    #最灵活的使用方试
    ul = soup.find_all(attrs={'class': 'me1 clearfix'})
    # 重新格式目标串
    li = []
    li.extend(ul[0].find_all('li'))
    for l in li:
        Mname = l.a["title"]
        Mlink = l.a["href"]
        Ming = l.img["src"]

        print({"标题": Mname,
            "链接": Mlink,
            "图片": Ming,
               })


    # num = 0
    # for i in em:
    #     title = i.a['title']
    #     link = i.a['href']
    #     phone = i.a.get_sr
    #
    #
    #     print({'标题': title,
    #             '链接': link,
    #            '图片': phone,
    #     })
    #     sleep(1)
    #     num += 1

if __name__ == "__main__":

    for i in range(1, 3):
        if i == 1:
            url = "https://www.80s.tw/ju/list"
            refer = "https://www.80s.tw"
        else:
            refernum = i - 1
            url = "https://www.80s.tw/ju/list/----0--p/%s" % i
            refer = "https://www.80s.tw/ju/list/----0--p/%s" % refernum
        print("第 %s 页开始爬取" % i)
        getURL(url, refer)
        print("第 %s 页爬取结束" % i)
        sleep(1)
