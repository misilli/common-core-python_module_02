#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def check_temperature(temp: str) -> None:
    temp_int: int
    try:
        temp_int = input_temperature(temp)
        print(f"Temperature is now {temp_int}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")


def ft_first_exception() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    check_temperature("25")
    print("Input data is 'abc'")
    check_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
