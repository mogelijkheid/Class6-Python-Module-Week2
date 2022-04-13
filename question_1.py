#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    x=input('Please enter a number')
    numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    try:
        x=int(x)
        for i in range(x):
            a=numbers.pop(0)
            numbers.append(a)
        print(numbers)
        break
    except:
        print('Please enter a number')





# In[ ]:





# In[ ]:





# In[ ]:




