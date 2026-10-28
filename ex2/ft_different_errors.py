def ft_error(operation: str) -> None:
    if operation == "0":
        int("abc")
    elif operation == "1":
        0/0
    elif operation == "2":
        open("/non/existent/file")
    elif operation == "3":
        "1" + 1
    elif operation == "4":
        pass


def ft_check_errors(operation: str) -> None:
    try:
        ft_error(operation)
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")

def ft_different_errors() ->None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    ft_check_errors("0")
    print("Testing operation 1...")
    ft_check_errors("1")
    print("Testing operation 2...")
    ft_check_errors("2")
    print("Testing operation 3...")
    ft_check_errors("3")
    print("Testing operation 4...")
    ft_check_errors("4")
    print("Operation completed successfully")
    print()
    print("All error types tested successfully!")
if __name__ == "__main__":
    ft_different_errors()