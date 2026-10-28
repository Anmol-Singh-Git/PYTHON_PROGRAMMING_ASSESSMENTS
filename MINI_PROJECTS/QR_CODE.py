import qrcode
data=input("Enter data to make a QR code")
qr=qrcode.make(data)           
qr.save("firstqrcode.png")
print("generate a qrcode")
