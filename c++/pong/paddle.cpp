#include "paddle.h"

#include <iostream>
#include <cmath>

using namespace std;

Paddle::Paddle() {
	this->height = 3;
}

Paddle::Paddle(int h) {
	this->height = abs(h);
}

int Paddle::getHeight() {
	return this->height;
}

// Pos Paddle::getPos() {
// 	return this->position;
// }

// void Paddle::printPos() {
// 	this->position.printCoords();
// }

// Pos Paddle::setPos() {
// 	return 
// }