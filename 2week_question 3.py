#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tuple1 = (20, 10, 60, 70, 50, 20, 80, 20, 10, 20, 60, 60, 50)
a=dict()
for i in tuple1:
  if i in a.keys():
    a[i]+=1
  else:
    a[i]=1
print(a)


# In[ ]:




