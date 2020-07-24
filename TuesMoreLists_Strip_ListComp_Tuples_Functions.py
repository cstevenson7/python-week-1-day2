#!/usr/bin/env python
# coding: utf-8

# # Functions, Scoping, Data Collections 1 & List Comprehensions

# ## Tasks Today:
# 
# <i>Monday Additions (or, and ... if statements)</i>
# 
# 1) String Manipulation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) strip() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) title() <br>
# 2) Working With Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) min() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) max() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) sum() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) sort() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Copying a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) 'not in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Checking an Empty List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Removing Instances with a Loop <br>
# 3) List Comprehensions <br>
# 4) Tuples <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) sorted() <br>
# 5) Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) User-Defined vs. Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accepting Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Default Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Making an Argument Optional <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Keyword Arguments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Returning Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) *args <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Docstring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Using a User Function in a Loop <br>
# 6) Scope

# ### Monday Refreshers

# ##### Using 'or' in if statements

# In[ ]:


# covered yesterday
#one or the other have to be true


# ##### Using 'and' in if statements

# In[ ]:


# covered yesterday
#both sides have to be true


# ##### Using both 'or' and 'and' in if statements

# In[ ]:


# covered yesterday


# ### String Manipulation

# ##### .lstrip()

# In[ ]:


# string.lstrip() removing white space but you can remove anything
name = "      h  John Smith"
# if brackest are emty it will look got white space
print(name.lstrip())

name = "    h  John Smith"
# if brackest  need thae right amount of spacese
print(name.lstrip("    h"))

print(name.lstrip(" " "h"))


# ##### .rstrip()

# In[ ]:


# string.rstrip()
name= "bill Ross    Th"
print(name.rstrip("    Th"))

name= "bill Ross    %"
print(name.rstrip("%"))

name= "bill Ross.com/dfasf"
print(name.rstrip("/dfasf"))


# ##### .strip()

# In[ ]:


# string.strip() # left and right
name = "    John Smith    xy"
print(name.strip(" "  " " "xy"))

name = "    John Smith    xy"
print(name.strip(" "  " " "h")) #parrern matching on both sides so space on left,  space on right   and then looking
#for an h


name = "John Smith"
print(name.strip("h"))##why is h in john still here


# ##### .title()

# In[ ]:


# string.title() # under the hood is a regular expression
president= 'barak obama'
print(president.title())

help(str.title)


# ### String Exercise <br>
# <p>Strip all white space and capitalize every name in the list given</p>

# In[ ]:


names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
# HINT: You will need to use a for loop for iteration string.lstrip()
for name in names:     
    print(name.strip().title())
    


# ### Working With Lists

# ##### min()

# In[ ]:


# min(list)
numbers = [4,2,97,54,16]
print (min(numbers))


# ##### max()

# In[ ]:


# max(list)

print(max(numbers))


# ##### sum()

# In[ ]:


# sum(list)
print(sum(numbers))


# ##### sorted()

# In[ ]:


# sorted(list)
numbers = [4,2,97,54,16]
print(numbers)


#SORTED returns a copy of the array in sorted order but does not do it in place
#if you want access you have to pss it to a variablr, stores in a differrent block memory and then sort
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)


# ##### .sort() <br>
# <p>Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list</p>

# In[ ]:


# list.sort()looks at the block of memory where the list is and drops it in the same place
numbers.sort() 

#print (numbers.sort()) - THIS RETURNS NOTHING have to sort then print
print(numbers)

# use sorted when you don't want to alter original list, use .sort() when you want to alter original list


# ##### Copying a List

# In[ ]:


# [:] copies a list, doesn't alter original 
list1 = numbers[:] #allows you to copy the full list this operation is
#the full list is linerally created. Family  with 10 kids in an  apt on a floor, we are copying the family and putting the copy in a different apt
print(list1)
print(numbers)


# ##### 'in' keyword

# In[ ]:


l_teachers = ["Joel", "Derek" , "Commer", "Brian", "Joe"]
if "Derek" in l_teachers:
    print ("Coding Temple instructor")
else:
    print("Not an instructor")


# ##### 'not in' keyword

# In[ ]:


l_teachers = ["Joel", "Derek" , "Commer", "Brian", "Joe"]
if "Derek" in l_teachers:
    print ("Coding Temple instructor")
else:
    print("Not an instructor")
if "Zack"  not in l_teachers:
    print (" Not a Coding Temple instructor")


# ##### Checking an Empty List

# In[ ]:


# if l_1: or if l_1 = []
lst2 = []
if lst2 ==[]:
    print("empty")


# ##### Removing Instances with a Loop

# In[ ]:


# while, remove
#Remove all of the instances of evan
names = ["Commer", "Joel", "Max" , "Evan", "Brian", "Evan"]

while 'Evan' in names:
     names.remove('Evan')

