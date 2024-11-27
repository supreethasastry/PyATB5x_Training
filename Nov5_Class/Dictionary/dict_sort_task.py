# Sort a dictionary by its values in descending order
my_dict = {"a": 3, "b": 1, "c": 2}

# {b: 1 , c: 2 , a :3}
print("Ascending")
sortdict=sorted(my_dict.items(),key=lambda x:x[1])
print(dict(sortdict))
print("Descending")
sortdict=sorted(my_dict.items(),key=lambda x:x[1], reverse=True)
print(dict(sortdict))

