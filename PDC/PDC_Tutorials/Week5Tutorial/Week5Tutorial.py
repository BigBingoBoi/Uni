# -*- coding: utf-8 -*-
"""
Programming for Data Science
Week 5 Tutorial (IO module)
@author u3141210 (Aleksandar Draskovic)
"""
import io_data_module as iodata
import tkinter

# Question 1
myList = list(range(100))

# Question 2 
myTuple = tuple(range(100))

# Question 3
input_list = ['2.1', '3.5', '4.8', '1.1', '2.0']
output_list = [float(number) for number in input_list]    

# Question 4
myList4 = [0, 2, 1, 3, 1, 2, 0, 1]
sum = sum(myList4)

for x in range(len(myList4)):
    myList4[x] = myList4[x] / sum

# Question 5
my_list = ['red', 0, 2, 1, 1, 2, 0, 1, 'blue']
my_list.remove(my_list[0])
my_list.remove(my_list[-1])

# Question 6
myList6 = [0, 1, 0, 2, 0, 1]
for l in range(len(myList6)):
    if myList6[l] == 0:
        myList6[l] = 10

# Question 7
list1 = [2, 3, 1]
list2 = [4, 5, 2]

list3 = []
list3.extend(list1)
list3.extend(list2)

list4 = []
list4.append(list1)
list4.append(list2)

list5 = []
list5.append(tuple(list1))
list5.append(tuple(list2))

# Question 8
datalist = iodata.read_multi_dim_data('iris.data')
print(datalist)

# Question 9
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=720, width=850)

s = 90 # scale
r = 4 # radius

# draw ovals
for z in datalist:
    x = z[0] * s
    y = z[1] * s
    C.create_oval(x-4, y-4, x+4, y+4, outline = "red", fill = "red")


# centre ovals
centre_1 = (5.1, 3.0, 1.1, 0.5)
centre_2 = (4.4, 3.2, 2.8, 0.2)
centre_3 = (5.7, 3.9, 3.9, 0.8)
a = centre_1[0] * s
b = centre_1[1] * s
c = centre_2[0] * s
d = centre_2[1] * s
e = centre_3[0] * s
f = centre_3[1] * s
C.create_oval(a-4, b-4, a+4, b+4, outline = "black", fill = "black")
C.create_oval(c-4, d-4, c+4, d+4, outline = "black", fill = "black")
C.create_oval(e-4, f-4, e+4, f+4, outline = "black", fill = "black") 

C.pack()
top.mainloop()
   
