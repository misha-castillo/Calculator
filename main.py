import math
# Program make a simple calculator

# This function let you choose how many numbers to operate
def selectNumbers():
    
    selectNumbersTot = numberChecker('0')

    return selectNumbersTot

def numberChecker(option,i=0,result=0):
    
    # Counter for number of attempts before closing the application after entering a wrong value format.
    attemptCounter = 3
    # Counter to know what question to ask. Addition, subtraction and multiplication only require 1 sentence to ask, other operations require 2 different sentences to ask
    counterValuesNeeded = 2
    
    while counterValuesNeeded > 0:
        # Try to check if the input value is a number. It will run while the attempt counter is greater than 0.
        while attemptCounter > 0:
            try:

                # Ask the numbers the user wants to operate.
                if option == '0':                    
                    counterValuesNeeded = 1
                    numI = int(input("How many numbers do you want to operate? "))
                
                # Ask for the i-ish number you want to add.
                # i+1 is displayed so the user can se the 1st number to add instead of the 0th number to add.
                if option == '1':
                    counterValuesNeeded = 1
                    numI = float(input("Enter number " + str(i+1) + " to add: "))

                # Ask for the i-ish number you want to subtract.
                elif option == '2':
                    counterValuesNeeded = 1
                    numI = float(input("Enter number " + str(i+1) + " to subtract: "))
                
                # Ask for the i-ish number you want to multiply.
                elif option == '3':
                    counterValuesNeeded = 1
                    numI = float(input("Enter number " + str(i+1) + " to multiply: "))
                
                elif option == '4':
                    dividend = float(input("Enter dividend number: "))
                    print("dividend asked")
                    divisor = float(input("Enter divisor number: "))
                    print("divisor asked")
                    if divisor == 0:
                        print("Invalid divisor value. Make sure the devisor is different from 0")
                    
                
                elif option == '5':
                    baseN = float(input("Enter base number: "))
                    expN = float(input("Enter exponent number: "))
                
                elif option == '6':
                    baseN = float(input("Enter base number: "))
                    expN = float(input("Enter the Nth root number: "))
                                    
                elif option == '7':
                    counterValuesNeeded == 1
                    numI = float(input("Enter number: "))
                    if numI == 0:
                        print("Invalid divisor value. Make sure the devisor is different from 0")
                    
                
                    
                # If all good, the counter is set to 0 so the application does not ask for the same i-ish number again.
                attemptCounter = 0
                
            # If value is not a number (float), the ValueError exception is send.
            except ValueError:
                # If there are chances to type the right number, ask for it.
                if attemptCounter > 1:
                    # Asking the user to type a number.
                    print("A string was entered, please enter a valid number")
                # If the counter is set to 1, then the application won't accept more inputs and it will close.
                else:
                    print("No correct value entered after 3 attempts. Closing Program.\n")
                    # Return the sum of valid numbers entered.
                    return result
                    
            # The attempt counter is decreased by 1.
            attemptCounter -= 1
        counterValuesNeeded -= 1


    if option < '4' or option == '7':
        return numI
    elif option == '4':
        return dividend, divisor
    else:
        return baseN, expN

def pi_e_changer(num1,num2=1):
    # Change if the number input is 3.14 or 3.1415 to PI, or if the number input is 2.7182 to euler number.
    if num1 == 3.14 or num1 == 3.1415:
        num1 = math.pi
    elif num1 == 2.7182:
        num1 = math.e
    if num2 == 3.14 or num2 == 3.1415:
        num2 = math.pi
    elif num1 == 2.7182:
        num2 = math.e

    return num1, num2
    

# This function adds s numbers.
def add(s,m):
    # Define the sum accumulator.
    sumNum = 0

    # Call function to use the last number saved
    memValue = useLastValue(s,m)
    sumNum = memValue[0]
    s = memValue[1]
        
    # Iterate i s times.
    for i in range(s):
        numI = numberChecker('1',i,sumNum)

        # Convert numbers if 3.14 or 2.71 were used.
        numI = pi_e_changer(numI)
        numI = numI[0]

        # Start summing previous value with the new one.
        sumNum += numI
        
    return sumNum

# This function subtracts s numbers.
def subtract(s,m):
    # Define the list where the numbers to subtract will be stored.
    subNumV = []
    numI = 0

    # Call function to use the last number saved
    memValue = useLastValue(s,m)
    if  memValue[2] == 1:
        subNumV.append(memValue[0])
        s = memValue[1]
    
    # Iterate i s times.
    for i in range(s):
        numI = numberChecker('2',i,numI)

        # Convert numbers if 3.14 or 2.71 were used.
        numI = pi_e_changer(numI)
        numI = numI[0]
        
        # Appending (or adding) the new number to the list.
        subNumV.append(numI)
        
    # The subtract accumulator is defined.
    # Its value is the first value added to the list.
    subNum = subNumV[0]
    
    # Iterate i s times.
    for i in range(len(subNumV)):
        # Do the operation only if i is greater than 0, because the value of subNumV[0] was already used before enter the loop.
        if i > 0:
            # Do the subtraction of the subNum with the next value in the list.            
            subNum = subNum - subNumV[i]
            
    return subNum

