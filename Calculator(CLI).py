from functools import reduce
import operator
import numpy
from time import sleep

counter = 0
number_list = []
divisor = []
again = True
op_list = "\n1. Addition(+) \n 2. subtraction(-) \n 3. multiplication(*) \n 4. division(/)"

print(op_list)
sleep(3)
while again:
    type_op = int(input("Enter type of operation (must be a number) > "))
    if type_op == 4:
        input_number = int(input("Enter your divisor > "))
        divisor.append(input_number)
    times = int(input("Enter the amount of numbers you would like to do some math on > "))
    while counter < times:
        input_number = int(input("Enter a number (Just one): "))
        number_list.append(input_number)
        counter += 1

    if type_op == 1:
        print("\n", number_list[0], "+", number_list[1:], "= ", sum(number_list))
    elif type_op == 2:
        print("\n", "the difference ", "= ", reduce(operator.__sub__, number_list))
    elif type_op == 3:
        print("\n", number_list[0], "* ", number_list[1:], "= ", reduce((lambda x, y: x*y), number_list))
    elif type_op == 4:
        whatever = numpy.divide(number_list, divisor)
        print("\n", "Quotients of each number divided by ", divisor, "= ", whatever, " In respecting order")
    else:
        print("There was a problem, sorry!")
        sleep(1)
        print("Terminating...")
        sleep(2)
        input("Click any key.....")
        break

    again_in = input("\nEnter with \'yes\' or \'no\' if you would like to use again or not > ").lower()
    if again_in == "yes":
        again = True
        counter = 0
        number_list = []
        divisor = []
    elif again == "no":
        again = False
    else:
        print("There was a problem, sorry!")
        sleep(1)
        print("Terminating...")
        sleep(2)
        input("Click any key.....")
        break

