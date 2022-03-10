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


def total_wage():
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    MAX_HRS_IN_MONTH = 100

    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage = 0
    empWage = []
    while totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:

        option = check_attendence()
        totalEmpHrs = totalEmpHrs + option()
        empWage.append(option() * EMP_RATE_PER_HOUR)
        print("Daily wage : ", empWage[totalWorkingDays])
        totalWorkingDays += 1
    print("Total Employee Hours : ", totalEmpHrs)
    print("Total Employee Wage : ", sum(empWage))
    print(empWage)
    print(len(empWage))

# print employee wage
if __name__== '__main__':
    total_wage()
