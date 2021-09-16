import qrcode


def create_code():

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=2,
    )

    data = {
        "header": {
            "format": format
        }
    }

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=(0, 0, 0), back_color=(255, 165, 0))
    img.save('test.png')

create_code()