#25/5/22 - Kate Barber
#Basic Maths Program
#Integer Checker V2
#Aim - Create a function that still checks the integer but is more flexible


def int_checker(question, error_message): 
  valid = False
  while not valid:

   #ask user for number and check it is valid
   try:
    response = int(input(question))
    valid = True
    #Checks if number is in range
   except:
    print(error_message)

  return response
      

#main 

#Allows user to easily change question and error_message
question = "Please enter a whole number: "
error_message = "Invalid! Please enter a whole number: "

#Gets users input and checks if its awhole number 
return_num = int_checker(question, error_message)
print(return_num)