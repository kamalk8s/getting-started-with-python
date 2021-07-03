# Defining the variables
my_int = 100  # Integer
my_str = 'This is a string'  # String
# List can contain any type of values
my_list = [1, 2, 3, 'Four', 'Five', 'Six', True, False, 2, 4, 'Four']  # List
# List inside a list
my_nested_list = [1, 2, 3, ['Hey, I\'m inside nested list', 'I\'m also in Nested List'], 4, 'Five']  # Nested List
# Tuple is also a list but, it's immutable list. This means you cannot change the values which are already defined in Tuple.
my_tuple = (1, 2, 3, 4, 'Five', 'Six')  # Tuple
# Range is a function which will produce the List in a series
my_range = range(1,10) # will produce list from 1 to 9
# Dictionary is a list of key:value pair
my_dict = {'key1':'val1', 'key2':'val2', 'key3':[1,2,3,4,5], 'key4': True}
# Bool
my_bool = True
# Set
my_set = set(my_list)  # This will return my_list but unique values only.


# Quotation types
quotation1 = 'Hey, I am string inside single quote'
quotation2 = "Hey, I'm string inside double quote"
quotation3 = '''
Hey, I'm in multiline quotes.
And I'm second line
'''

# Using Print function
print('Hello, Python!')

# Fetching values from Int and Str variables
print ('Number is ' + str(my_int))  # You can't concatinate the string with int, so convert the int to str using str() method
print ('String is ' + my_str)  # As it is string, we can directly concatinate

# Getting Values from List
print (my_list[0]) # It will return first Value
print (my_list[1]) # It will return second Value
print (my_list[-1]) # It will return Last Value
print (my_list[-2]) # It will return second last Value
print (my_list[-3]) # It will return third last Value and so on...
print (my_list[0:4]) # It will return first to forth value
print (my_list[3:6]) # It will return third to sixth value
print (my_list[:6]) # It will return all values before 7th value (includes 6th)
print (my_list[2:]) # It will return all values after 1st value (includes 2nd)

# Getting Values from nested List
print (my_nested_list[0])  # It will return 1st item in list
print (my_nested_list[3][0])  # It will return 1st item in nested list

# Using Tuples
print (my_tuple.count('Six')) # This will print how many times 'Six' exists in this Tuple
print (my_tuple.count('Five')) # This will print what's the index of 'Five' in Tuple

# Getting data from dictionary
print (my_dict.get('key2')) # This will return the value of 'key2'. If key name not exists, will return None.
print (my_dict['key2'])  # This will also return the value of 'key2'.  But it will give you error if key not exist.

# Escape Charactors
#  '\' can be used as escape charactor.
print ('Hi I\'m Kamal.')  # Here I'm using escape charactor as python was misunderstanding the ' as end of print statement.