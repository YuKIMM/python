import re
import requests

class Spider():
    """
    ????tv?????????????
    """

    # ??????url????
    pubg_url = "https://www.panda.tv/cate/pubg"

    def __response(self):
        """
        ??????
        """

        # ??requests???????
        response = requests.get(Spider.pubg_url)

        # ??????????
        response.encoding = "utf-8"
        
        # ????
        htmls = response.text
        return htmls

    def __analysis(self, htmls):
        """
        ?????html??????????
        """

        # ????????????????
        rough = re.findall(r'<div class="video-info">([\s\S]*?)</div>', htmls)
        
        # anchors??????????
        anchors = []
        for anchor in rough:

            # ????????????????
            name = re.findall(r'<span class="video-nickname" title="([\s\S]*?)">', anchor)
            name = str(name[0])

            # ????????????????
            number = re.findall(r'<span class="video-number">([\s\S]*?)</span>', anchor)
            number = str(number[0])
            
            # ????????????????????
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        return anchors

    def __sort(self, anchors):
        """
        ?????????????
        """
        return sorted(anchors, key=self.__sort_seed, reverse=True)

    def __sort_seed(self, anchor):
        """
        sorted??????????????????
        """
        if '?' in anchor['number']:
            number = int(float(anchor['number'][:-1]) * 10000)
        else:
            number = int(anchor['number'])
        return number

    def __show(self, anchors):
        """
        ??????
        """
        for i in anchors:
            print('name: ', i['name'],'\n','number:', i['number'],'\n')



    def go(self):
        """
        Spider???????Spider????????????go?????
        """
        htmls = self.__response()
        rough_list = self.__analysis(htmls)
        sort_list = self.__sort(rough_list)
        return self.__show(sort_list)


a = Spider()
a.go()