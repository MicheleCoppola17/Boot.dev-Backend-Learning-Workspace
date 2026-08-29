/*
Take a look at the dump_graphics function. It works similarly to the example above.

Go ahead and run it in its current state. 
You should notice that after all the values specified in main.c are printed... all hell breaks loose. 
That's because we've ventured out of the bounds of our array! We're going rogue! We're in the weeds! We're in undefined territory. 
This is something you do not want to do. It's one of the things that makes C powerful but dangerous.
Other languages stop you from going out of bounds, but C will let you fly off the edge of the world.

Fix the loop to only print the values that are actually in the array of structs. 
Take a look at the graphics_t struct in exercise.h to figure out how large each struct is.
*/

#include "exercise.h"
#include "munit.h"

int main() {
  graphics_t graphics_array[10] = {
      {60, 1080, 1920},  {30, 720, 1280},  {144, 1440, 2560}, {75, 900, 1600},
      {120, 1080, 1920}, {60, 2160, 3840}, {240, 1080, 1920}, {60, 768, 1366},
      {165, 1440, 2560}, {90, 1200, 1920},
  };
  dump_graphics(graphics_array);
  return 0;
}
