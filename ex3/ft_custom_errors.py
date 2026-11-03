#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def ft_check_custom_errors(operation_number: int) -> None:
    try:
        if operation_number == 0:
            raise PlantError("The tomato plant is wilting!")
        elif operation_number == 1:
            raise WaterError("Not enough water in the tank!")
        else:
            pass
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def ft_check_garden_errors(operation_number: int) -> None:
    try:
        if operation_number == 0:
            raise PlantError("The tomato plant is wilting!")
        elif operation_number == 1:
            raise WaterError("Not enough water in the tank!")
        else:
            pass
    except GardenError as error:
        print(f"Caught GardenError: {error}")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    ft_check_custom_errors(0)
    print()
    print("Testing WaterError...")
    ft_check_custom_errors(1)
    print()
    print("Testing catching all garden errors...")
    ft_check_garden_errors(0)
    ft_check_garden_errors(1)
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
