#26/5/22 - Kate Barber
#Basic Maths Program
#String Checker V2
#Aim - Create a function that still checks if the input is valid but by using variables and lists
#Reflection - The code works and is flexible with the varibles and error message however it is quite large (May change depending if it's needed moe than once)

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




#Lists

yes_no = [
  ["yes", "y"],
  ["no", "n"],
]
    

#Main Routine
want_neg_int = "invalid choice"
while want_neg_int == "invalid choice":
   want_neg_int = input("Do you want negative integers: ").lower()
   want_neg_int = string_check(want_neg_int, yes_no)
   if want_neg_int == "invalid choice":
     print("Please enter a valid choice (yes/no)")
print(want_neg_int)



