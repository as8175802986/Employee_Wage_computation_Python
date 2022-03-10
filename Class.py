import random

class Company:
    def __init__(self, name ,num_of_working_days,max_hrs_in_month):
        self.name = name
        self.num_of_working_days = num_of_working_days
        self.max_hrs_in_month=max_hrs_in_month
    def __str__(self):
        return self.name


# ob=Company("Bridgelabz")
# print(ob.name)
class EmpWage(Company):
    def __init__(self, name ,num_of_working_days,max_hrs_in_month):
        super().__init__(name ,num_of_working_days,max_hrs_in_month)
        self.Cname = {"Bridgelabz": ["Bridgelabz"], "wTVision": ["wTVision"]}

    def companies(self, name ,num_of_working_days,max_hrs_in_month):
        ob = Company(name ,num_of_working_days,max_hrs_in_month)
        if name in self.Cname.keys():
            #print(self.Cname[name])
            #print(self.Cname)
            object.total_emp_wage(name ,num_of_working_days,max_hrs_in_month)

        else:
            print("Company invalid")

    '''def fullTime(self):
        return 8

    def partTime(self):
        return 4

    def absent(self):
        return 0'''

    def attendence(self):
        self.number = random.randint(0, 2)
        '''switcher = {
            0: self.absent,
            1: self.fullTime,
            2: self.partTime,
        }'''
        if self.number == 0:
            #print("Absent")
            return 0
        elif self.number == 1:
            #print("full Time")
            return 8
        else:
            #print("Part time")
            return 4

        # return number.get(self.number)

    def total_emp_wage(self, name,  num_of_working_days,max_hrs_in_month):
        ob = Company(name,num_of_working_days,max_hrs_in_month)
        #ob.max_hrs_in_month(value2)
        #ob.num_of_working_days(value1)
        object.attendence()
        self.name = self.Cname.get(name)
        print(self.name)
        #num_of_working_days = 20
        #max_hrs_in_month = 100
        emp_rate_per_hr = 20
        totalEmpHrs = 0
        totalWorkingDays = 0
        totalEmpWage = 0
        empWage = []
        while totalEmpHrs <= int(max_hrs_in_month) and totalWorkingDays < int(num_of_working_days):
            option = object.attendence()
            totalEmpHrs = totalEmpHrs + self.number
            empWage.append(self.number * emp_rate_per_hr)
            print("Daily wage : ", empWage[totalWorkingDays])
            totalWorkingDays += 1

        print(empWage)
        print("Total Employee Hours : ", totalEmpHrs)
        print("Total Employee Wage : ", sum(empWage))

if __name__:
    object = EmpWage("",0,100)
    object.companies("Bridgelabz",20,100)
#object.total_emp_wage("Wtvision")
# object.company_details("wTVision")
# object.total_emp_wage()
