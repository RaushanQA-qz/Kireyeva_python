# --- TASK 1: Number Check ---
try:
    number = float(input("Enter a number: "))
    if number > 7:
        print("Hello")
except ValueError:
    print("Error: Please enter a valid number.")

# --- TASK 2: Name Check ---
name = input("Enter a name: ")
if name == "John":
    print("Hello, John")
else:
    print("There is no such name")

# --- TASK 3: Multiples of 3 ---
try:
    numbers_input = input("Enter numeric array (numbers separated by space): ")
    # Превращаем строку в список чисел
    array = [int(x) for x in numbers_input.split()]

    print("Elements multiple of 3:")
    for element in array:
        if element % 3 == 0:
            print(element)
except ValueError:
    print("Error: Please enter integers only.")