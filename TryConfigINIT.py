import glob
import io
import itertools

s = "Hello the World"
print(s)

# for i in s:
#     print(i)

t = "Hello the World"
# myList = [ i for i in t ]

print([ i for i in "Hello the World" if i.upper() != 'L' ])

