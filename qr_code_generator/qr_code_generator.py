#Takes a text srting/URl and converts it into a QR Code - pip install pyqrcode, pypng
import pyqrcode
import png
url = pyqrcode.create(input("Enter the text to convert: "))
filename=input("Enter the name of the QR code file: ")
url.show()
url.png(filename+".png", scale=6)

