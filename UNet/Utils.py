import numpy as np
from matplotlib import pyplot as plt
from patchify import patchify
import tifffile as tiff

def Create_Small_Patches(Image_Stack,output_path):

    for img in range(Image_Stack.shape[0]):

        large_image = Image_Stack[img]

        patches_img = patchify(large_image, (256, 256), step=256)  #Step=256 for 256 patches means no overlap

        for i in range(patches_img.shape[0]):
            for j in range(patches_img.shape[1]):

                single_patch_img = patches_img[i,j,:,:]
                tiff.imwrite(output_path + 'image_' + str(img) + '_' + str(i)+str(j)+ ".tif", single_patch_img)