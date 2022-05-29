from skimage import data, color
from ShowImage import show_image
import numpy as np
from skimage import io
myImage = io.imread('../../../Desktop/index.jpeg', as_gray = False)
print(io.imshow(myImage))
image = data.astronaut()
rotatedImge = np.flipud(image)
print(f'Shape of the Image: {image.shape}')
print(f'Number PX of the Image: {image.size}')
show_image(rotatedImge)
# redImage = image[:,:, 0]
# show_image(redImage, "Red Image", 'Reds')

# greenImage = image[:,:, 1]
# show_image(greenImage, "Green Image", 'Greens')

# blueImage = image[:,:, 2]
# show_image(blueImage, "Blue Image", 'Blues')
# print(image)
# show_image(image, "Astronaut", 'gray')