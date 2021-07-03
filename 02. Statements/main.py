# Single Line Statements
import os
print('Debug Mode is ON') if os.getenv('DEBUG_MODE') == 'True' else print ('Debug Mode is OFF')

# Multi Line Statements
x = 1
if x == 1:
  print ('X is 1')
elif x == '1':
  print ('X is 1, but type of X is String')
else:
  print ('X is not 1')
  
# Multi comparision statements
i = 10
j = '10'
if i == 10 and j == 10:
  print ('I and J are numbers. And Value is 10')
elif i == 10 or j == '10':
  print ('I is a number and J is string. Both having same value = 10')
elif i == j:
  print ('I and J both are of same type and having same values')  
elif type(i) == type(j):
  print ('I and J both are of same type')
else:
  print ('No statement matched')
  