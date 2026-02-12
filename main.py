# --- TASK 1: Number Check (With Float support) ---
try:
    user_input = input("Enter a number: ")
    number = float(user_input)
    if number > 7:
        print("Hello")
    else:
        print("Number is 7 or less, no greeting.") # Feedback for users
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")

# --- TASK 2: Name Check (Case-insensitive) ---
name = input("Enter a name: ")
if name.strip().lower() == "john":
    print("Hello, John")
else:
    print("There is no such name")

# --- TASK 3: Multiples of 3 (With validation) ---
try:
    numbers_input = input("Enter numbers separated by space: ")
    raw_list = numbers_input.split()
    array = []
    
    for item in raw_list:
        try:
            array.append(int(item))
        except ValueError:
            continue  

    result = [x for x in array if x % 3 == 0]
    
    if result:
        print(f"Elements multiple of 3: {result}")
    else:
        print("No numbers multiple of 3 found.")
except Exception as e:
    print(f"Something went wrong: {e}")
