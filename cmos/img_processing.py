import numpy as np

class ImgProcessing(object):


    def __init__(self):
        pass

    def findCenter(self,img_array):
        center_x = int(np.divide(img_array.shape[0], 2))
        center_y = int(np.divide(img_array.shape[1], 2))
        return (center_x,center_y)


    def kartesian2polar(self, img_array):
        # 1. find center:


    def polar2kartesian(self):
        pass

    def hemisphere2flat(self):
        pass





if __name__ == "__main__":
    pass
