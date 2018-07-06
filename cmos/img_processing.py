import numpy as np

class ImgProcessing(object):


    def __init__(self):
        pass

    def findCenter(self,img_array):
        """
        Find the position (x,y) of the center of an array.

        Args:
            img_array: array of the image

        Returns: tuple: center of the image.
        """
        center_x = int(np.divide(img_array.shape[0], 2))
        center_y = int(np.divide(img_array.shape[1], 2))
        return (center_x,center_y)


    def kartesian2polar(self, img_array):


        # 1. find center:
        center = self.findCenter(img_array)

        # 2. get coords in regards to center:
        # TODO: Wolkenkammera-Docu Abschnitt 4.2, am liebsten ohne Schleife. Die neuen vom Mittelpunktabhängigen Werte sollen x_new und y_new heißen.
        # Idee: mit numpy roll die achsen zurechtrollen.

        img_array_centered = np.roll(img_array,shift=center[0],axis=0)
        img_array_centered = np.roll(img_array_centered,shift=center[1],axis=1)

        # 2. get radius:
        r = np.sqrt()

        # 3. calc Azimuth:
        alpha = np.arctan2(x_new,y_new)

        # 4. calc Elevation:
        epsilon = np.deg2rad(90) * (np.subtract(1,np.divide(r,a))) # TODO: hier noch x und y fall unterscheiden?


    def polar2kartesian(self):
        pass

    def hemisphere2flat(self):
        pass





if __name__ == "__main__":
    pass
