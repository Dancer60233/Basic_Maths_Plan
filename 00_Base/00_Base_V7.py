#Basic Maths Game Base V6
#Aim - To add my basic multiplication component and division component 
#Reflection - Code works well need to add all function next


#import library************************************************
import random as r

#Functions

def int_checker(question): 
  valid = False
  while not valid:

   #ask user for number and check it is valid
   try:
    response = int(input(question))
    valid = True
    
   #If input isn't an integer has a consistent error message 
   except:
    print("Invalid integer! Enter a whole number")

  return response





def string_check(choice, options):

 for var_list in options:
   #if snack is in one of the lists, return the full name
      if choice in var_list:
  #Get full name of snack and put it in titles case so it looks nice when outputted
       return var_list[0].title()
       is_valid = "yes"
       break

      else:
        is_valid = "no"

 if is_valid == "yes":
    return chosen

 else:
    return "invalid choice"


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
  


def subtraction():
  answer = 0
  if want_neg == "Yes":
    while answer == 0:
     num_1 = random_generator(min_num, max_num)
     num_2 = random_generator(min_num, max_num)
     answer = num_1 - num_2
  if want_neg == "No":
    while answer == 0 or answer < 0 :
     num_1 = random_generator(min_num, max_num)
     num_2 = random_generator(min_num, max_num)
     answer = num_1 - num_2
  


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
  

def division():
  answer = 0
  num_1 = 1
  num_2 = 8
  if want_neg == "Yes":
    while answer == 0 or answer == 1:
     num_1 = random_generator(min_num, max_num)
     num_2 = random_generator(min_num, max_num)
     if num_1%num_2 == 0:
      answer = num_1 / num_2
     else:
       answer = 0
  if want_neg == "No":
    while answer == 0 or answer < 0 or answer == 1: 
     num_1 = random_generator(min_num, max_num)
     num_2 = random_generator(min_num, max_num)
     if num_1%num_2 == 0:
      answer = num_1 / num_2
     else:
       answer = 0
       
  


  user_answer = "False"
  while user_answer == "False":
   try:
     user_answer = int(input("{} / {}? ".format(num_1, num_2)))
   except:
      print("This is not a number! ")
   
  if user_answer == answer:
    print("correct")
    answer = "correct"
  else:
   print("incorrect")
   answer = "incorrect"
  return answer
  

  



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
  






def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num



def space(num_spaces):
 for item in range (0, num_spaces):
   print()





#Main Routine


#Lists
  

answer_list = [ ]


yes_no = [
  ["yes", "y"],
  ["no", "n"],
]
valid_operands = ["+","-","*", "/", "all"]

#Questions 
low_question = "Please enter a low number: "
high_question = "Please enter a high number: "
no_q_question = "How many questions: "



if __name__ == "__main__":




  print("Welcome to the Basic Maths Game!!!")

  #Ask user for operator
  space(1)
  operand= "invalid choice"
  while operand == "invalid choice":
   operand = input("What format do you want? (+,-,/,* or all) ").lower()
   operand = string_check(operand, valid_operands)
   if operand == "invalid choice":
     print("Please enter a valid operand")

  #Ask user if they want negative intergers
  space(1)
  want_neg = "invalid choice"
  while want_neg == "invalid choice":
   want_neg = input("Do you want negative integers: ").lower()
   want_neg = string_check(want_neg, yes_no)
   if want_neg == "invalid choice":
     print("Please enter a valid choice (yes/no)")

  #Ask user for low number
  space(1)
  min_num = int_checker(low_question)

  #Ask user for high number
  space(1)
  max_num = int_checker(high_question)
  
  #Ask how many questions they want
  #Temporary for testing 
  space(1)
  num_questions = int_checker(no_q_question)


  space(2)
  #Loop for number of questions
  for questions in range(0, num_questions):


     if operand == "+":
        answer_check = addition()
        answer_list.append(answer_check)



     elif operand == "-":
         answer_check = subtraction() 
         answer_list.append(answer_check)
      
 
     elif operand == "/":
        answer_check = division()
        answer_list.append(answer_check)
      
      
     elif operand == "*":
        answer_check = multiplication() 
        answer_list.append(answer_check)


      #When user enters all
     else:
            random_num = random_generator(min_num, max_num)
            print(random_num)
            print("go to random generator, send min_num and max_num (1 and 5)")
            print("then randomly go to each of the operand functions")

print(answer_list)
  
