import qrcode


def create_code(data, fcolor, bgcolor, box_size):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fcolor, background_color=bgcolor)
    img.save('cogs/etc/test.png')


