'''
        SR1 Points

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Engine 3D

'''

from gl import Bitmap

bmp = Bitmap(600, 600)

def glInit():
    return bmp


if __name__ == '__main__':
    '''Main Program'''

    #Initialize bmp Object
    bmp = glInit()

    #Set bmp width and height
    bmp_width = int(input("\nIngrese ancho de la imagen: "))
    bmp_height = int(input("\nIngrese alto de la imagen: "))

    bmp.glCreateWindow(bmp_height, bmp_width)

    #Set bmp Viewport width and height
    bmp_viewport_x = int(input("\nIngrese coordenada X para el Viewport"))
    bmp_viewport_y = int(input("\nIngrese coordenada Y para el Viewport"))
    bmp_viewport_width = int(input("\nIngrese ancho del ViewPort: "))
    bmp_viewport_height = int(input("\nIngrese alto del ViewPort: "))

    bmp.glViewPort(bmp_viewport_x, bmp_viewport_y, bmp_viewport_height, bmp_viewport_width)

    #Set all pixels to same color
    bmp.glClear()

    bmp.glWrite("test.bmp")