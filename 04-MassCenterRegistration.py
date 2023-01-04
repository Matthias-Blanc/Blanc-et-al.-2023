from skimage import io
from tifffile import imsave
import numpy as np
import scipy.ndimage as ndi

## Function set Up

def image_transform(im, TM, origin=None, output_shape=None, order=1):
    """Transform an m-dimensional image `im` by the  
    homogeneous transformation matrix `TM`.
    
    im : m-dimensional numpy image array
    TM : numpy array of shape ((m+1), (m+1))
    
    origin : numpy array of shape (m,), default None
             coordinates (in image space) of the origin 
             of the coordinate system within which TM 
             is defined. Use None if the TM is defined 
             in the same coordinate system as the image.
    output_shape : tuple of ints, default None
             Shape of the output image. If None, it has
             the same shape as the input.
    
    -> imT : transformed image, 
             m-dimensional numpy image array
    """

    # Get the linear transformation matrix
    ##A_L = TM[:-1,:-1]
    A_L = TM
    c = 0.0
    
    # Get offset to handle coordinate system translation
    if origin is not None:
        x_0 = origin
        c_L = TM[:-1,-1]
        c   = - np.dot(A_L, x_0) + x_0 + c_L        

    # Transform the image
    imT = ndi.affine_transform(im, A_L, offset=c, 
                               output_shape=output_shape,
                               order=order)
    
    return imT

## import stacks 

im1 = io.imread('C1E0.tif')
print(im1.shape)


im2 = io.imread('C1E2.tif')
print(im2.shape)
print(ndi.center_of_mass(im2))

## Compute Center of Mass

a = ndi.center_of_mass(im1)
print(a)
b = ndi.center_of_mass(im2)
print(b)

## Compute translation from center of mass

dX = b[0] - a[0]
dY = b[1] - a[1]
dZ = b[2] - a[2]

print(dX,dY,dZ)

TM = np.array([[1, 0, 0, dX],
               [0, 1, 0, dY],
               [0, 0, 1, dZ],
               [0, 0, 0, 1]])

print(TM)

## apply shift 
imC = image_transform(im2, TM, output_shape=im1.shape)

# save 32bit float (== single) tiff
imsave('test.tif', imC) 