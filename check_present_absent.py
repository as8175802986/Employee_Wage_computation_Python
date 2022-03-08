import random
def attendence():
    number = random.randint(0, 1)
    if number == 1:
        print("Employee is present")
    else:
        print("Employee is absent")

#Calling function to print result
if __name__== '__main__':
    attendence()