from Tkinter import Tk
import os
from tkFileDialog import askopenfilename
import Image


def main():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if(os.path.exists(filename) == False):
        print("The image no longer exists...Please enter a new file")
        return
    try:
        im = Image.open(filename)
    except IOError:
        print ("The file is either not an image file or the file is currupted!")



if __name__ == '__main__':
    main()
