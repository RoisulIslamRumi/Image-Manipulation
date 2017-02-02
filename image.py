from PIL import Image 

# open colour image
image_file = Image.open("image.jpg")

# convert image to black and white
black_and_white = image_file.convert('1')

#   another way you can rewrite this line
#   image_file = Image.open("image.jpg").convert("L")
black_and_white.save('black_and_white.jpg')

#   resize the image
size = (50, 150)    # width, height
new_image = image_file.resize(size, 1)
new_image.save('resize2.jpg')


#   rotate the image
rotate_image = image_file.rotate(90)
rotate_image.save('rotate_image.jpg')

