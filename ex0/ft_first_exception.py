def input_temperature(temp_str: str) -> int:
    return int(temp_str)
 
def check_temperature(temp: str) -> int:
     
	try:
		temp = input_temperature(temp)
	except ValueError as error:
		print(f"Caught input_temperature error: {error}")
	return temp
      
temp = check_temperature("4563456")
print(f"Input temperature: {temp}")