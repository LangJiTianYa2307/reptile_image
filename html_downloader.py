import urllib.request

class HtmlDownload(object):
    def download(self, new_url):
        if new_url is None:
            return None
        respond = urllib.request.urlopen(new_url)

        # print(respond.getcode())
        if respond.getcode() !=200:
            return None
        return respond.read().decode("UTF-8")