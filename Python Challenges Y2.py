#Python Programming Challenges Year 2

#Area of a triangle

def areaTriangle():
    height = int(input("Please enter the height of the triangle: "))
    base = int(input("Please enter the base of the triangle: "))
    area = (base * height) / 2
    print("The area of the triangle is " + str(area))

areaTriangle()

#Power Calculator

def powerCalculator():
    voltage = int(input("Please enter the amount of voltage: "))
    current = int(input("Please enter the amount of current: "))
    circuit_power = (voltage * current)
    print(str(circuit_power) + "W")

powerCalculator()

#Return the Sum of Two Numbers

def Addition():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter another number: "))
    total = (num1 + num2)
    print("The tolal is " + str(total))

Addition()

#Convert Age to Days

def ageConverter():
    age = input("Please enter your age: ")
    conversion = (age * 365)
    print("Your age in days is " + conversion)

ageConverter()
    
