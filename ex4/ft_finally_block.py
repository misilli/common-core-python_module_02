class GardenError(Exception):
    pass

class plantError(GardenError):
    pass


def ft_plant_water(plant : str , error_code : int) :
    if error_code == 1:
        raise GardenError(f" Invalid plant name to water: ''")

    print(f"Watering {plant}:", end = " ")

def ft_check_finally_block(plant : str , error_code : int) -> None:
    try:
        ft_plant_water(plant, error_code)
        print("[OK]")
    except plantError as error:
        print(f"Caught plantError: {error}")
    finally:
        print("Closing watering system")
        
        
def ft_finally_block() -> None:
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    print("Opening watering system")
    ft_check_finally_block("Tomato",0)
    ft_check_finally_block("Lettuce",0)
    ft_check_finally_block("Carrots",0)

    """büyük harfa göre hata vercek düzelt
    """    
    ft_check_finally_block("Tomato",1)
    ft_check_finally_block("lettuce",0)
    
    
if __name__ == "__main__":
    ft_finally_block()