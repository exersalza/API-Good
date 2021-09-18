import qrcode


def create_code(data, fcolor=(0, 0, 0), bgcolor=(255, 255, 255), box_size=6):

    print(fcolor, bgcolor, box_size)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=2,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save('test.png')


# create_code('data is not valid you bastard', (0, 0, 0), (0, 255, 255), 6)


