#Simple Calculator

#First to make functions for each operation

#Add function
def myFuncAdd(num1, num2):
    return (num1 + num2)

#Subtract function
def myFuncSub(num1, num2):
    return (num1 - num2)

#Multiply Function
def myFuncMul(num1, num2):
    return (num1*num2)

#Divide function
def myFuncDiv(num1, num2):
    if(num2 == 0):
        print("Divide by zero error")
    else:
        return (num1/num2)
    
#Main function
def __main():
    print("Enter numbers\n")
    print("Enter operation\n")

__main()     
        
