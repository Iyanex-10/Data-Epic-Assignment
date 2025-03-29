#Task 1
for i in range(1, 15):
    print(i)
for i in range(1, 15):
    if i%2==0:
        print("i is even")
    else:
        print("i is odd")







#Task 2
#step 1
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
a = 98
b = 56.7
print(float(98))
print(int(56.7))

#step 2
operation = input("choose an operation (+, -, *, /):")

#Step 3
num_1 = 4
num_2 = 2
if operation == "+":
    result = num_1 + num_2
    print(f"The sum is: {result}")
elif operation == '-':
    result = num_1 - num_2
    print(f"The difference is: {result}")
elif operation == '*':
    result = num_1 * num_2
    print(f"The product is: {result}")
elif operation == '/':
    if num_2 == 0:  
        result = num_1 / num_2
        print(f"The quotient is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Wrong operation, Please enter one of +, -, *, or /")
 
    except ValueError:
print("wrong input, enter only numbers")




    









