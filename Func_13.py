import random
def compare(a, b):
  if a > b:
    return 1
  elif a < b:
    return -1
  else:
    return 0

secret = random.randint(1, 20)
guess = True
while guess:
  guess = int(input("Guess a number between 1 and 20: "))
  if compare(guess, secret) == 1:
    print("Too high")
  elif compare(guess, secret) == -1:
    print("Too low")
  else:
    print("You got it!")
    guess = False
