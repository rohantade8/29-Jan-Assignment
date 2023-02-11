#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1.  Explain with an example each when to use a for loop and a while loop.


# A for loop is used when you want to iterate over a sequence (such as a list, tuple, or string) or a range of numbers and you know beforehand how many times you want to repeat the loop. Here is an example that uses a for loop to iterate over a range of numbers and print the square of each number:

# In[5]:


for i in range(1, 6):
    print(i ** 2)


#  A while loop, on the other hand, is used when you don't know beforehand how many times you want to repeat the loop and you want to continue looping as long as a certain condition is met. Here is an example that uses a while loop to print the numbers 1 to 5:

# In[10]:


i = 1
while i <= 5:
    print(i)
    i = i + 1
    


# In[12]:


# Q2. Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.


# In[13]:


# Using for loop
sum_of_numbers = 0
product_of_numbers = 1

for i in range(1, 11):
    sum_of_numbers += i
    product_of_numbers *= i

print("Sum of the first 10 natural numbers using for loop:", sum_of_numbers)
print("Product of the first 10 natural numbers using for loop:", product_of_numbers)


# In[15]:


# Using while loop
i = 1
sum_of_numbers = 0
product_of_numbers = 1

while i <= 10:
    sum_of_numbers += i
    product_of_numbers *= i
    i += 1

print("Sum of the first 10 natural numbers using while loop:", sum_of_numbers)
print("Product of the first 10 natural numbers using while loop:", product_of_numbers)


# In[18]:


# Q3. Create a python program to compute the electricity bill for a household.
# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# You are required to take the units of electricity consumed in a month from the user as input.
# Your program must pass this test case: when the unit of electricity consumed by the user in a month is
# 310, the total electricity bill should be 2250.


# In[20]:


units_of_electricity_consumed = int(input("Enter the units of electricity consumed in a month: "))

if units_of_electricity_consumed  <= 100:
    bill = units_of_electricity_consumed  * 4.5
elif units_of_electricity_consumed  <= 200:
    bill = (100 * 4.5) + ((units_of_electricity_consumed  - 100) * 6)
elif units_of_electricity_consumed  <= 300:
    bill = (100 * 4.5) + (100 * 6) + ((units_of_electricity_consumed  - 200) * 10)
else:
    bill = (100 * 4.5) + (100 * 6) + (100 * 10) + ((units_of_electricity_consumed - 300) * 20)

print("Total electricity bill: Rs.", bill)


# In[21]:


# Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
# that list.


# In[22]:


#using a for loop
numbers = []
for i in range(1,101):
    cube = i**3
    if (cube % 4 == 0) or (cube % 5 == 0):
        numbers.append(cube)
print("The list of numbers whose cube is divisible by 4 or 5:", numbers)


# In[24]:


# using a while loop 
numbers = []
i = 1
while i <= 100:
    cube = i**3
    if (cube % 4 == 0) or (cube % 5 == 0):
        numbers.append(cube)
    i += 1
print("The list of numbers whose cube is divisible by 4 or 5:", numbers)


# In[26]:


# Q5. Write a program to filter count vowels in the below-given string.
# string = "I want to become a data scientist"


# In[27]:


string = "I want to become a data scientist"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in the given string:", count)

