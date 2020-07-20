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

