string = "Hello World"
integer = 10
float = 4.67
bool_is_active = True
bool_is_passive = False
list = ["potato", "tomato", "cucumber"]
dict = {"name": "Alice", "age": 26, "city": "Los Angeles"}
tuple = (40.7128, -74.0060)
result = None

# 2. operators
print("plus:", integer + float)
print("minus:", integer - float)
print("multiple:", integer * float)
print("split:", integer / float)

print("1)", integer == float)
print("2)", integer != float)
print("3)", integer < float)
print("4)", integer > float)

print("5)", integer and float)
print("6)", integer or float)

# 3.1
num_str = 125
num_str = str(num_str)
print(num_str)
print(type(num_str))

# 3.2
message = 'Hi, my name is Python!'
new_message = message.replace("y", "0").replace("i", "1")
print(new_message)

# 3.3
split_test = 'This is a split test'
split_list = split_test.split()
string_join= ' '.join(split_list)
print("list before split:", split_list)
print("list after join:", string_join)

# 3.4
string_join_len = len(string_join)
print("length of the string:", string_join_len)

# lists
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print("list_append:", list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print("list_extend:", list_extend)

print("index of 6:", list_extend.index(6))

print("length of list:", len(list_append))

# dictionary
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}

if "car" and "where" in dict_test:
    print(dict_test["car"],",", dict_test["where"])

print(dict_test.keys(),":", dict_test.values())

print("key: value")
for key, value in dict_test.items():
    print(f"{key}: {value}")