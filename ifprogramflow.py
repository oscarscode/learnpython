# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}: ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the ballot box")
# else:
#     print("Please come back in {} years".format(18 - age))

myno = 8
print("Please guess a number between 1 and 10:")
guess = int(input())

# if guess < myno:
#     print("Please guess higher:")
#     guess = int(input())
#     if guess == myno:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > myno:
#     print("Please guess lower:")
#     guess = int(input())
#     if guess == myno:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess == myno:
#     print("You got it on the first try!!")

if guess != myno:
    if guess > myno:
        print("Please guess lower:")
    else:
        print("Please guess higher:")
    guess = int(input())
    if guess == myno:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("Well done, you guessed it!")