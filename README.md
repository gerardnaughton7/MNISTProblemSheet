# MNISTProblemSheet
MNIST Problem Sheet for emerging technology

# Objectives:
1. Read the image files

Download the image and label files, have Python decompress them and read them byte by byte into appropriate data structures in memory.

2. Output an image to the console

Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

3. Output the image files as PNGs

Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.

# How to use this repository?

Firstly download anaconda in order to code in python.
You can download anaconda through this link and following their instructions:
https://www.anaconda.com/download/

To view the code you can use any code editor from as basic textpad to pycharm. I am using Visual studio code.
Here is a link to download Visual Studio Code: https://code.visualstudio.com/download

With anaconda you recieve a terminal called anaconda prompt through this you will be able to run your python code by simply navigating to the directory to your python files and using the command "python" followed by your filename.py.

You will also have to download the images for this program. 
Here is the link to the images and labels: http://yann.lecun.com/exdb/mnist/
After you have downloaded the zipped images place them into a folder called data within your repository.

Finally you will have to create a folder called pngImages in your repository. This will be used for part 3 when you save all the images as png files.

You should now be able to run this code.


ps. in the pngImages folder it only shows a thousand images and not the 60000 the program produces. it had to truncate and omit 59000 images when i did my git push to this repository.



