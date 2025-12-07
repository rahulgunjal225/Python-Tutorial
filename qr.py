import qrcode

data = rahul

qr = qrcode.make(data)

qr.save('qrcode.png')

print('qr code generated successfully')
