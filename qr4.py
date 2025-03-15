import qrcode

qr = qrcode.QRCode(version = 1, error_correction= qrcode.constants.ERROR_CORRECT_L,box_size= 10, border = 4)
ab=input('Enter the Link:')

qr.add_data(ab)

qr.make(fit = True)

img = qr.make_image(fill_color = "red",back_color = "white")

img.save("red.png")
