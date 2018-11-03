import cv2 as opencv
import numpy as np

class Deteccion:
    def __init__(self,ruta):
        self.mser = opencv.MSER_create()
        self.imagen = opencv.imread(ruta)
    def impresion(self):
        print(self.imagen)
    def conversion(self):
        transfor = opencv.cvtColor (self.imagen, opencv.COLOR_BGR2GRAY)
        print(transfor)
        ejecucion = self.mser.detectRegions(transfor)
        print(ejecucion[0][1])

intento = Deteccion('C:\images.png')
intento.conversion()
