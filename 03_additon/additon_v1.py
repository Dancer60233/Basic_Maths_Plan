#27/5/22 - Kate Barber
#Basic Maths Program
#Addition Function V1
#Aim - Create a basic random generator function to understand how it works
#Reflection - Code works in a basic way and I feel I understand the random more 

import random as r

def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num


for item in range (10):
 min_num = 1
 max_num = 10
 rand_num = random_generator(min_num, max_num)
 print(rand_num)