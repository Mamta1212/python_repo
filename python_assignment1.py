#!/usr/bin/env python
# coding: utf-8

# python_assignment1

# In[1]:


#1. Write a Python program to print "Hello Python"?
print("Hello Python")


# In[3]:


#2. Write a Python program to do arithmetical operations addition and division.?
a=60      
b=5
c=a+b
d=a/b


# In[5]:


c


# In[7]:


int(d)


# In[15]:


#3. Write a Python program to find the area of a triangle?

side=int(input("enter length of side of tringle"))     #taking input from users
area=side*side
print("area of tringle=",area)


# In[21]:


# 4. Write a Python program to swap two variables?
var1=int(input("Enter variable one: v1="))
var2=int(input("Enter variable two: v2="))
new_var=var1      #taking new Variable to substitute the value of var1
var1=var2         # this exchange or swap the values of var1 and var2
print("var1=",var2)
print("var2=",new_var)


# In[26]:


# 5. Write a Python program to generate a random number?
import random    #importing random function
print("Random number: ",random.randint(1,100))   #print random number between 1 to 100


# In[ ]:




