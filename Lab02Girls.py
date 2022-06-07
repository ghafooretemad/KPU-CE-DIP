from skimage import data, color, exposure
from ShowImage import show_image
from matplotlib import pyplot as plt
import numpy as np
from skimage import io
from skimage.filters import threshold_mean

image = io.imread('testImage.jpg', as_gray=True)
mean = threshold_mean(image)
print("Mean Intensity Value", mean)
binaryImage = image > mean
show_image(binaryImage)
# plt.hist(image.ravel(), bins=256)
# plt.show()
# show_image(image)