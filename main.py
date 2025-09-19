import qrcode

img = qrcode.make('http://127.0.0.1:5500/mensagem.html')
img.save('qrcode.png')