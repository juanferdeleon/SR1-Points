/*#include <iostream>
#include <cstdint>
#include <fstream>
#include "bitmapinfoheader.h"
#include "bitmapfileheader.h"
#include "bitmap.h"

using namespace std;

Bitmap::Bitmap(int width, int height): _width(width), _height(height), m_pPixels(new uint8_t[width*height*3]{}){
    //Constructor

}

bool Bitmap::write(string fileName){

    BitmapFileHeader fileHeader;
    BitmapInfoHeader infoHeader;

    fileHeader.fileSize = sizeof(BitmapFileHeader) + sizeof(BitmapInfoHeader) + _width * _height * 3;
    fileHeader.dataOffset = sizeof(BitmapFileHeader) + sizeof(BitmapInfoHeader);

    infoHeader.width = _width;
    infoHeader.height = _height;

    ofstream file;
    file.open(fileName, ios::out | ios::binary);

    if(!file){
        return false;
    }

    file.write((char *)&fileHeader, sizeof(fileHeader));
    file.write((char *)&infoHeader, sizeof(infoHeader));
    file.write((char *)m_pPixels.get(), _width*_height*3);

    file.close();

    if(!file){
        return false;
    }

    return true;
}

void Bitmap::setPixel(int x, int y, uint8_t r, uint8_t g, uint8_t b){
    
    uint8_t *pPixel = m_pPixels.get();

    pPixel += (y * 3) * _width + (x * 3 );

    pPixel[0] = b;
    pPixel[1] = g;
    pPixel[2] = r;
}

Bitmap::~Bitmap(){
    //Destructor

}*/