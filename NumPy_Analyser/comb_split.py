import numpy as np

def combine_arrays(arr):
    if arr is None:
        print("No array found to combine.")
        return

    print("\nCombine Arrays:")
    print("1. Vertical Stack (Add rows to bottom)")
    print("2. Horizontal Stack (Add columns to side)")
    
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            rows = int(input("Enter number of rows for new array: "))
            cols = arr.shape[1] 
            req_elements = rows * cols
            print(f"Please enter {req_elements} elements (because original has {cols} columns).")
            
        elif choice == 2:
            rows = arr.shape[0] 
            cols = int(input("Enter number of columns for new array: "))
            req_elements = rows * cols
            print(f"Please enter {req_elements} elements (because original has {rows} rows).")
        else:
            print("Invalid choice.")
            return

        user_input = input(f"Enter elements separated by space: ")
        clean_data = list(map(int, user_input.split()))
        second_arr = np.array(clean_data).reshape(rows, cols)
        if choice == 1:
            result = np.vstack((arr, second_arr))
            stack_type = "Vertical Stack"
        else:
            result = np.hstack((arr, second_arr))
            stack_type = "Horizontal Stack"
        print("\nOriginal Array:")
        print(arr)
        
        print("\nSecond Array:")
        print(second_arr)
        
        print(f"\nCombined Array ({stack_type}):")
        print(result)

    except ValueError:
        print("Error: Invalid input or dimension mismatch.")
    except Exception as e:
        print(f"Error: {e}")

def split_array(arr):
    if arr is None:
        print("No array found.")
        return

    print("\nSplit Array:")
    print("1. Vertical Split")
    print("2. Horizontal Split")
    
    try:
        choice = int(input("Enter choice: "))
        splits = int(input("Enter number of sections to split into: "))

        if choice == 1:
            result = np.vsplit(arr, splits)
        elif choice == 2:
            result = np.hsplit(arr, splits)
        else:
            print("Invalid choice.")
            return

        print(f"\nResult ({splits} arrays):")
        for i, sub_arr in enumerate(result):
            print(f"Array {i+1}:\n{sub_arr}\n")

    except ValueError:
        print(f"Error: Cannot split array of shape {arr.shape} into {splits} equal parts.")