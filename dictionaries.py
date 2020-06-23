#dictionaries allows to store keys 
friend_age = {"Rolf":24,
              "Adam":25,
              "Charlie":30}
print(friend_age["Rolf"])
print("\n")


#change existing key

friend_age["Rolf"] = 25
print(friend_age)

riends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

# You can turn a list of lists or tuples into a dictionary:

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)
