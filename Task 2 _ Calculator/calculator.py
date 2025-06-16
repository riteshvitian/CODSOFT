def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    if y == 0:
        return "Wrong ! Division By zero"
    return x / y

print("Enter Operation to perform for eg(1,2,3,4)")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
operation = int(input())
num1 = float(input("Enter value 1: "))
num2 = float(input("Enter value 2: "))
if (operation == 1):
    print("Value :",addition(num1,num2))
elif (operation == 2):
    print("Value :",subtraction(num1,num2))
elif (operation == 3):
    print("Value :",multiplication(num1,num2))
elif (operation == 4):
    print("Value :",division(num1,num2))
else:
    print("Invalid Operation")

    
