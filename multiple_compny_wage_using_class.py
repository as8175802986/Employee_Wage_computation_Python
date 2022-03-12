import random
class Company:
    def __init__(self, name,num_of_working_days,max_hrs_in_month):
        self.name = name
        self.num_of_working_days=num_of_working_days
        self.max_hrs_in_month=max_hrs_in_month
    def __str__(self):
        return self.name

class EmpWage:
    def __init__(self):
        self.company_dict = {}

    def add_company(self, name,num_of_working_days,max_hrs_in_month):
        ob = Company(name,num_of_working_days,max_hrs_in_month)
        self.company_dict.update({ob.name: ob})
    def get_the_company(self, name):

        ob = self.company_dict.get(name)
        return ob


    def attendence(self):
        self.number = random.randint(0, 2)

        if self.number == 0:
            #print("Absent")
            return 0
        elif self.number == 1:
            #print("full Time")
            return 8
        else:
            #print("Part time")
            return 4

    def total_emp_wage(self, name):
        ob=self.get_the_company(name)
        if ob is None:
            raise Exception("Company not found")
        emp_rate_per_hr = 20
        totalEmpHrs = 0
        totalWorkingDays = 0
        totalEmpWage = 0
        empWage = []
        while totalEmpHrs <= int(ob.max_hrs_in_month) and totalWorkingDays < int(ob.num_of_working_days):
            emp_attendence=self.attendence()
            totalEmpHrs = totalEmpHrs + emp_attendence
            empWage.append(emp_attendence * emp_rate_per_hr)
            print("Daily wage : ", empWage[totalWorkingDays])
            totalWorkingDays += 1

        print(empWage)
        print("Total Employee Hours for : ",name,"is", totalEmpHrs)
        print("Total Employee Wage for : ",name,"is", sum(empWage))

if __name__:
    object = EmpWage()
    object.add_company("Accenture", 20, 100)
    object.total_emp_wage("Accenture")




