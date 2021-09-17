import qrcode


def create_code(data, fcolor=(0, 0, 0), bgcolor=(255, 255, 255), box_size=6):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fcolor, background_color=bgcolor)
    img.save('test.png')


