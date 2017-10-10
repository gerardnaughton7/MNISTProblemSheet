# MNIST Problem Sheet 
# Gerard Naughton G00209309
# Part 1
# Objective: Read the data files 
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

import gzip # open gzip file

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

# Read Images Function. Opens up file using gzip
def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        # Gets Magic number by reading in the first 4 bytes and converts into an int
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)# Prints to console

        # Gets Number of images by reading in the next 4 bytes and converts into an int
        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("Number of images: ", noimg)# Prints to console

        # Gets Number of columns by reading in the next 4 bytes and converts into an int
        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("Number of column: ", nocol)# Prints to console

        # Gets Number of rows by reading in the next 4 bytes and converts into an int
        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("Number of rows: ", norow)# Prints to console

# Call the functions for each file
print("Training Images")
read_images_from_file("data/train-images-idx3-ubyte.gz")
print("Test Images")
read_images_from_file("data/t10k-images-idx3-ubyte.gz")
print("Training Labels")
read_labels_from_file("data/train-labels-idx1-ubyte.gz")
print("Test Labels")
read_labels_from_file("data/t10k-labels-idx1-ubyte.gz")