import re
import requests

class Spider():
    panda_url = "https://www.panda.tv/cate/pubg"

    def __fetch_content(self):
        response = requests.get(Spider.panda_url)
        response.encoding = "utf-8"
        htmls = response.text
        return htmls

    def __analysis(self, htmls):
        rough = re.findall(r'<div class="video-info">([\s\S]*?)</div>', htmls)
        anchors = []
        for anchor in rough:
            name = re.findall(r'span class="video-nickname" title="(.*?)"', anchor)
            name = str(name[0])
            number = re.findall(r'<span class="video-number">(.*?)</span>', anchor)
            number = str(number[0])
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        return anchors
    
    def __sort(self, anchors):
        return sorted(anchors, key=self.__sort_seed, reverse=True)

    def __sort_seed(self, anchor):
        if '万' in anchor['number']:
            number = int(float(anchor['number'][:-1]) * 10000)
        else:
            number = int(anchor['number'])
        return number
    
    def __show(self, anchors):
        for rank in range(len(anchors)):
            print("rank %s: %s       %s" % (rank, anchors[rank]['name'], anchors[rank]['number']))



    def go(self):
        htmls = self.__fetch_content()
        rough_list = self.__analysis(htmls)
        sort_list = self.__sort(rough_list)
        return self.__show(sort_list)

a = Spider()
print(a.go())