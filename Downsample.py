import tifffile
from skimage.transform import resize

def downsample_tiff(input_file, output_file, scale_factor):
    # Load the 3D tiff file
    tiff = tifffile.imread(input_file)
    
    # Calculate the size of the output image
    output_shape = tuple(int(scale_factor * dim) for dim in tiff.shape)
    
    # Downsample the image using scikit-image's resize function
    downsampled_tiff = resize(tiff, output_shape=output_shape, mode='reflect')
    
    # Save the downsampled image to a new tiff file
    tifffile.imsave(output_file, downsampled_tiff)

# Example usage: downsample the 3D tiff file "input.tiff" and save the result to "output.tiff" with a scale factor of 0.5
downsample_tiff("C1E2MC.tif", "DSC1E2MC.tif", 0.2)
