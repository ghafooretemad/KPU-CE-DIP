from skimage import data, color
from ShowImage import show_image
from matplotlib import pyplot as plt
import numpy as np
from skimage import io
myImage = io.imread('testImage.jpg', as_gray = True)
plt.hist(myImage.ravel(), bins=256)
show_image(myImage)