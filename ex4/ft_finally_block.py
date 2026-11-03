#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant: str) -> None:
    if plant != plant.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant}'")
    print(f"Watering {plant}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def ft_finally_block() -> None:
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    array = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(array)
    print()
    print("Testing invalid plants...")
    array2 = ["Tomato", "lettuce"]
    test_watering_system(array2)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    ft_finally_block()
