# MNIST Problem Sheet 
# Gerard Naughton G00209309
# Part 2
# Objective: Output the image to the console
# Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol. 

import gzip # open gzip file

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

#function to print out image
# Loops through each row and column and prints either a . if the pixel in that column is less than or equal 127 and a # if it is higher 
def print_out_image(image_array):
    for row in image_array:
        for col in row:
            print("." if col <= 127 else "#", end="")
        print()

# Get all the images
train_images = read_images_from_file("data/train-images-idx3-ubyte.gz")

# Print out the third image to the console
print_out_image(train_images[2])

