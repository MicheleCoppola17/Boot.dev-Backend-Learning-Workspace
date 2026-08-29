/*
Assignment
Complete the update_file function. The filedata array is a large 200-integer array representing a Sneklang source file. Each integer in the array represents a special piece of data.

- Index 1 is the number of lines
- Index 2 is the filetype
- Index 199 is always 0

Update the function so that it:
1. overwrites indexes 1 and 2 with the provided values
2. ensures that index 199 is always 0

(!) By modifying the array within your function, you're changing the values of the original array, not just a copy. More on that later.
*/

#include "exercise.h"
#include "munit.h"

munit_case(RUN, test_update_file_basic, {
  int filedata[200] = {0};
  update_file(filedata, 1, 100);
  munit_assert_int(filedata[1], ==, 100,
                   "Number of lines should be updated to 100");
  munit_assert_int(filedata[2], ==, 1, "File type should be updated to 1");
  munit_assert_int(filedata[199], ==, 0, "Last element should be set to 0");
});

munit_case(SUBMIT, test_update_file_different_values, {
  int filedata[200] = {0};
  for (int i = 0; i < 200; i++) {
    filedata[i] = 69;
  }
  update_file(filedata, 3, 250);
  munit_assert_int(filedata[1], ==, 250,
                   "Number of lines should be updated to 250");
  munit_assert_int(filedata[2], ==, 3, "File type should be updated to 3");
  munit_assert_int(filedata[199], ==, 0, "Last element should be set to 0");
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_update_file_basic", test_update_file_basic),
      munit_test("/test_update_file_different_values",
                 test_update_file_different_values),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("update_file", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}
