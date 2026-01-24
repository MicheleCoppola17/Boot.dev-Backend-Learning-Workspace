from math import isclose

from main import avg_luck_boost
from test_cases import run_cases


def test(luck_boosts: list[int], expected_avg: float) -> bool:
    print("---------------------------------")
    print(f"Party luck boosts: {luck_boosts}")

    try:
        avg = avg_luck_boost(luck_boosts)
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")
        return False

    print(f"Expected average boost: {expected_avg}")
    print(f"Actual average boost:   {avg}")
    if isclose(avg, expected_avg):
        print("Pass")
        return True

    print("Fail")
    return False


def main() -> None:
    passed = 0
    failed = 0

    for case in run_cases:
        correct = test(**case)
        if correct:
            passed += 1
        else:
            failed += 1

    print()

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    print(f"{passed} passed, {failed} failed")


main()
