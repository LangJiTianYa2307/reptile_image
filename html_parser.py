from  bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    def __init__(self):
        self.img_pages = []
        self.img_pages.append('pn=0')
    def parse(self,page_url,html_cont):
        img_lists = set()
        new_urls = set()
        if page_url is None or html_cont is None:
            return
        imgs = re.findall(re.compile(r'http://[\S]*\.jpg'),html_cont)    #爬取网页中的图片
        for img in imgs:
            img_lists.add(img)
        soup = BeautifulSoup(
            html_cont,
            'html.parser'
        )

        links = soup.find_all('a',href = re.compile(r'/search/flip?[\S]'))
        # links = soup.find_all('a')
        # for link in links:
        #     print(link)

        for link in links:
            # print("the link is ",link)
            page =""             #用于保存页码字符串
            new_url = link['href']    #获取了Tag=href的信息
            # print(new_url)
            page = re.search(re.compile(r'pn=[\d]*'),new_url)
            # print(page.group())
            # if page not in self.img_pages:
            #     print(True)
            if page.group() is not None and page.group() not in self.img_pages:
                self.img_pages.append(page.group())
                new_full_url = urllib.parse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
            #     for img_page in self.img_pages:
            #         print('the img_page is ',img_page)
            # print('------')
        return img_lists,new_urls