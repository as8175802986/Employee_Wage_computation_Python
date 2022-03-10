import random

from wage import check_attendence, totalWage


def fullTime():
    return 8
def partTime():
    return 4
def absent():
    return 0
class Attendance():
    def check_attendence(self):
        number = random.randint(0, 2)
        switcher = {
            0: absent,
            1: fullTime,
            2: partTime,
        }
        return switcher.get(number)
class TotalWage():
    def totalWage(self):
        EMP_RATE_PER_HOUR = 20
        NUM_OF_WORKING_DAYS = input("NUM_OF_WORKING_DAYS")
        MAX_HRS_IN_MONTH = input("MAX_HRS_IN_MONTH")
        totalEmpHrs = 0
        totalWorkingDays = 0
        totalEmpWage = 0
        empWage = []
        while totalEmpHrs <= int(MAX_HRS_IN_MONTH) and totalWorkingDays < int(NUM_OF_WORKING_DAYS):

            option = check_attendence()
            totalEmpHrs = totalEmpHrs + option()
            empWage.append(option() * EMP_RATE_PER_HOUR )
            print("Daily wage : ", empWage[totalWorkingDays])
            totalWorkingDays += 1

        print(empWage)
        print("Total Employee Hours : ", totalEmpHrs)
        print("Total Employee Wage : ", sum(empWage))
class Check_Company(Attendance(),TotalWage()):
    def check_Company(self):
        number = random.randint(0, 1)
        if number == 1 :
            print("Bridgelabz")
            totalWage()

        else:
            print("Wtvision")
            totalWage()

    @classmethod
    def totalWage(cls):
        pass


ob=Check_Company
ob.totalWage()