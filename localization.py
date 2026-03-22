from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

carImage = imread("./test_images/car.jpg", as_gray = True)
print(carImage.shape)

grayCarImage = carImage * 255
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(grayCarImage, cmap="gray")

thresholdValue = threshold_otsu(grayCarImage)
binaryCarImage = grayCarImage > thresholdValue

ax2.imshow(binaryCarImage, cmap="gray")

plt.show()