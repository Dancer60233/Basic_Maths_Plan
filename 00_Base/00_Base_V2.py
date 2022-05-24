#Basic Maths Game Base V2
#Aim - To add and try to understand the random generator



#import library************************************************
import random as r

#Functions

def check_int():
 print("checkint")

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







#Main Routine


#Lists
answer_list = [ ]
yes_no = [
  ["yes", "y"],
  ["no", "n"],
]
operands = ["+","-","*", "/", "all"]



if __name__ == "__main__":



  print("Welcome to the Basic Maths Game!!!")

  #Ask user for operator
  operand = input("Pick an operator +, -, /, * or all ")

  #Ask user if they want negative intergers
  negatives = input("Do you want negative numbers? ").lower()
  negatives = string_check(negatives , yes_no)
  print(negatives)
  
  #Ask user fo high and low number
  #Int checker to see if its suitable
  
  #Ask how many questions they want
  #Temporary for testing 
  num_questions = 1
  
  #Loop for number of questions
  for questions in range(0, num_questions):


     if operand == "+":
        addition()


     elif operand == "-":
        subtraction()
      
 
     elif operand == "/":
        divison()
      
      
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
\
    
  
