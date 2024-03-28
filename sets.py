# SETS
# sets are unordered
# they have no duplicate elements
# you cannot index into a set

# creating a set
# {} <-- without key:value pairs
# set() 

#  [] <-- list
#  {key:value} <-- dictionary
#  {} <-- set
#  () <-- tuple
# declaring an empty set
my_set = set()
# while we use {}, if we initialize a variable with {} it automatically declares a dictionary

# declaring a set with stuff inside
party_guests = {"Alice", "Bob", "Charlie"}
guest_list = set(["Alice", "Bob", "Charlie"])
print(party_guests)
print(guest_list)

#converting other types into sets
people = ["Gertrude", "Obi Wan", "Link", "Link", "Gertrude", "Todd", "Jeff", "Todd"]
# covnerting a list into a set
people_set = set(people)
print(people_set)
people_again = list(people_set)
print(people_again)

# convert tuples
tuple_guests = ("Sebulba", "Lando", "Boba Fett", "Sebulba", "Lando")
set_guests = set(tuple_guests)
print(set_guests)

# converting a dictionary's values
card_dict = {"card1": "Charizard", "card2": "Heracross", "card3": "Espeon", "card4": "Espeon"}
print(card_dict.values())
card_set = set(card_dict.values())
print(card_set)

# Looping through sets
my_set = {"Alice", "Bob", "Charlie"}
for guest in my_set:
    print(f"Welcome {guest} to the party!")

#membership check in a set
guests = {"Gertrude", "Todd", "Jeff"}
if "Todd" in guests:
    print("Todd is enjoying the party")
else:
    print("Todd is being played in Valorant")

# set methods - adding, removing, similarities, differences, combining
guests = {"Alice", "Bob", "Charlie"}
print(guests)
guests.add("Diana")
print(guests)

# updating a set
# combine our current set with another converted iterable or set
guests = {"Alice", "Bob", "Charlie"}
more_guests = ["Shrek", "Fiona", "Donkey", "Puss in Boots"]
guests.update(more_guests)
print(guests)

even_more_guests = ("Gingerbread Man", "Lord Farquad")
guests.update(even_more_guests)
print(guests)

# because sets have unique elements, if we try to add a duplicate element
# either through add or update, those duplicates will be removed
# attempting to add a duplicate element
guests.add("Bob")
print(guests)

# updating with a list of duplicates
bobs = ["Bob", "Bob", "Bob", "Bob","Bob", "Bob"]
guests.update(bobs)
print(guests)

# Removing some rambunctious party guests
# set.remove(thing we are removing) <-- will raise an error if the value does not exist
# set.discard(thing we are removing) <-- will not raise an error
guests = {'Donkey', 'Lord Farquad', 'Alice', 'Shrek', 'Fiona', 'Puss in Boots', 'Charlie', 'Bob', 'Gingerbread Man'}
# removing Lord Farquad
guests.remove("Lord Farquad")
print(guests)
# trying to remove a value that does not exist in the set
# guests.remove('The Big Bad Wolf') #<-- KeyError

# guests = []
# guests.remove("The Big Bad Wolf") #<-- ValueError

# removing with set.discard
guests = {'Donkey', 'Lord Farquad', 'Alice', 'Shrek', 'Fiona', 'Puss in Boots', 'Charlie', 'Bob', 'Gingerbread Man'}
guests.discard("Gingerbread Man")
print(guests)
# discarding a guest that doesnt exist in the set
guests.discard("The Big Bad Wolf") #<-- no error when trying to discard element that doesnt exist
print(guests)

# set.pop() randomly remove something from the set
guests = {'Donkey', 'Lord Farquad', 'Alice', 'Shrek', 'Fiona', 'Puss in Boots', 'Charlie', 'Bob', 'Gingerbread Man'}
random_guest = guests.pop()
print(f"Oh no! The party is over capacity. {random_guest} has been ejected! ")

# set.clear()
# remove everythign from inside the set and leave us with set() <-- empty set
guests.clear()
print(guests)