print(names)


# ### List Exercise <br>
# <p>Remove all duplicates<br><b>Extra: Create a program that will remove any duplicates from a given list</b></p>

# In[ ]:


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
non_dup = []

# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier

# i read the question wrong did not have to 

# for name in names:
#     if name not in non_dup:
#         # to get title case
#         non_dup.append(names) 
        
#     names = []
#     names = non_dup[:] 

# print(non_dup)
# print(names)


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
non_dup = []

# #Ony needed to do this
for name in names:
    if name not in non_dup:
        non_dup.append(name)
        
print(non_dup)
print(names)

#this not working
# def create_list(names):
#     new_list =[name for name in names if name not in new_list]
#     return new_list

# print(create_list(names))


# ### List Comprehensions <br>
# <p>Creating a quickly generated list to work with<br>*result*  = [*transform*    *iteration*         *filter*     ]</p>

# ##### In a list comprehension we have a few pieces:
# 1. The first is the counter/ variable - IN this the variable is x
# 2. then we have a transform for the variable
# 3. The finale part of a list comp is called the condition
# 
# ```python
#     [variable, transform, condition]
# ```

# In[ ]:


#The new norm in lists - the actual list gets consrtructed when the for loop runs at runtime the list get consatructed
# number comprehension 

###***ONLY FOR CREATING NEW LISTS
# With a regular for loop
nums = []

for i in range(100):
    nums.append(i)
print(nums)

#list comp - condition is optional
#[variable, transform, condition]
print ("\n")

#like a backwards for loop

# i and i ALWAYS HAVE TO BE THE SAME these variables have to match
#the list is getting created insid 
      #variable   transform
nums_comp = [i for i in range(100)]
print(nums_comp)

# Joel - do the for loop old way first then fo the list cmop. the end of the for
#loop is kins the beginnin


# IN a list comprehension we have a few pieces:
# The first is the counter/ variable - IN this the variable is x
# Then we have a transform for the variable 
# The finale part of a list comp is called the condition
#[variable, transform, condition]




# There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.
# 
# Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.
# 
# Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# In[ ]:


# square number comprehension
#you kind of start at the end of the regular way with the (x**2)
squares = [x**2 for x in range(10)]
print(squares)


squares_reg=[]
for x in range(10):
    squares_reg.append(x**2)
    
print("\n")
print (squares_reg)



# In[ ]:


# string comprehension - get all first letters of the names
names = ['Conner', 'Max', 'Evan', 'Rob']

first_char =[name[0] for name in names]
print(first_char)

first_reg = []
for name in names:
    #get index 0 for each name
    first_reg.append(name[0])
    
print("\n")

print(first_reg)


# In[ ]:


#using a if
c_names = [name for name in names if name[0] =='C']

print(c_names)

#old way
reg_names = []
for name in names:
    if name[0] =='C':
        reg_names.append(name)
        
print("\n")
print(reg_names)


# In[ ]:


#using a list comp to create a grid  - inner how things look  - outer what's inside

# grid = [[x for x in range(5)] for x in range(15)]  #15 rows 5 columns

# grid # can't print a grid

grid = [[x for num in range(5)] for x in range(15)]  # still 15 rows 5 columns bit differernt values in grid

grid # can't print a grid


# ### Tuples <br>
# <p><b>Defined as an immutable list</b></p><br>Seperated by commas using parenthesis

# In[ ]:


# can't change values in a tuple, need to recreate a tuple
#can create tuples two  different ways
tuple1 = 1,2,3

tuple2 = (1,2,3)
# print(type(tuple1))
# print(type(tuple2))

#tuple[0] = 5 #returns an error TypeError: 'type' object does not support item assignment

#can print the index though
print(tuple1[0])


# ##### sorted()

# In[ ]:


t_2 = (20,5,1,3,9,45)
sorted_tup = sorted(t_2)
print(sorted_tup)


# ##### Adding values to a Tuple

# In[ ]:


print(tuple1)

#need to recreate the tuple to change it

# NEED THE COMMA, without the comma it becomes an int
tuple1 = tuple1 + (5,)

print(tuple1)


# ## Functions

# ##### User-Defined vs. Built-In Functions

# In[ ]:


#UDFs

def sayHello():
    return("Hello World")
    
#print(sayHello) # this gives you the memory location of the function
print(sayHello())


# ##### Accepting Parameters

# In[ ]:


# ORDER MATTERS
# a variable can be of any type of object, also you can pass a function

