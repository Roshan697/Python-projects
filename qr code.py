import qrcode as qr

img = qr.make("https://www.youtube.com/watch?v=EvYmTCx9BFs&list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL&index=15")

img.save("youtube_QR.png")