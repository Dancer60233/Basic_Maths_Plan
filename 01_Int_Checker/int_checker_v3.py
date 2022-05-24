#25/5/22 - Kate Barber
#Basic Maths Program
#Integer Checker V3
#Aim - To Make the code even more flexible with a consistent error message but a flexible question
#Reflection - Code works well goals are to add spacing and create more accurate questions for base component


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
      

#main 

#Allows user to easily change question 
question = "Please enter an integer: "

#Gets users input and checks if its awhole number 
return_num = int_checker(question)
print(return_num)