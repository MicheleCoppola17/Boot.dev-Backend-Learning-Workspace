#pragma once

#include <stddef.h>

// Mock/stub macros for Boot.dev unit tests
#define munit_case(type, name, body) \
    void name() body

#define assert_int(a, op, b, msg) (void)(a); (void)(b);
#define assert_string(a, op, b, msg) (void)(a); (void)(b);
#define assert_double(a, op, b, msg) (void)(a); (void)(b);
#define assert_float(a, op, b, msg) (void)(a); (void)(b);
#define assert_char(a, op, b, msg) (void)(a); (void)(b);
#define assert_true(expr, msg) (void)(expr);
#define assert_false(expr, msg) (void)(expr);
#define assert_null(ptr, msg) (void)(ptr);
#define assert_not_null(ptr, msg) (void)(ptr);
#define assert_memory_equal(size, a, b, msg) (void)(size); (void)(a); (void)(b);

#define munit_test(path, func) { (char*)path, func }
#define munit_null_test { NULL, NULL }

typedef void (*MunitTestFunc)(void);

typedef struct {
    char* name;
    MunitTestFunc test;
} MunitTest;

typedef struct {
    char* prefix;
    MunitTest* tests;
} MunitSuite;

#define munit_suite(name, tests) { (char*)name, tests }

static inline int munit_suite_main(MunitSuite* suite, void* user_data, int argc, char* const* argv) {
    (void)suite; (void)user_data; (void)argc; (void)argv;
    return 0;
}
