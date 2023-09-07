# 1. Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

i =1
while i <= 100:
    if i % 3 ==0:
        print(i)
    i +=1



# 2. Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

while True:
    inch = float(input("Enter number that you want to convert. =  "))
    if inch <1:
       print("ERROR VALUE")
       break

    centi= inch * 2.54  # 1 inch = 2.54 centimeter
    print(f"{inch} inches is equal to {centi} centimeter")



# 3. Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
smallest =None
largest = None

while True:
    try:
        num = input(" Enter a number or press enter to end :")
        if num == "":
            break

        num = int(num)
        if largest is None or largest < num:
            largest = num
        if smallest is None or smallest > num:
            smallest = num

    except ValueError:
        print("Invalid input")
        continue

print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")



# 4. Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

import random
SN = random.randint(1,10)
while True:
    EV = int(input("Guess the number = "))
    if EV == SN:
        print("You have guessed correct number")
        break
    elif EV < SN:
        print("Too low")
    else:
        print("Too high")



# 5. Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.p

max_count = 5
attempt = 0


while attempt < max_count:
    user_name = input("Enter Username : ")
    password = input("Enter Password : ")
    if user_name == "python" and password == "rules":
        print("WELCOME")
        break
    else:
        print("Incorrect password ")

    attempt +=1

if max_count == attempt:
    print("ACCESS DENIED ")



# 6. Implement an algorithm for calculating an approximation for the value of pi (π).........




