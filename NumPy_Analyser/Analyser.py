import numpy as np
import nparr 
import mop
import comb_split

def search_value(arr):
    try:
        val = int(input("Enter the value to search: "))
        indices = np.where(arr == val)
        if indices[0].size > 0:
            print(f"\nValue {val} found at index positions:")
            for position in zip(*indices):
                print(position)
        else:
            print(f"\nValue {val} not found.")
    except ValueError:
        print("Invalid input.")

def sort_array(arr):
    print("\nOriginal Array:\n", arr)
    print("\nSorted Array (Row-wise):\n", np.sort(arr))

def filter_array(arr):
    try:
        print("\nFilter Options:\n1. > X\n2. < X")
        choice = int(input("Enter choice: "))
        val = int(input("Enter value (X): "))
        if choice == 1:
            print(f"\nElements > {val}:\n", arr[arr > val])
        elif choice == 2:
            print(f"\nElements < {val}:\n", arr[arr < val])
    except ValueError:
        print("Invalid input.")


def stat_sum(arr):
    print(f"\nSum of all elements: {np.sum(arr)}")

    if arr.ndim == 2:
        print(f"Sum of each Column: {np.sum(arr, axis=0)}")
        print(f"Sum of each Row:    {np.sum(arr, axis=1)}")

def stat_mean(arr):
    print(f"\nMean (Average): {np.mean(arr):.2f}")

def stat_median(arr):
    print(f"\nMedian: {np.median(arr)}")

def stat_std_var(arr):
    print(f"\nStandard Deviation: {np.std(arr):.2f}")
    print(f"Variance: {np.var(arr):.2f}")

def stat_min_max(arr):
    print(f"\nMinimum Value: {np.min(arr)}")
    print(f"Maximum Value: {np.max(arr)}")

if __name__ == "__main__":
    current_array = None

    while True:
        print("\nWelcome to NumPy Analyser!")
        print("==========================")
        print("1. Create Numpy Array")
        print("2. Perform Mathematical Operation")
        print("3. Combine or Split Array")
        print("4. Search, Sort, Filter Array")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 1:
            while True:
                print("\n1. Create 1D Array\n2. Create 2D Array\n3. Back")
                try:
                    sub = int(input("Enter choice: "))
                    if sub == 1:
                        current_array = nparr.get_1d_array()
                        if current_array is not None: print("1D Array Created:\n", current_array)
                    elif sub == 2:
                        current_array = nparr.get_2d_array()
                        if current_array is not None: print("2D Array Created:\n", current_array)
                    elif sub == 3:
                        break
                except ValueError: 
                    continue

        elif choice == 2:
            if current_array is None:
                print("\nERROR: No array found! Create one first.")
                continue
            while True:
                print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Back")
                try:
                    sub = int(input("Enter choice: "))
                    if sub == 1: print("\nResult:\n", mop.perform_addition(current_array))
                    elif sub == 2: print("\nResult:\n", mop.perform_subtraction(current_array))
                    elif sub == 3: print("\nResult:\n", mop.perform_multiplication(current_array))
                    elif sub == 4: print("\nResult:\n", mop.perform_division(current_array))
                    elif sub == 5: break
                except ValueError: continue

        elif choice == 3:
            if current_array is None:
                print("\nERROR: No array found! Please create an array (Option 1) first.")
                continue

            while True:
                print("\n--- Combine or Split ---")
                print("1. Combine Arrays")
                print("2. Split Array")
                print("3. Back to Main Menu")
                
                try:
                    sub_choice = int(input("Enter your choice: "))
                    
                    if sub_choice == 1:
                        comb_split.combine_arrays(current_array)
                    elif sub_choice == 2:
                        comb_split.split_array(current_array)
                    elif sub_choice == 3:
                        break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input.")
                    continue
        elif choice == 4:
            if current_array is None:
                print("\nERROR: No array found!")
                continue
            while True:
                print("\n1. Search\n2. Sort\n3. Filter\n4. Back")
                try:
                    sub = int(input("Enter choice: "))
                    if sub == 1: search_value(current_array)
                    elif sub == 2: sort_array(current_array)
                    elif sub == 3: filter_array(current_array)
                    elif sub == 4: break
                except ValueError: continue
        elif choice == 5:
            if current_array is None:
                print("\nERROR: No array found!")
                continue
            
            while True:
                print("\n--- Statistics Menu ---")
                print("1. Sum")
                print("2. Mean (Average)")
                print("3. Median")
                print("4. Std Deviation & Variance")
                print("5. Min & Max")
                print("6. Back")
                
                try:
                    sub = int(input("Enter choice: "))
                    if sub == 1: stat_sum(current_array)
                    elif sub == 2: stat_mean(current_array)
                    elif sub == 3: stat_median(current_array)
                    elif sub == 4: stat_std_var(current_array)
                    elif sub == 5: stat_min_max(current_array)
                    elif sub == 6: break
                except ValueError: continue

        elif choice == 6:
            print("Exiting...")
            break