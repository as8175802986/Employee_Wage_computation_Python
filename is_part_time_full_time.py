import random
def part_tine_full_time():
    number = random.randint(0, 1)
    EMP_RATE_PER_HOUR = 20
    if number == 1:
        print("Employee is FullTime")
        empHrs = 8
    else:
        print("Employee is PartTime")
        empHrs = 4
    print("Daliy Wage is : ", empHrs * EMP_RATE_PER_HOUR)

#Calling function to print result
if __name__== '__main__':
    part_tine_full_time()