#30/5/22 - Kate Barber
#Basic Maths Program
#Addition Function V4
#Aim - Create error prevention in my code for not entering intgers and keeps a record of if answer was correct
#Reflection - Code works and has good error prevention and stores if answer was correct

import random as r

def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num

def addition():
 num_1 = random_generator(min_num, max_num)
 num_2 = random_generator(min_num, max_num)
 answer = num_1 + num_2

 user_answer = "False"
 while user_answer == "False":
  try:
   user_answer = int(input("{} + {}? ".format(num_1, num_2)))
  except:
    print("This is not a number! ")
   
 if user_answer == answer:
    print("correct")
    answer = "correct"
 else:
   print("incorrect")
   answer = "incorrect"
 return answer
  

score_list = []

for item in range (5):
  min_num = 1
  max_num = 10
  answer_check = addition()
  score_list.append(answer_check)

print(score_list)