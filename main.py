import qrcode
from PIL import Image
value ="https://in.linkedin.com/in/ashwik-bire-b2a000186"
qr_code=qrcode.QRCode(version=1,box_size=10,border=5)
qr_code.add_data(value)
qr_code.make(fit=True)
qr_image=qr_code.make_image(fill="black",back_color="white")
qr_image.save("qr.png")
