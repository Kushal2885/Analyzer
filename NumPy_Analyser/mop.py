import numpy as np

def perform_addition(arr):
    req_size = arr.size
    user_input = input(f"Enter {req_size} elements separated by space: ")
    clean_data = list(map(int, user_input.split()))
    secondary_arr = np.array(clean_data).reshape(arr.shape)
    print("\nOriginal Array:\n", arr)
    print("Secondary Array:\n", secondary_arr)
    return np.add(arr, secondary_arr)

def perform_subtraction(arr):
    req_size = arr.size
    user_input = input(f"Enter {req_size} elements separated by space: ")
    clean_data = list(map(int, user_input.split()))
    secondary_arr = np.array(clean_data).reshape(arr.shape)
    print("\nOriginal Array:\n", arr)
    print("Secondary Array:\n", secondary_arr)
    return np.subtract(arr, secondary_arr)

def perform_multiplication(arr):
    req_size = arr.size
    user_input = input(f"Enter {req_size} elements separated by space: ")
    clean_data = list(map(int, user_input.split()))
    secondary_arr = np.array(clean_data).reshape(arr.shape)
    print("\nOriginal Array:\n", arr)
    print("Secondary Array:\n", secondary_arr)
    return np.multiply(arr, secondary_arr)

def perform_division(arr):
    req_size = arr.size
    user_input = input(f"Enter {req_size} elements separated by space: ")
    clean_data = list(map(int, user_input.split()))
    secondary_arr = np.array(clean_data).reshape(arr.shape)
    print("\nOriginal Array:\n", arr)
    print("Secondary Array:\n", secondary_arr)
    return np.divide(arr, secondary_arr)