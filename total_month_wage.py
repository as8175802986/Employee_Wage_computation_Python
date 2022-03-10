import random
def fulltime():
    return 8

def parttime():
    return 4

def absent():
    return 0

def check_attendence():

    number = random.randint(0, 2)
    switcher = {
        0: absent,
        1: fulltime,
        2: parttime,
    }
    return switcher.get(number)

def total_month_wage():
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    empHrs = 0
    empWage = 0
    totalEmpWage = 0
    day = 0
    while day<NUM_OF_WORKING_DAYS:
    # Get the option from switcher dictionary
        option = check_attendence()
        empWage=(option()*EMP_RATE_PER_HOUR)
        totalEmpWage += empWage
        day+=1
    #print employee wage
    print("Total Employee Wage : ",totalEmpWage)

#Calling function to print result
if __name__== '__main__':
    total_month_wage()
