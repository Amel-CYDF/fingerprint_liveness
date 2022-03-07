from PIL import Image, ImageDraw
import numpy as np

img = Image.open('001.jpeg')

imgarr = np.array(img)
print(imgarr)

x = 600; y = 600; siz = 30
draw = ImageDraw.Draw(img)
draw.ellipse((x,y,x+siz,y+siz), outline='red', width=3)

img.show()

img.save('001_result.png')