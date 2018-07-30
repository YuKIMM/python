import re
import requests

class Spider():
    """
    爬取熊猫直播绝地求生板块下主播的人气排行
    """
    panda_url = "https://www.panda.tv/cate/pubg"

    def __fetch_content(self):
        """
        取得网页内容方法
        """

        # 获取网页内容
        response = requests.get(Spider.panda_url)
        
        # 将内容转码为utf-8
        response.encoding = "utf-8"
        
        # 取得内容
        htmls = response.text
        return htmls

    def __analysis(self, htmls):
        """
        分析并取得关键内容方法
        """

        # 用正则表达式粗略取得信息
        rough = re.findall(r'<div class="video-info">([\s\S]*?)</div>', htmls)
        
        # 将取得的内容存放在列表中
        anchors = []
        for anchor in rough:
            
            # 用正则表达式取得主播名
            name = re.findall(r'span class="video-nickname" title="(.*?)"', anchor)
            name = str(name[0])
            
            # 用正则表达式取得观看人数
            number = re.findall(r'<span class="video-number">(.*?)</span>', anchor)
            number = str(number[0])
            
            # 将主播名与观看人数对应起来存到字典中
            anchor = {'name':name, 'number':number}
            
            # 将存有主播名和观看人数的字典存入到anchors列表中
            anchors.append(anchor)
        return anchors
    
    def __sort(self, anchors):
        """
        对数据进行排序的方法
        """

        # 利用sorted函数，函数式编程，reverse进行降序排序
        return sorted(anchors, key=self.__sort_seed, reverse=True)

    def __sort_seed(self, anchor):
        """
        排序方法，__sort的种子方法，可通过此方法指定排序依据
        """
        if '万' in anchor['number']:
            number = int(float(anchor['number'][:-1]) * 10000)
        else:
            number = int(anchor['number'])
        return number
    
    def __show(self, anchors):
        """
        打印数据
        """
        for rank in range(len(anchors)):
            print("rank %s: %s       %s" % (rank, anchors[rank]['name'], anchors[rank]['number']))



    def go(self):
        """
        入口方法，Spider类内部所有方法的调用都通过go方法来调用
        """
        htmls = self.__fetch_content()
        rough_list = self.__analysis(htmls)
        sort_list = self.__sort(rough_list)
        return self.__show(sort_list)

a = Spider()
a.go()