import PIL
import numpy as np


class DataHandler(object):

    def __init__(self):
        pass

    def readImage(self,inputFile:str, scale_factor:float):
        """
        Routine zum einlesen einer .png datei. Diese wird als numpy array
        zurückgegeben.

        Args:
            inputFile: str: Pfad und Name des Bildes
            scale_factor: float: Skalierungsfaktor in %. 100=original, 50=halbe Pixelzahl.

        Returns:
            Numpy array mit shape:(3,breite,höhe), sodass mit dem ersten index farbwert abgegriffen wird.

        """
        image_raw = PIL.Image.open(inputFile)
        x_size_raw = image_raw.size[0]
        y_size_raw = image_raw.size[1]
        set_scale_factor = (scale_factor / 100.)

        new_size = (x_size_raw * scale_factor, y_size_raw * scale_factor)
        image = image_raw.thumbnail(new_size, PIL.Image.ANTIALIAS)

        image_array = np.asarray(image, order='F')

        return image_array


