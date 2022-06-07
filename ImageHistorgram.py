from skimage import data, color, exposure
from ShowImage import show_image
from matplotlib import pyplot as plt
import numpy as np
from skimage import io
from skimage.filters import threshold_mean

myImage = io.imread('contrast.jpeg', as_gray = True)
# mean = threshold_mean(myImage)
# binayImage = myImage > mean
# show_image(myImage)
# # plt.hist(myImage.ravel(), bins=256)
# io.imshow(binayImage)
# show_image(255-myImage)

# Contrast stretching
show_image(myImage)
p2, p98 = np.percentile(myImage, (2, 98))
print(p2, "   ", p98)
contrastImage = exposure.rescale_intensity(myImage, in_range=(p2, p98))
# show_image(contrastImage)
l = 11
h = 85
contsImage = 255/(l-h)*(myImage-l)
print(contsImage.min(), "        ", contsImage.max())
show_image(contrastImage)
show_image(contsImage)
plt.show()