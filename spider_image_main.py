import download_image
import html_downloader
import html_parser
import url_manager


class SpiderImage(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.htmldownloader = html_downloader.HtmlDownload()
        self.parse = html_parser.HtmlParser()
        self.downloader = download_image.DownloadImage()
    def craw_image(self, root_url):
        img_full_lists = set()
        count =1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print("the url %d is %s",count,new_url)
            if count == 1000:
                break
            count += 1
            html_cont = self.htmldownloader.download(new_url)
            img_lists,new_urls = self.parse.parse(new_url,html_cont)
            for img in img_lists:
                img_full_lists.add(img)
            self.urls.add_new_urls(new_urls)
        self.downloader.download(img_full_lists)

if __name__ == "__main__":
    root_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%B0%91%E5%8F%B8%E5%91%BD&pn=0&gsm=8c&ct=&ic=0&lm=-1&width=0&height=0'
    obj_spider_image = SpiderImage()
    obj_spider_image.craw_image(root_url)