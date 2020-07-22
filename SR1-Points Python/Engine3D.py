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

    #Input bmp width and height
    while True:
        bmp_width = input("\nIngrese ancho de la imagen: ")
        bmp_height = input("\nIngrese alto de la imagen: ")
        try:
            bmp_width = int(bmp_width)
            bmp_height = int(bmp_height)
            break
        except ValueError:
            print("\n\nERROR: Por favor ingrese un numero entero.\n")

    #Set bmp width and height
    bmp.glCreateWindow(bmp_height, bmp_width)

    #Input bmp Viewport width and height
    while True:
        bmp_viewport_x = input("\nIngrese coordenada X para el Viewport: ")
        bmp_viewport_y = input("\nIngrese coordenada Y para el Viewport: ")
        bmp_viewport_width = input("\nIngrese ancho del ViewPort: ")
        bmp_viewport_height = input("\nIngrese alto del ViewPort: ")
        try:
            bmp_viewport_x = int(bmp_viewport_x)
            bmp_viewport_y = int(bmp_viewport_y)
            bmp_viewport_width = int(bmp_viewport_width)
            bmp_viewport_height = int(bmp_viewport_height)
            break
        except ValueError:
            print("\n\nERROR: Por favor ingrese un numero entero.\n")

    #Set bmp Viewport width and height
    bmp.glViewPort(bmp_viewport_x, bmp_viewport_y, bmp_viewport_height, bmp_viewport_width)

    #Set all pixels to same color
    bmp.glClear()

    #Input glVertex Colors
    while True:
        bmp_r = input("\nHex color (R): ")
        bmp_g = input("\nHex color (G): ")
        bmp_b = input("\nHex color (B): ")
        try:
            bmp_r = float(bmp_r)
            bmp_g = float(bmp_g)
            bmp_b = float(bmp_b)
            if 0 <= bmp_g <= 1 and 0 <= bmp_g <= 1 and 0 <= bmp_b <= 1:
                break
        except ValueError:
            print("\n\nERROR: Por favor ingrese un numero entre 0 y 1.\n")

    #Input glVertex Colors
    bmp.glColor(bmp_r, bmp_g, bmp_b)

    bmp.glVertex(0, 0)
    bmp.glVertex(-1, -1)
    bmp.glVertex(-1, 1)
    bmp.glVertex(1, 1)
    bmp.glVertex(1, -1)

    #Output BMP
    bmp.glWrite("test.bmp")
