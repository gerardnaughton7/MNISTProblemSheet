# MNIST problem sheet
# Gerard Naughton G00209309

# Part 1 : Download the image and label files, have Python decompress them and read them byte by byte into appropriate data structures in memory.

# Adapted code discovered on this link
# https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

# import gzip
import gzip

# Read in image file in bytes
f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')# r represents read and b represents bytes

# magic reads in the first 4 bytes
magic = f.read(4)

# Print magic
print(magic)

#Converting binary to decimal
print(int.from_bytes(magic, byteorder='big')) #convert bytes to int and it is read in the big order

f.close()

