import random
def fullTime():
    return 8
def partTime():
    return 4
def absent():
    return 0
def check_attendence():

    number = random.randint(0, 2)
    switcher = {
        0: absent,
        1: fullTime,
        2: partTime,
    }
    return switcher.get(number)
def total_wage_and_hrs():
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    MAX_HRS_IN_MONTH = 100
    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage=0
    empWage = 0
    while totalEmpHrs <= int(MAX_HRS_IN_MONTH) and totalWorkingDays < NUM_OF_WORKING_DAYS:
            totalWorkingDays+=1
            option = check_attendence()
            totalEmpHrs=totalEmpHrs+option()
            empWage=option()*EMP_RATE_PER_HOUR
            #Incrementing and storing the values in total emp wage
            totalEmpWage += empWage
    print("Total Employee Hours : ",totalEmpHrs)
    print("Total Employee Wage : ",totalEmpWage)

if __name__== '__main__':
    total_wage_and_hrs()