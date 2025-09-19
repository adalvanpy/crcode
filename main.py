import qrcode

img = qrcode.make('https://adalvanpy.github.io/crcode/mensagem.html')
img.save('qrcode.png')