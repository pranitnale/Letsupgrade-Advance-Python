#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from configparser import ConfigParser
import os 

config=ConfigParser()
config.read("P:\Pranit\Courses\Advance Python\Materials\Day 13\exc - Mohit Raj.ini")

path=config.get("Exten","path")
old_ext=config.get("Ext","OE")
new_ext=config.get("Exten","NE")

os.chdir(path)
os.getcwd()

for file in os.listdir():
   if file.endswith(old_ext):
       print(file)
       first_name=file.rsplit(".",1)[0]
       new_name=first_name + "." + new_ext
       print(new_name)
       os.rename(file, new_name)


# In[ ]:


import os
rep=os.walk("D:\\Company")

d1={}
for r,d,f in rep:
    for file in f:
        d1.setdefault(file,[]).append(r)

file_name=input("Enter your File Name :") 
for k,v in d1.items():
    if file_name.lower() in k.lower():
        print(k,":",v)   
        for find_file in v:
            print(find_file)

