from API.urlscan.url_grep import urlscan
from switch import Switch


class Main:
    def __init__(self, val):
        self.val = val

    def url_check(url):

        return urlscan(url)

