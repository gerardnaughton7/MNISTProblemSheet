# MNIST Problem Sheet 
# Gerard Naughton G00209309
# Part 3
# Objective: Output the image files as PNGs
# Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. 
# For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.

import gzip # open gzip file
import numpy as np # for image arrays 
import PIL.Image as pil # into pil array

# Read Images Function. Opens up file using gzip
def read_images_from_file(filename):
    
    with gzip.open(filename, 'rb') as f:
        # Gets Magic number by reading in the first 4 bytes and converts into an int
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')

        # Gets Number of images by reading in the next 4 bytes and converts into an int
        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')

        # Gets Number of columns by reading in the next 4 bytes and converts into an int
        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        
        # Gets Number of rows by reading in the next 4 bytes and converts into an int
        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')

        # Creat a image array
        images = []

        # Loop through all the images/row/col to get each pixel and its position
        for i in range(noimg):
            row = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                row.append(cols)
            images.append(row)

        # Return images array
        return images

# Read Labels function. Opens up file using gzip
def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f: # r represents read and b represents bytes
        # Gets us our magic number in the first 4 bytes
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')#convert bytes to int and it is read in the big order
        print("Magic is: ", magic)# Prints to console

        # Reads the next 4 byts to get the number of labels
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels: ", nolab)# Prints to console

        labelno = []
        # Loop through all the images/row/col to get each pixel and its position
        for i in range(nolab):
            labelno.append(int.from_bytes(f.read(1), 'big'))

        return labelno            

# Function to save image. takes in 2 paramaters images lis and labels list
def save_images_as_pngs(images, labels):
    i = 0# create i as a counter
    for img in images:# loop through list
        pngImg = img
        pngImg = np.array(pngImg)# using numpy array
        pngImg = pil.fromarray(pngImg)# gives us a monochromatic image. and allows us to get a RGB Image
        pngImg = pngImg.convert('RGB')# convert to RGB
        pngImg.save("pngImages/train-"+str(i)+"-"+str(labels[i])+".png")# Save png image in folder pngImages and with id train-number in list-number in picture
        i = i + 1# Increment the counter


# Get all the images and labels
train_images = read_images_from_file("data/train-images-idx3-ubyte.gz")
train_labels = read_labels_from_file("data/train-labels-idx1-ubyte.gz")

# save images and labels as png
save_images_as_pngs(train_images, train_labels)