# This function multiplies s numbers.
def multiply(s,m):
    # Define the multiply accumulator
    timesNum = 1

    # Call function to use the last number saved
    memValue = useLastValue(s,m)
    if  memValue[2] == 1:   
        timesNum = memValue[0]
        s = memValue[1]
    
    # Iterate i s times
    for i in range(s):
        numI = numberChecker('3',i,timesNum)

        # Convert numbers if 3.14 or 2.71 were used.
        numI = pi_e_changer(numI)
        numI = numI[0]
        
        # Start multiplication of subNum times the new number defined.
        timesNum = timesNum * numI
        
    return timesNum

# This function divides two numbers and is also used to get the inverse value of a number
def divide(s,m):
    if s == 4:
        div = numberChecker('4')
        dividend = div[0]
        divisor = div[1]

        # Convert numbers if 3.14 or 2.71 were used.
        numI = pi_e_changer(div[0], div[1])
        dividend = numI[0]
        divisor = numI[1]
        
        return dividend/divisor       

    elif s == 7:

        # Call function to use the last number saved
        memValue = useLastValue(s,m)
        
        if memValue[2] == 1:
            # Convert numbers if 3.14 or 2.71 were used.
            numI = pi_e_changer(m[len(m)-1])
            return 1/numI[0]
        
        else:
            divisor = numberChecker('7')
            # Convert numbers if 3.14 or 2.71 were used.
            numI = pi_e_changer(divisor)
            divisor = numI[0]
            return 1/divisor
        

# Function to get the power of a number or Nth root of a number
def powerExp(s):


    if s == 5:
        base_exp = numberChecker('5')
    elif s == 6:
        base_exp = numberChecker('6')
    
    base = base_exp[0]
    expN = base_exp[1]

    # Convert numbers if 3.14 or 2.71 were used.
    numI = pi_e_changer(base, expN)
    base = numI[0]
    expN = numI[1]

    if s == 5:
        return pow(base,expN)
    elif s == 6:
       return pow(base,1/expN)

#Function to store outputs
def memorySave(m):
    
    if m != 'none':
        answer = input("Do you want to store the obtained value (yes / no): ")
        if answer == 'yes':
            print("The value has been saved. Type 'mem' to access it")
    return m

def history(m):
    return m

def useLastValue(s,m):
    answer = input("Use last saved value? (yes/no): ")
    if answer == 'yes' and m != []:
        numI = m[len(m)-1]
        s = s - 1
        return numI, s, 1
    elif answer == 'yes' and m == []:
        print("You don't have a stored value in memory")
        return 0, s, 0
    else:
        return 0, s, 0
    
print("Select operation.\n")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Nth Root")
print("7.Inverse")
print("8.History")
print("q.Quit")

mem=[]

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/q: ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', 'q'):



        if choice == '1':
            selectNumbersTot = selectNumbers()
            additionValue = add(selectNumbersTot,mem)
            print(str(additionValue))
            mem.append(memorySave(additionValue))
            
        elif choice == '2':
            selectNumbersTot = selectNumbers()
            subtractValue = subtract(selectNumbersTot,mem)
            print(str(subtractValue))
            mem.append(memorySave(subtractValue))

        elif choice == '3':
            selectNumbersTot = selectNumbers()
            multiplyValue = multiply(selectNumbersTot,mem)
            print(str(multiplyValue))
            mem.append(memorySave(multiplyValue))

        elif choice == '4':
            divisionValue = divide(4,mem)
            print(str(divisionValue))
            mem.append(memorySave(divisionValue))

        elif choice == '5':
            powerValue = powerExp(5)
            print(str(powerValue))
            mem.append(memorySave(powerValue))

        elif choice == '6':
            nRootValue = powerExp(6)
            print(str(nRootValue))
            mem.append(memorySave(nRootValue))

        elif choice == '7':
            inverseValue = divide(7,mem)
            print(str(inverseValue))
            mem.append(memorySave(inverseValue))

        elif choice == '8':
            print("History of results:")
            print(history(mem))

        elif choice == 'q':
            print("Thanks for using the Calculator. Have a nice day. Bye, Bye.")
            break
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            print("Thanks for using the Calculator. Have a nice day. Bye, Bye.")
            break
    
    else:
        print("Invalid Input, please enter a valid option.")
