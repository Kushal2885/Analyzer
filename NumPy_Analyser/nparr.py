import numpy as np

def get_1d_array():
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        clean_data = list(map(int, user_input.split()))
        np_arr = np.array(clean_data)
        return np_arr.flatten()
    except ValueError:
        print("Error: Please enter valid integers.")
        return np.array([])

def get_2d_array():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        user_input = input(f"Enter {rows * cols} numbers separated by spaces: ")
        elements = list(map(int, user_input.split()))
        if len(elements) != rows * cols:
            print(f"Error: You entered {len(elements)} numbers, but needed {rows * cols}.")
            return None
        np_arr = np.array(elements).reshape(rows, cols)
        return np_arr
    except ValueError:
        print("Error: Invalid input. Please enter integers only.")
        return None