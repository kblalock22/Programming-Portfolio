#This is a program that asks the user for a number between 1 and 1000 and then tells the user whether that number is odd or even.

num_input = int(input("Enter a number between 1 and 1000. What number are you thinking?"))

print(num_input)

print("Thank you for your number!")

if (num_input % 2) == 0:
    print("{0} is an even number!".format(num_input))
else:
    print("{0} is an odd number!".format(num_input))


