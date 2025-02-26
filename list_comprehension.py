nums = [12, 9, 21, 3, 16]
new_nums = [num+1 for num in nums]
# for num in nums:
#     new_nums.append(num+1)
# print(new_nums)
result = [num for num in range(1,11)]
# print(result)
pairs = []
for num1 in range(0,2):
    for num2 in range(6,8):
        pairs.append((num1,num2))
# print(pairs)
pairs2 = [(num1,num2) for num1 in range(0,2) for num2 in range(6,8)]
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# conditional 
cond = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
# print(cond)
# Dictionary Comprehension
pos_neg = {num: -num for num in range(9)}
# print(pos_neg)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
# new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]
# dict 
new_fellowship = {member: len(member) for member in fellowship}
# Print the new list
# print(new_fellowship)

# Generator Expressions
# x = (num for num in range(10**10000000))
# print (list(x))

# Generator Functions
def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1
result = num_sequence(5)
# print(list(result))

# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# Print the rest of the values
# for value in result:
#     print(value)

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Define the function get_lengths
def get_lengths(input_list):
    """Generator function that yields the length of the strings in input_list."""
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
# for value in get_lengths(lannister):
#     print(value) 
# Extract the created_at column from df: tweet_time
# import pandas as pd
# df = pd.read_csv('tweets.csv')
# tweet_time = df['created_at']

# # Extract the clock time: tweet_clock_time
# tweet_clock_time = [entry[11:19] for entry in tweet_time]

# # Import the pandas package
# # import pandas as pd

# # Initialize reader object: df_reader
# df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# # Print two chunks
# # print(next(df_reader))

# # Initialize reader object: urb_pop_reader
# urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# # Get the first DataFrame chunk: df_urb_pop
# df_urb_pop = next(urb_pop_reader)

# # Check out the head of the DataFrame
# print(df_urb_pop.head())

# # Check out specific country: df_pop_ceb
# df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# # Zip DataFrame columns of interest: pops
# pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])


# # Code from previous exercise
# urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
# df_urb_pop = next(urb_pop_reader)
# df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
# pops = zip(df_pop_ceb['Total Population'], 
#            df_pop_ceb['Urban population (% of total)'])
# pops_list = list(pops)

# # Use list comprehension to create new DataFrame column 'Total Urban Population'
# df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
# # explain above code
# # for tup in pops_list:
# #     df_pop_ceb['Total Urban Population'] = int(tup[0] * tup[1] * 0.01)


# # Plot urban population data
# df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
# # plt.show()

# # Initialize reader object: urb_pop_reader
# urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# # Initialize empty DataFrame: data
# data = pd.DataFrame()

# # Iterate over each DataFrame chunk
# for df_urb_pop in urb_pop_reader:

#     # Check out specific country: df_pop_ceb
#     df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

#     # Zip DataFrame columns of interest: pops
#     pops = zip(df_pop_ceb['Total Population'],
#                 df_pop_ceb['Urban population (% of total)'])

#     # Turn zip object into list: pops_list
#     pops_list = list(pops)

#     # Use list comprehension to create new DataFrame column 'Total Urban Population'
#     df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
#     # Append DataFrame chunk to data: data
#     data = data.append(df_pop_ceb)

