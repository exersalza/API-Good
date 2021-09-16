from API.urlscan.url_grep import urlscan


class Main:
    def __init__(self, val):
        self.val = val

    async def url_check(url):

        return urlscan(url)

    async def qr_gen(self, ):

