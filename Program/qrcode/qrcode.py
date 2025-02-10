import qrcode
x = qrcode.make("https://www.w3schools.com/python/trypython.asp?filename=demo_default")
a=1
for a in range (1,10):
    x.save(f'{a}.png')
    