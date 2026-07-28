/*
Assignment
Take a look at exercise.h. 
Write the implementation for the function prototype found there back in exercise.c. 
It should calculate whether the given temperature is too cold or too hot (it's already in Fahrenheit of course, the most reasonable scale for regular living).

1. Less than 70 returns "too cold".
2. More than 90 returns "too hot".
3. Otherwise return "just right".

(!) Do not add the \n to the end of the strings. That's done at print-time.
*/

#include "exercise.h"

char *get_temperature_status(int temp) {
    if (temp < 70) {
        return "too cold";
    } else if (temp > 90) {
        return "too hot";
    } else {
        return "just right";
    }
}
