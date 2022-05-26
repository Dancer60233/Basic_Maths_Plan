#26/5/22 - Kate Barber
#Basic Maths Program
#String Checker V1
#Aim - Create a function that checks if input is inside to_check
#Reflection - Code is quite basic and I would like to have the list outside of the main code/ inside the brackets


def string_checker(question, to_check):


  valid = False

  while not valid:

    response = input(question).lower()

    if response in to_check:
      return response

    else:
      for item in to_check:
        #checks if response is the first letter of an item in the list
        if response == item[0]:
          # note:returns the entire response rather than just the first letter
          return item

      print("Sorry that is not a valid response")

    

#Main Routine

for item in range (0,6):
  want_integers = string_checker("Do you want " 
                               "integers? ", ["yes", "no"])
  print("Answer OK, you said: {} \n".format(want_integers))



