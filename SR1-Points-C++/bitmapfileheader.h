/*
        SR1 Points

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Bitmap File Header

*/

#ifndef BITMAPFILEHEADER_H_
#define BITMAPFILEHEADER_H_

#include <cstdint>

using namespace std;

#pragma pack(2) //Align all header info in 2 bite boundaries

struct BitmapFileHeader {
    char header[2]{'B', 'M'};
    int32_t fileSize;
    int32_t reserved{0};
    int32_t dataOffset;
};

#endif