def create_list():
    n = int(input("Enter number of elements for the list: "))
    return [int(input(f"Enter element {i+1}: ")) for i in range(n)]

def create_dict():
    n = int(input("Enter number of key-value pairs for the dictionary: "))
    return {input(f"Enter key {i+1}: "): input(f"Enter value for key {i+1}: ") for i in range(n)}

def create_set():
    n = int(input("Enter number of elements for the set: "))
    return {int(input(f"Enter element {i+1}: ")) for i in range(n)}

def create_tuple():
    n = int(input("Enter number of elements for the tuple: "))
    return tuple(int(input(f"Enter element {i+1}: ")) for i in range(n))

def list_operations():
    my_list = create_list()
    print("Original List:", my_list)
    
    while True:
        choice = int(input("Choose operation: 1. Append 2. Reverse 3. Delete 0. Exit: "))
        if choice == 1:
            elem = int(input("Enter element to append: "))
            my_list.append(elem)
            print("List after appending:", my_list)
        elif choice == 2:
            my_list.reverse()
            print("Reversed List:", my_list)
        elif choice == 3:
            del my_list
            print("List deleted")
            break
        elif choice == 0:
            break
        else:
            print("Invalid choice, please try again.")

def dict_operations():
    my_dict = create_dict()
    print("Original Dictionary:", my_dict)
    
    while True:
        choice = int(input("Choose operation: 1. Append 2. Reverse 3. Delete 0. Exit: "))
        if choice == 1:
            key = input("Enter key to append: ")
            value = input("Enter value for the key: ")
            my_dict[key] = value
            print("Dictionary after appending:", my_dict)
        elif choice == 2:
            reversed_dict = {k: my_dict[k] for k in reversed(my_dict)}
            print("Reversed Dictionary:", reversed_dict)
        elif choice == 3:
            del my_dict
            print("Dictionary deleted")
            break
        elif choice == 0:
            break
        else:
            print("Invalid choice, please try again.")

def set_operations():
    my_set = create_set()
    print("Original Set:", my_set)
    
    while True:
        choice = int(input("Choose operation: 1. Add 2. Reverse 3. Delete 0. Exit: "))
        if choice == 1:
            elem = int(input("Enter element to add: "))
            my_set.add(elem)
            print("Set after adding:", my_set)
        elif choice == 2:
            reversed_set = set(reversed(list(my_set)))
            print("Reversed Set (as a list):", reversed_set)
        elif choice == 3:
            del my_set
            print("Set deleted")
            break
        elif choice == 0:
            break
        else:
            print("Invalid choice, please try again.")

def tuple_operations():
    my_tuple = create_tuple()
    print("Original Tuple:", my_tuple)
    
    while True:
        choice = int(input("Choose operation: 1. Append 2. Reverse 3. Delete 0. Exit: "))
        if choice == 1:
            elem = int(input("Enter element to append: "))
            my_tuple = my_tuple + (elem,)
            print("Tuple after appending:", my_tuple)
        elif choice == 2:
            reversed_tuple = my_tuple[::-1]
            print("Reversed Tuple:", reversed_tuple)
        elif choice == 3:
            del my_tuple
            print("Tuple deleted")
            break
        elif choice == 0:
            break
        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        data_type = int(input("Choose data type to operate on: 1. List 2. Dictionary 3. Set 4. Tuple 0. Exit: "))
        if data_type == 1:
            list_operations()
        elif data_type == 2:
            dict_operations()
        elif data_type == 3:
            set_operations()
        elif data_type == 4:
            tuple_operations()
        elif data_type == 0:
            break
        else:
            print("Invalid choice, please try again.")
        print()

if __name__ == "__main__":
    main()