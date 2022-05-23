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

yes_no = [
  ["yes", "y"],
  ["no", "n"],
]

operands = ["+", "-","*", "/"]

negatives = input("Do you want negative numbers? ").lower()
negatives = string_check(negatives , yes_no)
print(negatives)