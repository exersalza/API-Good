# from urlscan.url_grep import urlscan
from .qrcode.qr_creator import create_code


class Main:
    def __init__(self, val):
        self.val = val

    # async def url_check(url):
    #
    #     return urlscan(url)

    def qr_gen(data, c1=(0, 0, 0), c2=(255, 255, 255), bs=6):
        create_code(data, c1, c2, bs)
        return


