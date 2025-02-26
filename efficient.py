names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Rewrite the for loop to use enumerate
indexed_names = []

for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_lc = [(i, name) for i, name in enumerate(names)]
print(indexed_names_lc)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

import numpy as np
nums = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Print second row of nums
print(nums[1])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# create a list of Arrival Times
arrival_times = [*range(10, 60, 10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i], time) for i, time in enumerate(new_times)]

print(guest_arrivals)

def welcome_guest(guest_and_time):
    guest, arrival_time = guest_and_time
    return "Welcome to Festivus {}... You're {} min late.".format(guest, arrival_time)

# Map the welcome_guest function to each (guest, time) pair
welcome_map = map(welcome_guest, guest_arrivals)

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]

# Use %timeit to see which one is faster
import timeit
print(timeit.timeit('[*range(51)]', number=10000))
print(timeit.timeit('[num for num in range(51)]', number=10000))

import line_profiler

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

# use %lprun to profile the convert_units() function acting on your superheroes data. Remember to use the special syntax for working with %lprun (you'll have to provide a -f flag specifying the function you'd like to profile).
heroes = ['Batman', 'Superman', 'Wonder Woman']
hts = [188, 191, 183]
wts = [95, 101, 74]
lstat = line_profiler.LineProfiler(convert_units)
lstat.run('convert_units(heroes, hts, wts)')
lstat.print_stats()

def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

lstat = line_profiler.LineProfiler(convert_units_broadcast)
lstat.run('convert_units_broadcast(heroes, hts, wts)')
lstat.print_stats()

import memory_profiler
def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis

mprun = memory_profiler.memory_usage()
calc_bmi_lists(range(1000), hts, wts)
mprun()

heroes = ['Lightwalker', 'Starboy', 'Jupiter']
publishers = ['George Lucas', 'George Lucas', 'George Lucas']
def get_publisher_heroes(heroes, publishers, desired_publisher):
    desired_heroes = []

    for i, publisher in enumerate(publishers):
        if publisher == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes

def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)
    
    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

# benchmark the two functions
print(timeit.timeit('get_publisher_heroes(heroes, publishers, "George Lucas")', globals=globals(), number=10000))
print(timeit.timeit('get_publisher_heroes_np(heroes, publishers, "George Lucas")', globals=globals(), number=10000))

# memory usage
mprun = memory_profiler.memory_usage()
get_publisher_heroes(heroes, publishers, 'George Lucas')
mprun()

mprun = memory_profiler.memory_usage()
get_publisher_heroes_np(heroes, publishers, 'George Lucas')
mprun()

names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl']
primary_types = ['Grass', 'Psychic', 'Dark', 'Bug', 'Rock']
secondary_types = ['Ice', np.nan, np.nan, np.nan, 'Flying']
# Combine names and primary_types
names_type1 =[*zip(names, primary_types)]

# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(names, 2)

print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]

print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(names, 4)]

# Convert both lists to sets
# ash_set = set(ash_pokedex)
# misty_set = set(misty_pokedex)

# # Find the Pokémon that exist in both sets
# both = ash_set.intersection(misty_set)
# print(both)

# # Find the Pokémon that Ash has and Misty does not have
# ash_only = ash_set.difference(misty_set)
# print(ash_only)

# # Find the Pokémon that are in only one set (not both)
# unique_to_set = ash_set.symmetric_difference(misty_set)


# # Convert Brock's Pokédex to a set
# brock_pokedex_set = set(brock_pokedex)
# print(brock_pokedex_set)

# # Check if Psyduck is in Ash's list and Brock's set
# print('Psyduck' in ash_pokedex)
# print('Psyduck' in brock_pokedex_set)

# # Check if Machop is in Ash's list and Brock's set
# print('Machop' in ash_pokedex)
# print('Machop' in brock_pokedex_set)

# def find_unique_items(data):
#     uniques = []

#     for item in data:
#         if item not in uniques:
#             uniques.append(item)

#     return uniques
# # Use the provided function to collect unique Pokémon names
# uniq_names_func = find_unique_items(names)
# print(len(uniq_names_func))

# # Convert the names list to a set to collect unique Pokémon names
# uniq_names_set = set(names)
# print(len(uniq_names_set))

# # Check that both unique collections are equivalent
# print(sorted(uniq_names_func) == sorted(uniq_names_set))

# # Use the best approach to collect unique primary types and generations
# uniq_types = set(primary_types)
# uniq_gens = set(generations)
# print(uniq_types, uniq_gens, sep='\n')

# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, generations) if gen in [1, 2]]

# Create a map object that stores the name lengths
name_lengths_map = map(len, names)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

# Create a total stats array
total_stats_np=np.array(axis=np.sum(stats_np, axis=1))

# Create an average stats array
avg_stats_np = np.mean(stats_np, axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

# Import Counter
from collections import Counter

# Collect the count of each generation
gen_counts = Counter(generation)

# Improve for loop by moving one calculation above the loop
total_count = len(poke_names)