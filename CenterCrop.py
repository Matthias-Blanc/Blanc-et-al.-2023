from skimage import io
from tifffile import imsave
import numpy as np
import scipy.ndimage as ndi

## Function set Up

def crop_center(img,cropx,cropy,cropz):
    z,y,x = img.shape
    startx = x//2 - cropx//2
    starty = y//2 - cropy//2
    startz = z//2 - cropz//2    
    return img[startz:startz+cropz, starty:starty+cropy, startx:startx+cropx]

## import stacks 

im1 = io.imread('C1E0.tif')
print(im1.shape)

im2 = io.imread('C1E2.tif')
print(im2.shape)

### center crop to array shape of E0
Cropped = crop_center(im2, 795, 634, 192)
print(Cropped.shape)
imsave('testcrop.tif', Cropped) 
