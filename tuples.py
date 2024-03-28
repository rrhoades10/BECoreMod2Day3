# Tuples In Python
# immutable list
# immutable means it cannot be changed

# delcaring tuples ()
empty_tuple = ()
# cannot add to a tuple
# empty_tuple.add(1)
# empty_tuple.append("hello")

swamp = ("Shrek", "Fiona") # no one allowed in our out of the swamp

# creating a tuple with a series of values separated by commas
farquad_castle = "Lord Farquard", "Gingerbread Man", "Guard"
print(farquad_castle)

another_tuple = ['Shrek', "Fiona", "Donkey"],
print(another_tuple)

name = "Big Bad Wolf", #<-- watch out for sneaky commas
print(name)
print(name[0])

# nested tuples
nested_tuple = ("Lord Farquad", "Magic Mirror", ("Gingerbread Man", "Three Little Pigs"))
print(nested_tuple)

# nested_list in a tuple
nested_list = ("Lord Farquad", "Magic Mirror", ["Gingerbread Man", "Three Little Pigs"])
print(nested_list[0])
print(nested_list[2])
nested_list[2].append("Three Blind Mice")
print(nested_list)
# nested_list[0] = "Fairy Godmother" #Type Error

# slicing a tuple
swamp = ("Shrek", "Fiona", "Donkey", "Dragon", "King", "Queen") 
print(swamp[1:4:2])
# swamp[2] = "Gingerbread Man"

# indexing into a list in a tuple
nested_list = ("Lord Farquad", "Magic Mirror", ["Gingerbread Man", "Three Little Pigs"])
# print(nested_list[2][1])

# Workaround for modifying a tuple
# sorting a tuple
# tuple() and list()
swamp = ("Shrek", "Fiona")
print(swamp)
temp_swamp = list(swamp)
temp_swamp.append("Donkey")
swamp = tuple(temp_swamp)
print(swamp)

num_tup = (5, 1, 7, 2, 5, 9, 10, 8)
sorted_nums = sorted(num_tup)
print(sorted_nums)
sorted_tup = tuple(sorted_nums)
print(sorted_tup)
# sorted() -> copies and sorts an iterable
# .sort() which sorts a list in place
# num_tup.sort()

# Unpacking Tuples
my_tuple = ("Fantasy", "Mystery", "Adventure")
genre1, genre2, genre3 = my_tuple
print(genre1, genre2, genre3)

swamp_residents = {
    "Shrek": "123 swamp rd",
    "Donkey": "124 swamp rd",
    "Gingerbread Man": "125 Swamp Rd"
}
print(swamp_residents.items())

addresses = [('Shrek', '123 swamp rd'), ('Donkey', '124 swamp rd'), ('Gingerbread Man', '125 Swamp Rd')]
for name, address in addresses:
    print(f"{name} lives at {address}")

for name, address in swamp_residents.items():
    print(f"{name} lives at {address}")

# unpacking multiple parts
parts = ("Prologue", "Adventure", "Climax", "Epilogue", "Credits")
# *is going to take as many pices of the tuple as it needs to
# so the rest of our variables, positionally, line up with items in the tuple
*beginning, middle, end = parts
print(beginning)
print(middle)
print(end)
print("============ LOOPING ==============")
# looping through tuples
# looks the same as looping through a list, only we cant change aynthing （；´д｀）ゞ(っ °Д °;)っ
print("============ FOR LOOP ==============")
swamp_residents = ("Shrek", "Fiona", "Donkey", "King", "Queen")
for resident in swamp_residents:
    print(resident)


print("============ WHILE LOOP ==============")
# while loop with indexes
#                    0          1       2         3       4
swamp_residents = ("Shrek", "Donkey", "Fiona", "Queen", "King" )
index = 0
while index < len(swamp_residents):
    print(f"{swamp_residents[index]} is resident number {index + 1}")
    index += 1

print("============ LOOPING WITH ENUMERATE ==============")
swamp_residents = ("Shrek", "Donkey", "Fiona", "Queen", "King" )
for index, resident in enumerate(swamp_residents):
    print(f"{resident} is resident number {index + 1}")

print("============ DOUBLE LOOPING A TUPLE ==============")
swampy_goodness = (("Shrek", "Fiona"), ("Donkey", "Dragon"))
for pair in swampy_goodness:
    for person in pair:
        print(person)

print("============ UNPACKING TUPLES IN A TUPLE ==============")
for person1, person2 in swampy_goodness:
    print(f"{person1} loves {person2}")

# Concatenating Tuples
heroes = ("Shrek", "Donkey", "Fiona")
villains = ("Lord Farquad", "Fairy Godmother", "Prince Charming")
characters = heroes + villains
print(characters)

bad_guy = ("Guard",)
henchmen = bad_guy*3
print(henchmen)

# .index() .count()
print(henchmen.count("Guard"))
print(characters.index("Donkey"))












    
    

