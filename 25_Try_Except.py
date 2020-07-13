try:
    number = int(input("Enter a number: "))
    result = number / 2
    print(str(number) + " / 2 = " + str(result))
except:
    print("Something was wrong") # => return for all error case



try:
    number1= int(input("Enter a number 1: "))
    number2 = int(input("Enter a number 2: "))
    result = number1 / number2
    print(str(number1) + " / " + str(number2) +" = " + str(result))
except ZeroDivisionError as err_1:
    print(err_1) # => input: 0
except ValueError:
    print("Invaild input") # => input: 'a'
