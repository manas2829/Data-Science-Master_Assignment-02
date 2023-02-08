#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Program accept percentage from the user and display the grade according to the          following createria:

# |MARKS|     |GRADE|
# |-----|     |-----|
# | >90 |         | A   |
# | >80 and <=90| | B   |
# | >=60 and <=80|| c   |
# | below 60   |  | D   |

# In[1]:


per_num=int(input("Enter the percetage number: "))
if per_num >90:
    print("Grade A")
elif per_num >80 and per_num <=90:
    print("Grade B")
elif per_num >=60 and per_num <=80:
    print("Grade C")
else:
    print("Grade D")


# ## 2. Write a Progarm to accept the cost price of a bike  and display the road tax to be paid according to the following Creteria.

# |TAX|     |COST PRICE (in Rupess)|
# |---|     |----------------------|
# |15%|     | >100000              |
# |10%|     | >50000 and <=100000  |
# |5% |     | <=50000              |

# In[2]:


Bike_Price = int(input("Enter the Price of the Bike: "))
if Bike_Price > 100000:
    print("Road Tax to be paid {}".format(Bike_price * 0.15))
elif Bike_Price >50000 and Bike_Price <= 100000:
    print("Road Tax to be paid {}".format(Bike_Price * 0.10))
else:
    print("Road Tax to be paid {}".format(Bike_Price * 0.05))


# ## 3. Accept any City From User and display mouments of the City.

# |CITY|  |MONUMENT|
# |----|  |--------|
# |Delhi| |Red Fort|
# |Agra|  |Taj Mahal|
# |Jaipur||Jal Mahal|
# |Mumbai||Gate way of India|
# |Varoda||Statue of Unity|

# In[3]:


city = input("Enter a city Name: ")
Monument={'Delhi':'Redfort',
               'Agra':'TajMahal',
               'Jaipur':'Jal Mahal',
               'Mumbai':'Gate way of India',
               'Varoda':'Statue of Unity',}
if city in Monument:
    print("The monument of {} is {}".format(city,Monument[city]))
else:
    print("Sorry, The Monument of {} is not in our database".format(city))


# ## 4. Check how many times a given number can be divided by 3 before it is less than or                   equal to 10.

# In[4]:


number = int(input("Enter a number: "))
count = 0

while number > 10:
    #if number % 3==0:
        number = number/3
        count = count + 1

print("The number can be divided by 3", [count], "times before it is less than or equal to 10.")


# ## 7. Reverse a while loop to display number from 10 to 1

# In[5]:


number = 10

while number >= 1:
    print(number)
    number = number - 1


# ## 8. Reverse a while loop to display number from 10 to 1

# In[6]:


num=10
while num != 0:
    print(num)
    num=num-1
        
    


# ## 6. Use nested While loop to print 3 different Pattern.

# In[7]:


# Pattern-1
Size= int(input("Enter the row size: "))
i = 1
while i <= Size:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1
    


# In[8]:


# Pattern-2
i = int(input("Enter the number of row: "))
while i >=1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i -= 1


# In[9]:


# Pattern-3
size= int(input("Enter the number of row/Column: "))
i=1
while i <= size:
    j=1
    while j <= size-i:
        print(" ",end="")
        j+=1
    K=1
    while K <= 2*i-1:
        print("*",end="")
        K+=1
    print("")
    i+=1
    
    


# ## 5. Why and When to used While loop in Python give a detail description with Example.
# 
# ### Ans.
#          The while loop in Python is used when you want to repeatedly execute a block of code as long as a certain 
#          condition is met. It's called a loop because the code inside it repeatedly "loops" through the statements 
#          until the condition is no longer satisfied.
#          
#          syntax of the while loop in Python:
#                     while condition:
#                             code to be executed as long as the condition is True.
#           
#           The condition can be any expression that returns a Boolean value (True or False). If the condition is True, 
#           the code inside the loop is executed. Then, the condition is evaluated again, and if it's still True, 
#           the code inside the loop is executed again. This continues until the condition becomes False, at which 
#           point the loop terminates and control is transferred to the first statement after the loop.

# In[10]:


# one Example of while loop
## Calculate the first positive positve integers using while loop.
n= int(input("Enter the number: "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum of first",n,"The positive integers is ",sum)

