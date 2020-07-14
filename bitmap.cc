#include "bitmap.h"
#include "bitmapinfoheader.h"
#include "bitmapfileheader.h"

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

    return false;
}

void Bitmap::setPixel(int x, int y, uint8_t r, uint8_t g, uint8_t b){

}

Bitmap::~Bitmap(){
    //Destructor

}