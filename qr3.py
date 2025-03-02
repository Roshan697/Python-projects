import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction= qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")

qr.make(fit=True)

img = qr.make_image(fill_color = "blue", back_color = "white")
img.save("qr3.png")
