# -*- coding: utf-8 -*-
"""
Programming for Data Science
Week 3 Tutorial
@author u3141210 (Aleksandar Draskovic)
"""
# Example 1
# define function
def welcome():
    print('Welcome to Python functions')
# end of function
    
# call function
welcome()


# Example 2
# define function
def square(x):
    print('Square of ' +  str(x) + ' is ' + str(x*x))
# end of function
    
# call function
square(5)


# Example 3
# define function
def square(x):
    return x * x
# end of function

# call function
s = square(5)
print('Square of 5 is ' + str(s))


# Example 4
# distance d = square root of (x2-x1) * (x2-x1) + (y2-y1) * (y2-y1)
# define function
def distance(x1, y1, x2, y2):
     d = ((x2-x1)*(x2-x1) + (y2-y1) * (y2-y1))**0.5
     return d
# end function
     
# call function
x1 = 3
y1 = 0
x2 = 0
y2 = 4
dist = distance(x1, y1, x2, y2)
print('Distance between (3, 0) and (0, 4) is ' + str(dist))


# Example 5
# distance d = square root of (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
# Two points are two tuples p1 = (x1, y1) and p2 = (x2, y2)
# define function 
def distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d += (p2[i] - p1[i]) * (p2[i] - p1[i]) 
    d = d**0.5
    return d
#end function
#call function 
#Two points are two tuples (x, y)
p1 = (3, 0)
p2 = (0, 4)
dist = distance(p1, p2)
print('Distance between p1 and p2 is ' + str(dist))
