import requests
import random


class HTTP:
    ua_list = [
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
        "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
    ]

    header = {
        "Referer": "http://www.mmjpg.com/",
        "User-Agent": random.choice(ua_list),
    }

    base_url = "http://www.mmjpg.com/{}"

    @classmethod
    def get(cls, keyword=''):
        url = cls.base_url.format(keyword)
        request = requests.get(url=url, params=None, headers=cls.header)
        request.encoding = 'utf-8'
        return request.text



