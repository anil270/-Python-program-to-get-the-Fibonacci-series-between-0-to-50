#!/usr/bin/env python
# coding: utf-8

# ## Write a Python program to get the Fibonacci series between 0 to 50 

# In[13]:


x = int(input())
y = int(input())
c = 0
while y<=50:
    if c==34:
        break;
    x=y
    y=c
    c=x+y
    print(c,end=" ")

