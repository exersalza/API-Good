import qrcode
from datetime import datetime


def create_code(data, fname, fcolor=(0, 0, 0), bgcolor=(255, 255, 255), box_size=6):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fcolor, back_color=bgcolor)
    img.save(fname)


# create_code('testing some data for exchange', 'test.png', (0, 0, 0), (255, 255, 255), 6)


