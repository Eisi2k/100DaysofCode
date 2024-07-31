
#Lists
#fruits = [item1, item2]


states_of_germany = ["Bayer", "Brandenburg", "Sachsen", "Berlin"]
print(states_of_germany)

print( states_of_germany[1])
print(states_of_germany[-1])

states_of_germany[3] ="Shitehole"
print(states_of_germany)

states_of_germany.append("Mallorca")
print(states_of_germany)
states_of_germany.extend("Menorca")
print(states_of_germany)

num_of_states = len(states_of_germany)
print(states_of_germany[num_of_states-1])