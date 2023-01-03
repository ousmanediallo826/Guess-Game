import random

number = random.randint(1, 100)
# user_name = input('Enter your name:')
number_of_attempt = 0
# print("Hello", + user_name+  "Iam a a guessing game from 1 to 100." )

while number_of_attempt < 5:
  guess = int(input("Enter a number: "))
  number_of_attempt += 1
  if guess > number:
    print("number is too High.")
  if guess < number:
    print("number is too low")
  if guess == number:

    break

if guess == number:
  print("Your guess is right!")

else:
  print("Enter a number")
