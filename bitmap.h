/*
        SR1 Points

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Bitmap Class

*/

#ifndef BITMAP_H_
#define BITMAP_H_

#include <string>
#include <cstdint>
#include <memory>

using namespace std;

class Bitmap {

    private:
        int _width{0};
        int _height{0};
        unique_ptr<uint8_t[]> m_pPixels{nullptr};

    public:
        Bitmap(int width, int height);
        void setPixel(int x, int y, uint8_t r, uint8_t g, uint8_t b);
        bool write(string fileName);
        virtual ~Bitmap();

};

#endif