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

    def __init__(self, heigh, width):
        '''Constructor'''
        self.heigh = heigh
        self.width = width
        self.frambufer = []
        self.clear_color = color(0, 0, 0)
        self.glClear()

    def glInit(self):
        pass

    def glClear(self):
        '''Set all pixels to same color'''
        self.frambufer = [
            [self.clear_color for x in range(self.width)] for y in range(self.heigh)
        ]
    
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
				bmp_file.write(self.pixels[x][y])
        
        bmp_file.close()