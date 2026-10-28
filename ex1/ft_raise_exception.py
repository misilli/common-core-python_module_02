from typing import Optional


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


def check_temperature(temp: str) -> None:
    try:
        temp = input_temperature(temp)
        print(f"Temperature is now {temp}°C")
    except TemperatureError as error:
        print(f"Caught input_temperature error: {error}")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

def ft_raise_exception():
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    check_temperature("25")
    print()
    print("Input data is 'abc'")
    check_temperature("abc")
    print()
    print("Input data is '100'")
    check_temperature("100")
    print()
    print("Input data is '-50'")
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    ft_first_exception()