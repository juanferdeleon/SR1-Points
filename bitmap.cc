#include "bitmap.h"

Bitmap::Bitmap(int width, int height): _width(width), _height(height), m_pPixels(new uint8_t[width*height*3]){
    //Constructor

}

bool Bitmap::write(string fileName){
    return false;
}

void Bitmap::setPixel(int x, int y, uint8_t r, uint8_t g, uint8_t b){

}

Bitmap::~Bitmap(){
    //Destructor

}