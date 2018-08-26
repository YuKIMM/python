from helper import Spider
import os


all_tag_info = Spider.get_all_tag()
for tag in all_tag_info:
    tag = {'性感': 'http://www.mmjpg.com/tag/xinggan'}
    tag_dir = Spider.mkdir_by_tag(tag)
    tag_page = Spider.tag_page(tag)
    for page in range(1, tag_page+1):
        cut_form_html = Spider.tag_html(tag, page)
        cut_form_info = Spider.get_single_tag_info(cut_form_html)
        for photo_info in cut_form_info:
            photo_dir, = photo_info.keys()
            if os.path.exists("D:\\img\\{}\\{}".format(tag_dir, photo_dir)):
                break
            Spider.mkdir_photo(tag_dir, photo_info)
            photo_page = Spider.get_photo_page(photo_info)
            for i in range(1, photo_page+1):
                photo_html = Spider.get_photo_html(photo_info, i)
                photo_url = Spider.get_photo_url(photo_html)
                Spider.download_photo(photo_url, tag_dir, photo_dir, photo_dir, i)



































