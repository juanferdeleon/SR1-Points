'''
        SR1 Points

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Bitmap Class

'''

import struct

def char(c):
    '''1 Byte'''

    return struct.pack('=c', c.encode('ascii'))

def word(w):
    '''2 Bytes'''

    return struct.pack('=h', w)

def dword(d):
    '''4 Bytes'''

    return struct.pack('=l', d)

def color(r,g,b):
    '''Set pixel color'''

    return bytes([b, g, r])

class Bitmap(object):
    '''Bitmap Class'''

    def __init__(self, height, width):
        '''Constructor'''

        self.height = height
        self.width = width
        self.framebuffer = []
        self.clear_color = color(255, 255, 255)
        self.vertex_color = color(255, 0, 0)
        self.glClear()

    def glInit(self):
        '''Initialize any internal objects that your renderer software requires'''

        pass

    def glCreateWindow(self, height, width):
        '''Initialize framebuffer, img will be this size'''

        self.height = height
        self.width = width
        self.glClear()
    
    def glViewPort(self, x, y, width, height):
        '''Define the area of the image to draw on'''

        self.x = x
        self.y = y
        self.vpx = width
        self.vpy = height

    def glClear(self):
        '''Set all pixels to same color'''

        self.framebuffer = [
            [self.clear_color for x in range(self.width)] for y in range(self.height)
        ]
    
    def glClearColor(self, r, g, b):
        '''Can change the color of glClear(), parameters must be numbers in the 
        range of 0 to 1.'''

        try:
            self.rc = round(255*r)
            self.gc = round(255*g)
            self.bc = round(255*b)
            self.clear_color = color(self.rc, self.rg, self.rb)
        except ValueError:
            print('\nERROR: Please enter a number between 1 and 0\n')
    
    def glVertex(self, x, y):
        '''Change the color of a point on the screen. The x, y coordinates are 
        specific to the viewport that they defined with glViewPort().'''

        if x <= 1 and x>= -1 and y >= -1 and y <= 1:
                
                if x > 0:
                        self.vx = self.x + round(round(self.vpx/2)*x) - 1
                if y > 0:
                        self.vy = self.y + round(round(self.vpy/2)*y) - 1
                if x <= 0:
                        self.vx = self.x + round(round(self.vpx/2)*x)
                if y <= 0:
                        self.vy = self.y + round(round(self.vpy/2)*y)
                
                self.point(self.vx,self.vy, self.vertex_color)
        else:
                pass
    
    def glColor(self, r, g, b):
        '''Change the color glVertex() works with. The parameters must 
        be numbers in the range of 0 to 1.'''

        try:
            self.rv = round(255*r)
            self.gv = round(255*g)
            self.bv = round(255*b)
            self.vertex_color = color(self.rv,self.gv,self.bv)
        except ValueError:
                print('\nERROR: Please enter a number between 1 and 0\n')

    def point(self, x, y, color):
        '''Draw a point'''
        try:
                self.framebuffer[y][x] = color
        except IndexError:
                print("\nPixel is outside the limits of the image\n")
    
    def glWrite(self, file_name):
        '''Write Bitmap File'''
        
        bmp_file = open(file_name, 'wb')

        #File header 14 bytes
        bmp_file.write(char('B'))
        bmp_file.write(char('M'))
        bmp_file.write(dword(14 + 40 + self.width * self.height))
        bmp_file.write(dword(0))
        bmp_file.write(dword(14 + 40))
        
        #File info 40 bytes
        bmp_file.write(dword(40))
        bmp_file.write(dword(self.width))
        bmp_file.write(dword(self.height))
        bmp_file.write(word(1))
        bmp_file.write(word(24))
        bmp_file.write(dword(0))
        bmp_file.write(dword(self.width * self.height * 3))
        bmp_file.write(dword(0))
        bmp_file.write(dword(0))
        bmp_file.write(dword(0))
        bmp_file.write(dword(0))

        # Pixeles, 3 bytes each
        for x in range(self.height):
            for y in range(self.width):
                bmp_file.write(self.framebuffer[x][y])
            
        bmp_file.close()