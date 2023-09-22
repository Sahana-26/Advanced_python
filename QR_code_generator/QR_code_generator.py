import qrcode as qr

img = qr.make("https://github.com/Sahana-26")
img.save("My_github.png")