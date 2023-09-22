import qrcode

qr_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=3 )

qr_code.add_data("https://www.linkedin.com/in/sahana26/")
qr_code.make(fit=True)

img1 = qrcode.make("https://github.com/Sahana-26")
img1.save("My_github.png")
img2 = qr_code.make_image(fill_color="red", back_color="blue")
img2.save("My_linkedIn.png")
