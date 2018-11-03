import cv2 as opencv
import numpy as np

class Deteccion:
    def __init__(self,ruta):
        self.mser = opencv.MSER_create ()
        self.imagen = opencv.imread (ruta)
    def impresion(self):
        print(self.imagen)

intento = Deteccion('C:\images.png')
intento.impresion()
