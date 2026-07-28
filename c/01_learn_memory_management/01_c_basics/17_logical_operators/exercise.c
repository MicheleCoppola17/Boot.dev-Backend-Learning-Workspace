/*
Assignment
The Sneklang package manager needs an access control system for its private package registry. 
Take a look at exercise.h and implement the function in exercise.c.

The can_access_registry function should return 1 (true) if a user can access the private registry, or 0 (false) if they cannot.

A user can access the private registry if any of these conditions are met:

1. They have is_premium set to 1 (true)
2. They have both reputation >= 100 AND has_2fa (two-factor authentication) set to 1 (true)

(i) In C, we use 1 for true and 0 for false when returning boolean-like values from functions that return int.
*/

#include "exercise.h"

int can_access_registry(int is_premium, int reputation, int has_2fa) {
    return (is_premium || (reputation >= 100 && has_2fa));
}
