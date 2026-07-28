/*
Assignment
Implement the print_numbers_reverse prototyped in exercise.h. 
It takes a starting number (higher) and an ending number (lower) and prints all the numbers in that range from highest to lowest inclusive.
*/

#include <stdio.h>

void print_numbers_reverse(int start, int end) {
    int i = end;
    while (i >= start) {
        printf("%d\n", i);
        i--;
    }
}