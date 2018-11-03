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
        dimensiona,_ = self.mser.detectRegions(transfor)
        self.dimensiones = [opencv.convexHull ( p.reshape ( -1, 1, 2 ) ) for p in dimensiona]
        opencv.polylines(self.imagen, self.dimensiones, 1, (0, 255, 0) )
        opencv.imshow ( 'img', self.imagen )
        opencv.waitKey ( 0 )
    def presentacion(self):
        opencv.imshow ( 'img',self.imagen)
        recst = np.zeros ( (self.imagen.shape[0], self.imagen.shape[1], 1), dtype=np.uint8 )
        for contour in self.dimensiones:
            opencv.drawContours ( self.dimensiones, [contour], -1, (255, 255, 255), -1 )
        text_only = opencv.bitwise_and ( self.imagen, self.imagen, mask=recst )
        opencv.imshow ( "text only", text_only )
        opencv.waitKey ( 0 )

intento = Deteccion('C:\images.png')
intento.conversion()
intento.presentacion()
