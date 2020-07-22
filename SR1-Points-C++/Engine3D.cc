/*
        SR1 Points

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

*/

#include <iostream>
#include "bitmap.h"

using namespace std;

int main() {

    int const WIDTH = 800;
    int const HEIGHT = 600;

    Bitmap bitmap(WIDTH, HEIGHT);

    bitmap.setPixel(WIDTH/2, HEIGHT/2, 255, 255, 255);

    bitmap.write("test.bmp");

    cout<<"Finished"<<endl;
    
    return 0;
}