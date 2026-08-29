/*
Assignment
Complete the smart_append function. It appends a src string to the buffer field inside the dest TextBuffer struct.

The TextBuffer struct tracks both the buffer and its current length. It's called a "smart" append because the destination buffer is a fixed 64 bytes, and it:

- Checks for available space before appending.
- Appends as much as possible if there's not enough space.
- Always ensures the buffer remains null-terminated.
- Returns a status indicating whether the full append was possible.

Here are the steps:

1. If either the dest or src input is NULL, return 1 (failure). The input pointer checks can be done with ptr == NULL or !ptr.
(i) In C, NULL represents a null pointer, which does not point to a value.
2. Create a constant to represent the max buffer size of 64.
3. Get the length of the src string using strlen.
4. Calculate the remaining space in the dest buffer. Notice that it stores its own length. The 64-byte buffer can hold 63 characters plus the null terminator.
5. If the src string is larger than the remaining space:
    1. Copy as much of the src string as possible to the dest buffer using strncat.
    2. Update the dest buffer length to the max size, accounting for the null terminator.
    3. Return 1 (failure) to indicate the full append wasn't possible.
6. Otherwise, if there's enough space:
    1. Append the entire src string to the dest buffer using strcat.
    2. Update the dest buffer length.
    3. Return 0 (success) to indicate the full append was possible.
*/

#include "exercise.h"
#include "munit.h"
#include <string.h>

munit_case(RUN, test_return_1_for_null_value, {
  TextBuffer dest;
  const char *src = NULL;
  int result = smart_append(&dest, src);
  munit_assert_int(result, ==, 1, "Should return 1 for null value");
});

munit_case(RUN, test_smart_append_empty_buffer, {
  TextBuffer dest;
  strcpy(dest.buffer, "");
  dest.length = 0;
  const char *src = "Hello";
  int result = smart_append(&dest, src);
  munit_assert_int(result, ==, 0, "Should return 0 for successful append");
  munit_assert_string_equal(dest.buffer, "Hello",
                            "Buffer should contain 'Hello'");
  munit_assert_int(dest.length, ==, 5, "Length should be 5");
});

munit_case(SUBMIT, test_smart_append_full_buffer, {
  TextBuffer dest;
  strcpy(dest.buffer,
         "This is a very long string that will fill up the entire buffer.");
  dest.length = 63;
  const char *src = " Extra";
  int result = smart_append(&dest, src);
  munit_assert_int(result, ==, 1, "Should return 1 for unsuccessful append");
  munit_assert_string_equal(
      dest.buffer,
      "This is a very long string that will fill up the entire buffer.",
      "Buffer should remain unchanged");
  munit_assert_int(dest.length, ==, 63, "Length should remain 63");
});

munit_case(SUBMIT, test_smart_append_overflow, {
  TextBuffer dest;
  strcpy(dest.buffer, "This is a long string");
  dest.length = 21;
  const char *src = " that will fill the whole buffer and leave no space for "
                    "some of the chars.";
  int result = smart_append(&dest, src);
  munit_assert_int(result, ==, 1, "Should return 1 for overflow append");
  munit_assert_string_equal(
      dest.buffer,
      "This is a long string that will fill the whole buffer and leave",
      "Buffer should be filled to capacity");
  munit_assert_int(dest.length, ==, 63,
                   "Length should be 63 after overflow append");
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_return_1_for_null_value", test_return_1_for_null_value),
      munit_test("/test_smart_append_empty_buffer",
                 test_smart_append_empty_buffer),
      munit_test("/test_smart_append_full_buffer",
                 test_smart_append_full_buffer),
      munit_test("/test_smart_append_overflow", test_smart_append_overflow),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("smart_append", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}
