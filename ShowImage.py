from matplotlib import pyplot as plt

def show_image(img, title = 'Image', cmap_type='gray'):
    plt.imshow(img, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()