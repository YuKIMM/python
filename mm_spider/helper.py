import time

import requests

from httper import HTTP
import os
import re

class Spider:

    @staticmethod
    def get_all_tag():
        """
        拿到主页所有标题和url
        """
        all_info = []
        home_html = HTTP.get()
        all_tag = re.findall('<span>所有</span>([\S\s]*?)</div>', home_html)[0]
        all_tag = re.findall('<a href="(.*?)">(.*?)</a>', all_tag)
        for i in all_tag:
            tag = i[1]
            url = i[0]
            anchor = {tag: url}
            all_info.append(anchor)
        return all_info

    @staticmethod
    def mkdir_by_tag(info):
        """
        根据主页分类建立目录
        info：字典 例如：{'xxx':'www.xxxx.com'}性感

        """
        tag_name, = info.keys()
        if not os.path.exists('D:\\img\\{}'.format(tag_name)):
            os.makedirs('D:\\img\\{}'.format(tag_name))
        return tag_name

    @staticmethod
    def tag_html(info, page=1):
        """
        获得单个标签的html 例如性感主页的html
        info：字典 例如：{'xxx':'www.xxx.com'}性感
        """
        url, = info.values()
        url = url[21:] + "/{}".format(page)
        html = HTTP.get(url)
        return html

    @staticmethod
    def tag_page(info):
        """
        拿到总标签各个分类里的总页数（例如：性感的页数）
        html：性感主页解析的html
        """
        url, = info.values()
        html = HTTP.get(url[21:])
        page = int(re.findall('<em class="info">共(\d*?)页</em>', html)[0])
        return page

    @staticmethod
    def get_single_tag_info(html):
        """
        性感标签里面单页的信息
        html：性感一页的信息
        返回{'目录名'：'图集url'}
        """
        anchors = []
        info = re.findall('<li>([\S\s]*?)</li>', html)
        info = list(map(lambda x: re.findall(r'<span class="title"><a href="(.*?)" target="_blank">(.*?)</a></span>', x), info))
        for i in info:
            name = i[0][1]
            url = i[0][0]
            tag_anchor = {name: url}
            anchors.append(tag_anchor)
        return anchors

    @staticmethod
    def mkdir_photo(tag_name, info):
        """
        建立图集的目录
        """
        photo_name, = info.keys()
        if not os.path.exists('D:\\img\\{}\\{}'.format(tag_name, photo_name)):
            os.makedirs('D:\\img\\{}\\{}'.format(tag_name, photo_name))
        return photo_name

    @staticmethod
    def get_photo_html(info, page=1):
        """
        info : 字典包含图集的url 例如 性感下第一个图集
        """
        url, = info.values()
        url = url[21:] + "/{}".format(page)
        html = HTTP.get(url)
        return html


    @staticmethod
    def get_photo_page(info):
        """
        获得写真页码 例如性感下第一个图集的页码
        """
        url, = info.values()
        html = HTTP.get(url[21:])
        page = int(re.findall('<i></i><a href=".*?">(\d*?)</a>', html)[0])
        return page

    @staticmethod
    def get_photo_url(html):
        img_url = re.findall('<img src="(.*?)" data-img=', html)[0]
        return img_url

    @staticmethod
    def download_photo(img_url, tag_dir, photo_dir, photo_name, page):
        img = requests.get(url=img_url, params=None, headers=HTTP.header)
        # if not os.path.exists("D:\\img\\{}\\{}".format(tag_dir, photo_dir)):
        with open("D:\\img\\{}\\{}\\{}{}.jpg".format(tag_dir, photo_dir, photo_name, page), 'wb') as f:
            f.write(img.content)
        time.sleep(0.5)









