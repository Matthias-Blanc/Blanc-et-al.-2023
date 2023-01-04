import numpy as np
import tifffile as tiff
import skimage
import skimage.io
from skimage.morphology import skeletonize_3d

def skeletonize(tiff_image):

    # Determine the threshold value using Otsu's method
    threshold = skimage.filters.threshold_otsu(tiff_image)

    # Segment the image using the threshold
    segmented_image = tiff_image > threshold

    # Generate the 3D skeleton of the image
    skeleton = skeletonize_3d(segmented_image)

    # Save the skeleton as a new .tiff file
    tiff.imwrite("segment.tif", segmented_image)
    tiff.imwrite("skeleton.tif", skeleton.astype(np.uint8))

    return skeleton

# Load the image from the .tiff file
tiff_image = skimage.io.imread('C1E0.tif')

skeletonize(tiff_image)