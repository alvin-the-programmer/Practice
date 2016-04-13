#ifndef _PADDLE_H_
#define _PADDLE_H_

#include "pos.h"

class Paddle {
	private:
		int height;
		Pos position;
	public:
		Paddle();
		Paddle(int);
		int getHeight();
		// Pos getPos();
		// Pos setPos();
		void printPos();	
};

#endif