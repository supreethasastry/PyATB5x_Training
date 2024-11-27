my_dict = {
    "name": "Suppie",
    "age": 31,
    "role": "SDET",
    "experience": 5.5
}
print(my_dict)
print(my_dict["age"])

my_dict["role"] = "Manual Tester"
print(my_dict)

del my_dict["age"]
print(my_dict)

for key, value in my_dict.items():
    print(key, " -> ", value)

print("age" in my_dict)
print("role" in my_dict)