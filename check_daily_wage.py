import random
def daily_wage():
    EMP_RATE_PER_HOUR = 20
    number = random.randint(0, 1)
    if number == 1:
        print("Employee is present")
        empHrs = 8
    else:
        print("Employee is absent")
        empHrs = 0
    print("Daliy Wage is : ", empHrs * EMP_RATE_PER_HOUR)

#Calling function to print result
if __name__== '__main__':
    print(daily_wage())

