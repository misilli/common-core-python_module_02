class GardenError(Exception):
    pass

class plantError(GardenError):
    pass

class waterError(GardenError):
    pass

def ft_check_custom_errors(operation: str) -> None:
    try:
        if operation == "0":
            raise plantError("The tomato plant is wilting!")
        elif operation == "1":
            raise waterError("Not enough water in the tank!")
        elif operation == "2":
            raise GardenError("General garden error occurred")
        elif operation == "3":
            pass
    except plantError as error:
        print(f"Caught plantError: {error}")
    except waterError as error:
        print(f"Caught waterError: {error}")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        
def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    ft_check_custom_errors("0")
    print()
    print("Testing WaterError...")
    ft_check_custom_errors("1")
    print()
    print("Testing catching all garden errors...")
    ft_check_custom_errors("0")
    ft_check_custom_errors("1")
    print()
    print("All custom error types work correctly!")

if __name__ == "__main__":
    ft_custom_errors()