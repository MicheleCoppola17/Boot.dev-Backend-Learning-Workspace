/*
Assignment

Complete the coordinate_update_x and coordinate_update_and_return_x functions.

1. coordinate_update_x should update the x field with the provided new_x value. It returns void and should not update the caller's struct.
2. coordinate_update_and_return_x should update the x field with the provided new_x value, and then return the updated coordinate struct.
Remember, you can access the field of a struct with a . operator, like so:

car.tires = 4;
*/

#include "coordinate.h"
#include "munit.h"

coordinate_t new_coordinate(int x, int y, int z) {
  return (coordinate_t){.x = x, .y = y, .z = z};
}

munit_case(RUN, test_unchanged, {
  coordinate_t old = new_coordinate(1, 2, 3);
  munit_assert_int(old.x, ==, 1, "old.x must be 1");

  coordinate_update_x(old, 4);
  munit_assert_int(old.x, ==, 1, "old.x must still be 1");
});

munit_case(SUBMIT, test_changed, {
  coordinate_t old = new_coordinate(1, 2, 3);
  munit_assert_int(old.x, ==, 1, ".x must be 1");

  coordinate_t new = coordinate_update_and_return_x(old, 4);
  munit_assert_int(new.x, ==, 4, "new .x must be 4");
  munit_assert_int(old.x, ==, 1, "old.x must still be 1");

  // Notice, they have different addresses
  munit_assert_ptr_not_equal(&old, &new, "Must be different addresses");
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_unchanged", test_unchanged),
      munit_test("/test_changed", test_changed),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("pointers", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}
