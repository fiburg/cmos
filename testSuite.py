import numpy as np
import matplotlib.pyplot as plt
from cmos.datahandling import DataHandling
from cmos.img_processing import ImgProcessing

if __name__ == "__main__":
    testFile = "./data/Image_20170827_093730_UTCp1.jpg"

    dh = DataHandling()
    ip = ImgProcessing()

    img = dh.readImage(testFile, 100)