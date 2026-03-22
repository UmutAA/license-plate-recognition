from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

# this gets all the connected regions and groups them together
labelImage = measure.label(localization.binaryCarImage)
fig, (ax1) = plt.subplots(1)
ax1.imshow(localization.grayCarImage, cmap="gray");

minHeight, maxHeight, minWidth, maxWidth = (0.08 * labelImage.shape[0], 0.2 * labelImage.shape[0], 0.15 * labelImage.shape[1], 0.4 * labelImage.shape[1])
plateObjectsCordinates = []
plateLikeObjects = []


# regionprops creates a list of properties of all the labelled regions
for region in regionprops(labelImage):
    if region.area < 50:
        #if the region is so small then it's likely not a license plate
        continue

    # the bounding box coordinates
    minRow, minCol, maxRow, maxCol = region.bbox
    regionHeight = maxRow - minRow
    regionWidth = maxCol - minCol
    if regionHeight >= minHeight and regionHeight <= maxHeight and regionWidth >= minWidth and regionWidth <= maxWidth and regionWidth >= regionHeight:
        plateLikeObjects.append(localization.binaryCarImage[minRow: maxRow, minCol: maxCol])
        plateObjectsCordinates.append((minRow, maxRow, minCol, maxCol))


        # draw a red rectangle over those regions
        rectBorder = patches.Rectangle((minCol, minRow), maxCol-minCol, maxRow-minRow, edgecolor="red", linewidth=2, fill=False)
        ax1.add_patch(rectBorder)
   

plt.show()