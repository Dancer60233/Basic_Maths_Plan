#31/5/22 - Kate Barber
#Basic Maths Program
#Multiplication Function V1
#Aim - basic multiplication function and attempt to get the negative numbers to work
#Reflection - Didn't include the yes 
import random as r

def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num



def multiplication():
  num_1 = random_generator(min_num, max_num)
  num_2 = random_generator(min_num, max_num)
  answer = num_1 * num_2
    
  


  user_answer = "False"
  while user_answer == "False":
   try:
     user_answer = int(input("{} x {}? ".format(num_1, num_2)))
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
for item in range(5):
 min_num = 1
 max_num = 10
 answer_check = multiplication() 
 answer_list.append(answer_check)

print(score_list)