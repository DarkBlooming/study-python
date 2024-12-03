# Lists
# ---1---
list_of_numbers = [3, 2, 5, 6, 9]
list_of_numbers.append(10)
list_of_numbers.append(20)
print(f"List before: {list_of_numbers}")
list_of_numbers.pop(-2)
print(f"List after: {list_of_numbers}")

# ---2---
sum_list = [2, 5, 6, 7, 4, 9, 8]
print(f"Sum: {sum(sum_list)}")

# ---3---
numbers = [1, 2, 3, 4, 5]
double_numbers = []
for num in numbers:
    double_numbers.append(num * 2)
print(f"Double number list: {double_numbers}")

#Tuples
# ---1---
tuple = ("apple", "banana", "orange")
for fruit in tuple:
    print(fruit)

# ---2---
tuple1 = (1, 2, 3)
tuple2 = (7, 8, 9)
combined_tuple = tuple1 + tuple2
print(f"Combined tuple: {combined_tuple}")

#Dictionary
# ---1---
sportsman = {"name" : "Yaroslava Mahuchikh",
             "age" : 23,
             "sport" : "athletics",
             "weight" : "55 kg",
             "city" : "Dnipro"}
print(">-------<")
for key, value in sportsman.items():
    print(f"{key}: {value}")

# ---2---
favourite_books = {"Dearly Devoted Dexter" : 2005,
                   "Sweetpea" : 2017,
                   "No Longer Human" : 1948}

favourite_books["Witcher"] = 1993

print(f">--Updated list of my favourite books--<")
for key, value in favourite_books.items():
    print(f"{key}: {value}")

# ---3---
countries = {"USA" : "Washington",
             "England" : "London",
             "Sweden" : "Stockholm",
             "France" : "Paris",
             "Japan" : "Tokyo"}
country = input("Enter the country you need: ")
if country in countries:
    print(f"The capital of {country} is {countries[country]}")
else:
    print("There's no such a country in the dictionary")