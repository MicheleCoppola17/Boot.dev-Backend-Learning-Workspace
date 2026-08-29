/*
Assignment
At Sneklang, we have a bit of "not invented here" culture. As such, we've decided to implement our own string concatenation function.

Complete the concat_strings function. It should append str2 to the end of str1 in place. Here are the steps:

1. Find the null terminator ('\0') of str1
2. Iterate over str2 and copy each character to the memory locations at the end of str1.
3. Add a null terminator at the end of the concatenated string.

Don't cheat and use strcat!

str1 is already allocated with enough memory to hold the concatenated string, so don't worry about that.
*/

#include "exercise.h"
#include "munit.h"
#include <string.h>

munit_case(RUN, test_concat_empty_strings, {
  char str1[100] = "";
  const char *str2 = "";
  concat_strings(str1, str2);
  munit_assert_string_equal(
      str1, "",
      "Concatenating two empty strings should result in an empty string");
});

munit_case(RUN, test_concat_empty_to_nonempty, {
  char str1[100] = "Hello";
  const char *str2 = "";
  concat_strings(str1, str2);
  munit_assert_string_equal(str1, "Hello",
                            "Concatenating an empty string to a non-empty "
                            "string should not change the original string");
});

munit_case(RUN, test_concat_small_strings, {
  char str1[100] = "Hello ";
  const char *str2 = "World";
  concat_strings(str1, str2);
  munit_assert_string_equal(str1, "Hello World",
                            "Concatenating strings should work correctly");
});

munit_case(SUBMIT, test_concat_long_strings, {
  char str1[200] = "This is a longer string that ";
  const char *str2 = "will be concatenated with another long string.";
  concat_strings(str1, str2);
  munit_assert_string_equal(
      str1,
      "This is a longer string that will be concatenated with another long "
      "string.",
      "Concatenating longer strings should work correctly");
});

munit_case(SUBMIT, test_concat_nonempty_to_empty, {
  char str1[100] = "";
  const char *str2 = "Hello";
  concat_strings(str1, str2);
  munit_assert_string_equal(
      str1, "Hello",
      "Concatenating a string to an empty should change the original string");
});

munit_case(RUN, test_concat_null_terminator_explicit, {
  char str1[10];
  memset(str1, 'x', sizeof(str1));
  str1[0] = 'A';
  str1[1] = 'B';
  str1[2] = '\0';

  const char *str2 = "CD";
  concat_strings(str1, str2);

  munit_assert_string_equal(str1, "ABCD", "Content should match");
  munit_assert_int(str1[4], ==, '\0',
                   "Must explicitly write null terminator at the end");
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_concat_small_strings", test_concat_small_strings),
      munit_test("/test_concat_empty_strings", test_concat_empty_strings),
      munit_test("/test_concat_empty_to_nonempty",
                 test_concat_empty_to_nonempty),
      munit_test("/test_concat_long_strings", test_concat_long_strings),
      munit_test("/test_concat_nonempty_to_empty",
                 test_concat_nonempty_to_empty),
      munit_test("/test_concat_null_terminator_explicit",
                 test_concat_null_terminator_explicit),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("concat_strings", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}
