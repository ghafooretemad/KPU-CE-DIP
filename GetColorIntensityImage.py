from skimage import data, color
from ShowImage import show_image

rocket = data.rocket()

red = rocket[:,:, 0]
green = rocket[:,:, 1]
blue = rocket[:,:, 2]

print("Red Intensity Image:", red)
print("Green Intensity Image:", green)
print("Blue Intensity Image:", blue)

show_image(red, 'Red Intensity Image', 'Reds')
show_image(blue, 'Blue Intensity Image', 'Blues')
show_image(green, 'Green Intensity Image', 'Greens')