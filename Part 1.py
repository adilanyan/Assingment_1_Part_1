#!/usr/bin/env python
# coding: utf-8

# In[1]:


def list_divide(numbers,divide = 2):
 x = 0
 for i in numbers:
  if i%divide == 0:
   x += 1
  else:
   continue
 return x

print(list_divide([1,2,3,4,5]))
print(list_divide([2,4,6,8,10]))

