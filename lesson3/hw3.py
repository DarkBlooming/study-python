# conditional constructions
# --- 1 ---
correct_password = "password123"
input_password = input("Enter the password: ")

if input_password == correct_password:
    print("Your password is correct")
else:
    print("Wrong password")

# --- 2 ---
day_number = int(input("Enter number of the day (1-7): "))

day_of_week = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}

if day_number in day_of_week:
    print(f"It's {day_of_week[day_number]}.")
else:
    print("Wrong day number. Please, enter a number from 1 to 7.")

# Cycles
# --- 1 ---
number = int(input("Enter the number: "))
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# --- 2 ---
list_of_numbers = [1, 4, 3, 6, 10, 7]
sum = 0
for number in list_of_numbers:
    sum += number

print(f"List: {list_of_numbers}")
print(f"List sum: {sum}")

# --- 3 ---
num_for_fact = int(input("Enter your number: "))
factorial = 1

if num_for_fact < 0:
    print("Factorial is defined only for non-negative numbers.")
elif num_for_fact == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, num_for_fact + 1):
        factorial *= i
        print(f"Factorial of {num_for_fact} is {factorial}.")

# --- 4 ---
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
print(f"Even numbers from {start} to {end}:", even_numbers)

# --- 5 ---
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

plain_numbers = [num for num in range(start, end + 1)
                 if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

print(f"Plain numbers: {plain_numbers}")
