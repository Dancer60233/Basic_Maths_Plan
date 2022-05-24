import random as r


def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num

if __name__ == "__main__":
  min_num = 1
  max_num = 5
  random_num = random_generator(min_num, max_num)
  print(random_num)
  print("go to random generator, send min_num and max_num (1 and 5)")
  print("then randomly go to each of the operand functions")