#27/5/22 - Kate Barber
#Basic Maths Program
#Addition Function V3
#Aim - Add my code from the previous version into a function
#Reflection - 

import random as r

def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num

def addition():
  print()
 


for item in range (10):
 min_num = 1
 max_num = 10
 num_1 = random_generator(min_num, max_num)
 num_2 = random_generator(min_num, max_num)
 question = "{} + {}".format(num_1, num_2)
 answer = num_1 + num_2
 print(question)
 print(answer)