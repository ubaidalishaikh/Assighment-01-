def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Element at index {index} updated to '{new_value}'."
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    if 0 <= start < len(lst) and 0 <= end <= len(lst) and start <= end:
        return lst[start:end]
    else:
        return "Invalid slice range!"

def main():
    # Initialize list
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    while True:
        print("\nCurrent List:", my_list)
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                index = int(input("Enter the index to access: "))
                result = access_element(my_list, index)
                print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '2':
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                result = modify_element(my_list, index, new_value)
                print(result)
            except ValueError:
                print("Invalid input.")

        elif choice == '3':
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print("Sliced List:", result)
            except ValueError:
                print("Please enter valid integers.")

        elif choice == '4':
            print("Thanks for playing the Index Game!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()