def printFullName(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    
printFullName("Fred", "Flintstone")


# ##### Default Parameters

# In[ ]:


#order matters here as well
#default paramweters hve to be after non-defalut parameters

def printAgentName( first_name, last_name="Bond"):
    print(f"the name is {first_name} {last_name}")
    
printAgentName("James")
#Can overwrite the defaults

printAgentName("Joel", "Carter")


# ##### Making an Argument Optional

# In[ ]:


def printHorseName(first, middle="", last = "Ed"):
    print(f"Hello {first} {middle} {last}")
    
printHorseName("Mr", "lee")
printHorseName("Mr")


# ##### Keyword Arguments

# In[ ]:


# last_name='Max', first_name='Smith' in the function call
#KEYWORD CANNOT go BEFORE Optional
# see above

def printHorseName(, middle="", first, last = "Ed"):
    print(f"Hello {first} {middle} {last}")
    
printHorseName("Mr", "lee")
printHorseName("Mr")


# # Creating a start, stop, step function

# In[ ]:


def my_range (stop, start =0, step = 1):
    for i in range(start, stop, step):
        print (i)
        
my_range(100,50,2)


# ##### Returning Values

# In[ ]:


def addNums(num1, num2):
    return num1 + num2

#To see what data type
print(type(addNums(5,10)))
print(addNums(5,10))


# ##### *args

# In[ ]:


# stansd for arguements takes any number of argument as papameters
#musst be last if multiplse parameters are present Pep8 style guide says *args should go last

def printArgs(num1, *args, **kwargs):
    print(args)
    print(num1)
    print(kwargs)
    
    random_list=[]
    
    for arg in args:
        if type(arg) == str:
            random_list.append(arg)
    print (random_list)
    
printArgs(56,2,3,'Goku', 'vanilla', 26, first_name = "joel", last_name = 'carter')


# ##### Docstring

# In[ ]:


# can call the help function on the UDF and the docstring will be displayed
def printNames(list_1):
    """print Names (list1)
    functions requires a list ato be passed as a parameter
    and will prit the contnets of the list. Expecting a list oo fnames to be padded
    """
    for name in list_1:
        print(name)
        
printNames(['Conner', 'Max', 'Evan', 'Rob'])
print("\n")
help(printNames)


# ##### Using a User Function in a Loop

# In[ ]:


def printInput(answer):
       print(answer)
       
response= input("are you ready to quit? ")

while True:
   ask = input("What to you want to do?")
   printInput(ask)
   response = input('Ready Yet')
   if response.lower() == 'quit':
       break
   
               
   
   


# ## Function Exercise <br>
# <p>Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names</p>

# In[ ]:


first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']
full_name = []
# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']

#WITH ZIP - basically just like a zipper for any iterable
# def combine_name(first_name, last_name):
#     for f_name, l_name in zip(first_name,last_name):
#         #print (f_name)
#         #print(l_name)
#         #full_name.append(f_name[0] + l_name[0]) got first initials with this
#         full_name.append(f_name + " " + l_name)
        
#     return full_name

# print(combine_name(first_name, last_name))

#lists have to be the same size for both these ways to work, if they were not then wrap in a try and except

#Using len of first list
def combine_name(first_name, last_name):
    #go through first_name list till the end
    for name in range(len(first_name)):  
        full_name.append(first_name[name] + " " + last_name[name])
        
    return full_name

print(combine_name(first_name, last_name))


# ## Scope <br>
# <p>Scope refers to the ability to access variables, different types of scope include:<br>a) Global<br>b) Function (local)<br>c) Class (local)</p>

# In[ ]:


#placement of variables declaration matters
# num = 3  #global Varable
# def myFunc():
#     num3 = 6 # local Varaible
  

# print(num)
# print(num3) # this will throw an error  because it is only availabe INSIDE the function

num = 3  #global Varable
def myFunc():
    num3 = 6 # local Varaible
    return num3
  

print(num)
print(myFunc())


# # Exercises

# ## Exercise 1 <br>
# <p>Given a list as a parameter,write a function that returns a list of numbers that are less than ten</b></i></p><br>
# <p> For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]</p>

# In[ ]:


# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

# def createList(list1):
#     new_list = []
#     for num in list1:
#         if num < 10:
#             new_list.append(num)
#     return new_list

# print(createList(l_1))

def createList(list1):
    new_list =[num for num in list1 if num <10]
    return new_list

print(createList(l_1))
            
        


# ## Exercise 2 <br>
# <p>Write a function that takes in two lists and returns the two lists merged together and sorted<br>
# <b><i>Hint: You can use the .sort() method</i></b></p>

# In[143]:


l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def mergeLists(list_1, list_2):
    new_list = list_1 + list_2
    sorted_list = sorted(new_list)
    return sorted_list


def removeMultiples(a_list):    
    #getting error with list comp
    #free variable 'single_list' referenced before assignment in enclosing scope
    #single_list = [item for item in a_list if item not in single_list]
    single_list = []
    for item in a_list:
        if item not in single_list:
            single_list.append(item)
    return single_list
    

print(removeMultiples(mergeLists(l_1,l_2)))


# In[ ]:




