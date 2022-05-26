#Basic Maths Game Base V3
#Aim - To add my string checker component and find out if the user wants negatuive numbers
#Reflection - Code works well and I created a space function that works


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
  print("+")



def subtraction():
  print("-")



def division():
  print("/")
  


def multiplication():
  print("*")



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
operands = ["+","-","*", "/", "all"]

#Questions 
low_question = "Please enter a low number: "
high_question = "Please enter a high number: "
no_q_question = "How many questions: "



if __name__ == "__main__":




  print("Welcome to the Basic Maths Game!!!")

  #Ask user for operator
  operand = input("Pick an operator +, -, /, * or all ")

  #Ask user if they want negative intergers
  want_neg_int = "invalid choice"
  while want_neg_int == "invalid choice":
   want_neg_int = input("Do you want negative integers: ").lower()
   want_neg_int = string_check(want_neg_int, yes_no)
   if want_neg_int == "invalid choice":
     print("Please enter a valid choice (yes/no)")

  #Ask user for low number
  space(1)
  low_num = int_checker(low_question)

  #Ask user for high number
  space(1)
  high_num = int_checker(high_question)
  
  #Ask how many questions they want
  #Temporary for testing 
  space(1)
  num_questions = int_checker(no_q_question)


  space(2)
  #Loop for number of questions
  for questions in range(0, num_questions):


     if operand == "+":
        addition()


     elif operand == "-":
        subtraction()
      
 
     elif operand == "/":
        division()
      
      
     elif operand == "*":
        multiplication()

      #When user enters all
     else:
            #this is called when user inputs all
            min_num = 3
            max_num = 7
            random_num = random_generator(min_num, max_num)
            print(random_num)
            print("go to random generator, send min_num and max_num (1 and 5)")
            print("then randomly go to each of the operand functions")

    
  
