#30/5/22 - Kate Barber
#Basic Maths Program
#Addition Function V3
#Aim - Add my code from the previous version into a basic function
#Reflection - Code works and I now ask te question in the function. next steps is to add more error prevention

import random as r

def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num

def addition():
 num_1 = random_generator(min_num, max_num)
 num_2 = random_generator(min_num, max_num)
 answer = num_1 + num_2


 try:
  user_answer = int(input("{} + {}? ".format(num_1, num_2)))
 except:
        print("This is not a number! ")
   
 if user_answer == answer:
    print("correct")
 else:
   print("incorrect")
  



for item in range (5):
 min_num = 1
 max_num = 10
 addition()