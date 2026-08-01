/*
Assignment
Re-arrange the fields in sneklang_var_t so that the padding is optimal and the tests in main.c pass.
*/

#include "exercise.h"
#include "munit.h"

munit_case(RUN, test_optimal_size, {
  assert_int(sizeof(sneklang_var_t), ==, 24, "Should be 24 (in WebAssembly)");
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_optimal_size", test_optimal_size),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("padding", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}
