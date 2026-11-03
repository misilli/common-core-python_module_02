#!/usr/bin/env python3

class TemperatureError(ValueError):
    pass


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise TemperatureError(
            f"{temp}°C is too hot for plants (max 40°C)"
        )
    if temp < 0:
        raise TemperatureError(
            f"{temp}°C is too cold for plants (min 0°C)"
        )
    return temp


def test_temperature(temp: str) -> None:
    try:
        temp_int = input_temperature(temp)
        print(f"Temperature is now {temp_int}°C")
    except (TemperatureError, ValueError) as error:
        print(f"Caught input_temperature error: {error}")


def ft_raise_exception() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    test_temperature("25")
    print()
    print("Input data is 'abc'")
    test_temperature("abc")
    print()
    print("Input data is '100'")
    test_temperature("100")
    print()
    print("Input data is '-50'")
    test_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_raise_exception()
