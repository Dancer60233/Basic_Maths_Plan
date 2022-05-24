#25/5/22 - Kate Barber
#Basic Maths Program
#Integer Checker V1
#Aim - Create a function that checks if input is a whole number


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




return_num = int_checker("Please enter an integer: ", "Invalid! Please enter an integer: ")
print(return_num)