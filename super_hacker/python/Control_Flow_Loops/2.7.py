import random
correct_number = random.randint(1, 11)
while 1:  
  print("Guess a number between 1 and 10")  
  guess = int(input())
  if guess < correct_number:
    print("Your guess is too low.")
  elif guess > correct_number:
    print("Your guess is too high.") 
  else:
    print("You guessed it!")
    break
