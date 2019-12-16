#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd


# In[2]:


pybank_path = 'C:/Users/bassa/projects/PyBank/Resources/'
pybank_csv_file = 'budget_data.csv'
pybank_csv_filepath = os.path.join( pybank_path, pybank_csv_file)
print(pybank_csv_filepath)


# In[4]:


pybank_df = pd.read_csv(pybank_csv_filepath)

# I need to create a file variable that I will use in each operation


# In[39]:


print("Total Months:" ) 

# The total number of months are all in the left column

# I need to add every row on the left column

# what function allows me to do that? 

# "The shape attribute of pandas.DataFrame stores the number of rows and columns as a tuple (number of rows, number of columns)""

print(pybank_df.shape[0])


# In[21]:


print("Total: ")

print(pybank_df["Profit/Losses"].sum())


# In[ ]:





# In[49]:


print("Average Change: ")

# how the fuck do I find that
# an average change will start finding out how I can find a function that the difference of every profit/loss and create something that goes backwards for the total sum of the profits
#if i subtract the total losses by each month I can use a mean function to find the same answer

average_change = pybank_df["Last_Month_ProfitsLosses"] = pybank_df["Profit/Losses"].shift()
pybank_df["month_over_month_difference"] = pybank_df["Profit/Losses"] - pybank_df["Last_Month_ProfitsLosses"]
pybank_df["month_over_month_difference"].mean()

print("-2315.11764")


# In[42]:


print("Greatest increase in profits: ")

#it should be the max of the month to month difference

max_difference = pybank_df["month_over_month_difference"].max()


print(max_difference)


# In[43]:


print("Greatest decrease in profits: ")

min_difference = pybank_df["month_over_month_difference"].min()


print(min_difference)


# In[ ]:




