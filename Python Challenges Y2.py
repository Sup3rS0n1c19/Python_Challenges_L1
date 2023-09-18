#Python Programming Challenges Year 2

#Menu
def Menu():
    print("1) Area of a Triangle 2) Power Calculator 3) Addition 4) Age Converter")
    global userChoice
    userChoice = int(input("Please select a number between 1 and 7: "))
    
    if userChoice == 1:
        areaTriangle()
    elif userChoice == 2:
        powerCalculator()
    elif userChoice == 3:
        Addition()
    elif userChoice == 4:
        ageConverter()



#Area of a triangle

def areaTriangle():
    height = int(input("Please enter the height of the triangle: "))
    base = int(input("Please enter the base of the triangle: "))
    area = (base * height) / 2
    print("The area of the triangle is " + str(area))


#Power Calculator

def powerCalculator():
    voltage = int(input("Please enter the amount of voltage: "))
    current = int(input("Please enter the amount of current: "))
    circuit_power = (voltage * current)
    print(str(circuit_power) + "W")


#Return the Sum of Two Numbers

def Addition():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter another number: "))
    total = (num1 + num2)
    print("The total is " + str(total))

    if num1%7 or num2%7:
        division = num1 / num2
        print("The division answer would be " + str(division))

    elif num1%11 or num2%11:
        multiplication = num1 * num2
        print("The multiplication answer would be " + str(multiplication))
    

#Convert Age to Days

def ageConverter():
    age = int(input("Please enter your age: "))
    conversion = (age * 365)
    print("Your age in days is " + str(conversion))

    LY_conversion = (age * 365) + (age // 4)
    print("Your age in days, including leap years, is " + str(LY_conversion))


Menu()
