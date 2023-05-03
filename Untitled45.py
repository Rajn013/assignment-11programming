#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python program to find words which are greater than given length k?

# In[5]:


def find_long_words(sting, k):
    words = string.split()
    long_words = [word for word in words if len(word) > k]
    return long_words

#example 
string = "The black box was open"
k = 4
long_words = find_long_words(string, k)
print(long_words)


# 2.Write a Python program for removing i-th character from a string?

# In[7]:


def remove_char(string, i):
    return string[:i] + string[i+1:]
string  = "Rajan"
i = 4
new_string = remove_char(string, i)
print(new_string)


# 3.Write a Python program to split and join a string?

# In[10]:


def split_and_join(string):
    word = string.split()
    new_string = "-".join(word)
    return new_string
string = "Rajan"
new_string = split_and_join(string)
print(new_string)


# 4.Write a Python to check if a given string is binary string or not?

# In[27]:


def is_binary_string(string):
    binary_set = {'0','1'}
    return set(string).issubset(binary_set)

string1 = "1998"
string2 = "rajan"
print(is_binary_string(string1))
print(is_binary_string(string2))


# 5.Write a Python program to find uncommon words from two Strings?

# In[32]:


def uncommon_words(string1, string2):
    set1 = set(string1.split())
    set2 = set(string2.split())
    return list(set1.symmetric_difference(set2))

string1 = "the world is big"
string2 = "the black box"
uncommon = uncommon_words(string1, string2)
print(uncommon)


# 6.Write a Python to find all duplicate characters in string?

# In[36]:


def find_duplicate_char(string):
    duplicates = []
    for char in string:
        if string.count(char) > 1 and char not in duplicates:
            duplicates.append(char)
            return duplicates
        
string = "rajan"
duplicates = find_duplicate_char(string)
print(duplicates)


# 7.Write a Python Program to check if a string contains any special character?

# In[37]:


import  re
def contains_special_char(string):
    pattern = re.compile('[!@#$%^&*()_+=\[{\}];:<>|./?,-]')
    return bool(pattern.search(string))

string1 = "rajan"
string2 = "data10"
print(contains_special_char(string1))
print(contains_special_char(string2))


# In[ ]:




