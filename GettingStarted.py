import skimage
from skimage import data
camera = data.camera()
print(type(camera))
print(camera.shape)
print(camera.size)
print(camera)