image = "./cat.jfif"

with open(image, 'rb') as image_file:
    content = image_file.read()
    print(len(content))