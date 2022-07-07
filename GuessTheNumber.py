import random
number=random.randint(1,10)

name=input("Hello,whats your name?")
number_of_guesses=0
print("Okay! "+name+" guess the number between 1 and 10")
 
while number_of_guesses<5:
    guess=int(input())
    number_of_guesses +=1
    if guess<number:
        print("Your guess is low")
    elif guess>number:
        print("Your guess is high")
    elif guess==number:
        break

if guess==number:
    print("😊 You guessed the number in "+str(number_of_guesses)+" tries!")
else:
    print("😔 You did not guess the correct number, The number was "+ str(number))