# adding back to a cleared set
guests.add("Shrek")
print(guests)

# adding to an empty set that we declared as empty

swamp = set()
print(swamp)
# swamp.add("Shrek")
# print(swamp)
swamp.update(['Shrek', "Fiona", "Donkey"])
print(swamp)

# set.union()
# combine two sets into one harmonious set
# remove any duplicates from either set
set1 = {"Shrek", "Fiona", "Donkey"}
set2 = {"Gingerbread Man", "Puss in Boots", "Cypher", "Donkey"}
grand_gathering = set1.union(set2) #<-- order doesnt matter == set2.union(set1)
print(grand_gathering)
# print(set1.union(set2))

# similar functionality with lists
# concatenation
# list1 = ["Shrek", "Fiona", "Donkey"]
# new_string = " loves ".join(list1)
# print(new_string)
# list2 = ["Gingerbread Man", "Puss in Boots", "Cypher", "Donkey"]
# grand_gathering = list1 + list2
# print(grand_gathering)
# list3 = list1.union(list2) <-- AttributeError

# set.intersection(set2) <-- the similarities between two sets
set1 = {"Shrek", "Fiona", "Donkey", "Puss in Boots"}
set2 = {"Gingerbread Man", "Puss in Boots", "Cypher", "Donkey"}
# print(set1.intersection(set2))
samesies = set1.intersection(set2) # order doesnt matter == set2.intersection(set1)
print(samesies)

# set1.difference(set2) 
# items in set1 that are not in set2
# set2.difference(set1)
# items in set2 that are not in set 1
# ORDER MATTERS
set1 = {"Shrek", "Fiona", "Donkey", "Puss in Boots"}
set2 = {"Gingerbread Man", "Puss in Boots", "Cypher", "Donkey"}
swamp_residents = set1.difference(set2)
print(swamp_residents)
non_swamp_residents = set2.difference(set1)
print(non_swamp_residents)

# set.symmetric(set2)
# returns a new set with the differences from both sets
#the order doesnt matter
set1 = {"Shrek", "Fiona", "Donkey", "Puss in Boots"}
set2 = {"Gingerbread Man", "Puss in Boots", "Cypher", "Donkey"}
symmetry = set1.symmetric_difference(set2) # == set2.symmetric_difference(set2)
print(symmetry)


# enumerate a set
# similary to .items() in a dictionary
# position/value
set1 = {"Shrek", "Fiona", "Donkey", "Puss in Boots"}
print(enumerate(set1))
list1 = ["Shrek", "Fiona", "Donkey", "Puss in Boots"]
print(enumerate(list1))
for i, name in enumerate(list1):
    print(f"{name} is at position {i}")
for i in range(len(list1)):
    print(f"{list1[i]} is at position {i}")
# enumerate on a set
    
my_dict = {"name": "Mega Man",
           "address": "Dr Lights Lab",
           "occupation": "cool fighting robot"}
for item in my_dict.items():
    print(item)

for key in enumerate(my_dict):
    print(key)

for key in my_dict.keys():
    print(key)
print(my_dict.keys())

# enumerating with set
set1 = {"Shrek", "Fiona", "Donkey", "Puss in Boots"}
for i, guest in enumerate(set1):
    print(f"Guest {i} is {guest}")

# sorting a set
# sorted()
set1 = {"Shrek", "Fiona", "Donkey", "Puss in Boots"}
sorted_set = sorted(set1)
print(sorted_set)
for i, guest in enumerate(sorted_set):
    print(f"Guest # {i + 1} is {guest}")

# set comprehension
no_dups = set()
numbers = [1, 2, 6, 51, 12]

for num in range(10):
    no_dups.add(num)
print(no_dups)
# set comprehension
# thing that is being added to the list - for iterator variable -  in  - thing we're iterating through
no_more_dups = {num for num in numbers}
print(no_more_dups)
no_more_dups = set(no_more_dups)
print(no_more_dups)


square_set = {num**2 for num in numbers}
print(square_set)

even_square = {num**2 for num in numbers if num % 2 == 0}
print(even_square)



























