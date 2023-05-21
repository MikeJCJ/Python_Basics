#Creating the Parent class (Generic Employee)
################################################################
class Employee(): #Creating a parent class
    job_title = 'Employee'
    christmas_bonus = 0.05 #Class attributes (no input required)
    def __init__(self, name, age, base_salary, contract_type): #Class attributes (input required)
        self.name = name
        self.age = age
        self.base_salary = base_salary
        self.contract_type = contract_type
    
    def CalculateSalary(self): #Class method
        salary = self.base_salary * (self.christmas_bonus+1)
        return salary

#Creating child classes
################################################################
class Salesman(Employee):
    job_title = 'Salesman'
    commission = 0.1
    def __init__(self, name, age, base_salary, contract_type, last_year_sales):
        super().__init__(name, age, base_salary, contract_type) #super() is required in order to inherit attributes from the parent class
        #.super() can be used to call any method in the Parent Class
        self.last_year_sales = last_year_sales

    def CalculateSalary(self): #Creating a function with the same name and number of parameters as the parent class overrides the parent method
        salary = self.base_salary*(self.christmas_bonus+1) + self.last_year_sales*self.commission
        return salary

class Boss(Employee):
    job_title = 'Boss'
    def __init__(self, name, age, base_salary, contract_type, tier):
        super().__init__(name, age, base_salary, contract_type) #Do not need to include 'self' when using .super()
        self.tier = tier

    def CalculateSalary(self):
        salary = 1.1**self.tier + self.base_salary * (self.christmas_bonus+1)
        return salary

class_dict = {'Employee':Employee, 'Salesman':Salesman, 'Boss':Boss} #Allows classes to be created dynamically
#Creating instances of the parent and child classes
################################################################
def CreateEmployee(employee_type, employee_data): #Creates employees dynamically
    employee = class_dict[employee_type](*employee_data) #Uses class_dict to translate the string into the desired class creation
        # using '*' expands list elements into the function arguments, '**' is used for dictionaries
    return employee

#Employee data
employee_data_array = {'Employee':[["Mike", 21, 30000, "full-time"], ["Edgar", 30, 20000, "part-time"]] \
                ,'Salesman':[["Jannett", 40, 32000, "consultant", 200000], ["Jimbo", 32, 38000, "full-time", 250000]] \
                ,'Boss':[["harriette", 50, 55000, 'full-time', 1], ["Rashid", 60, 60000, 'full-time', 2]] }

if __name__=='__main__':
    employee_list = {}
    for employee_type in employee_data_array:
        for employee_data in employee_data_array[employee_type]:
            employee_list['employee'+str(len(employee_list))] = CreateEmployee(employee_type, employee_data)
    for key, employee in employee_list.items():
        print(f"The {employee.job_title} named {employee.name} earns {employee.CalculateSalary()} each year")