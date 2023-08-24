#load and show an image with pillow

from PIL import Image

#load the image
Img = Image.open('puppies/p1.jpeg')

#get basic details about puppies

print(Img.format)
print(Img.mode)
print(Img.size)

Img.rotate(45).show()


#show image

Img.show()

#save image
#Img.save('puppies/p1_gs.jpeg')