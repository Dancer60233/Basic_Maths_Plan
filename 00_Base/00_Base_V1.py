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

def ran_num():
  print("ran_num")

def addition():
  print("+")

def subtraction():
  print("-")

def division():
  print("/")
  
def multiplication():
  print("*")


#Main Routine




#Main Routine


#Lists

yes_no = [
  ["yes", "y"],
  ["no", "n"],
]


print("Welcome to the Basic Maths Game!!!")

#Ask user for operator
operator = input("Pick an operator +, -, /, * or all ")

#Ask user if they want negative intergers
negatives = input("Do you want negative numbers? ").lower()
negatives = string_check(negatives , yes_no)
print(negatives)

#Ask user fo high and low number

#Ask how many questions they want

#Loop for number of questions
  

