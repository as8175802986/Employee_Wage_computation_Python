import random
def fullTime():
    return 8
def partTime():
    return 4
def absent():
    return 0

class Company_details:
    def Company_details(self):

        self.NUM_OF_WORKING_DAYS=input("NUM_OF_WORKING_DAYS")
        self.MAX_HRS_IN_MONTH=input("MAX_HRS_IN_MONTH")


    #def __str__(self):
    #    return self.name,

class Attendence:
    def check_attendence(self):
        self.number = random.randint(0, 2)
        switcher = {
            0: absent,
            1: fullTime,
            2: partTime,
        }
        return switcher.get(self.number)




class Company:

   def add_company(self,Company):
        self.Company=input("add new Company")
        Companies = []
        Companies.append(option()+self.Company)


    def show(self):
        print(self.Company)


    #def add_company(self,value):
       # ob=Company(value)
       # Company.append(C)
         #empWage.append(option() * EMP_RATE_PER_HOUR)
       # print(ob)
class EmpWage(Company_details,Company,Attendence):

    def emp_wage(self):

        #self.Company= Company.__dict__.get(Company_details)
        #option1 = self.add_company(self,value)

        self.totalEmpHrs = 0
        self.totalWorkingDays = 0
        self.totalEmpWage = 0
        self.EMP_RATE_PER_HOUR = 2020
        empWage = []
        while totalEmpHrs <= int(self.MAX_HRS_IN_MONTH) and self.totalWorkingDays < int(self.NUM_OF_WORKING_DAYS):
            self.Company_details()
            option = self.check_attendence(self)
            totalEmpHrs = totalEmpHrs + option()
            empWage.append(option() * self.EMP_RATE_PER_HOUR)
            print("Daily wage : ", empWage[self.totalWorkingDays])
            self.totalWorkingDays += 1

            print(empWage)
            print("Total Employee Hours : ", totalEmpHrs)
            print("Total Employee Wage : ", sum(empWage))



ob=EmpWage()
ob.Company_details()


