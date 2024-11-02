import easyocr 

reader = easyocr.Reader(['en'])

result = reader.readtext('C:/Users/pc/Desktop/Image Recog/images/book1.jpg')

for(bbox , text , prob) in result:
    print(text)