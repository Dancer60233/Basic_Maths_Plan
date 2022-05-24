def int_check(question):
 error = "Please enter a whole number that is more than 0"
 
 valid = False
 while not valid:

   #ask user for number and check it is valid
  try:
    response = int(input(question))

    #Checks if number is in range
    if response <= 0:
     print(error)     
    else:
      return response
      
    
  #if an interger us not entered, display an error message   
  except ValueError:
    print(error)


    
print("Welcome to the Basic Maths Game!!!")
operator = input("Pick an operator +, -, /, * or all ")





