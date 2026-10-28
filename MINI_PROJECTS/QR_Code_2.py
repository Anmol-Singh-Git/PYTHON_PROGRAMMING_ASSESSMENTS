import qrcode
url=input("Enter url to make a QR code")
if url.startswith("http") or url.startswith("https"):
    qr=qrcode.make(url)           
    qr.save("secondqrcode.png")
    print("generate a qrcode")
else:
    print("invalid qrcode")
