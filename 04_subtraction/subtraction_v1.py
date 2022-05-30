#30/5/22 - Kate Barber
#Basic Maths Program
#Subtraction Function V1
#Aim - Use the code from my addition function and change it to subtraction
#Reflection - 

import random as r

def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num



def subtraction(want_neg):
 answer = 0
   while answer == 0: 
    num_1 = random_generator(min_num, max_num)
    num_2 = random_generator(min_num, max_num)
    answer = num_1 + num_2
   while answer == 0 or answer < 0: 
    num_1 = random_generator(min_num, max_num)
    num_2 = random_generator(min_num, max_num)
    answer = num_1 + num_2


 user_answer = "False"
 while user_answer == "False":
  try:
   user_answer = int(input("{} - {}? ".format(num_1, num_2)))
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

want_neg_int = input("Do you want integers ")
min_num = 1
max_num = 10
answer_check = subtraction(want_neg_int)
score_list.append(answer_check)

print(score_list)