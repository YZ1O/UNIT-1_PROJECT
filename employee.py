from person import * 
from datetime import date
#import xlsxwriter
from openpyxl import Workbook
class Employee(Person):

    employee_id:int=0
    employees_information:list=[]
    date_of_hiring=date.today()

    def __init__(self,id:str,name:str,salary:str,position:str,service_month:int,gender:str):
        Employee.employee_id+=1
        Employee.date_of_hiring
        super().__init__(id,name,gender)
        self.verify_info(id,name,salary,position,service_month,gender)

    def set_emp_id(self,emp_id:int):
        Employee.employee_id=emp_id

    def get_emp_id(self):
        return Employee.employee_id

    def set_salary(self,salary):
        self.__salary = int(salary)

    def get_salary(self):
        return self.__salary
    
    def set_position(self,position):
        self.__position = position
    
    def get_position(self):
        return self.__position

    def set_service_month(self,service_month):
        self.__service_month = service_month
        
    def get_service_month(self):
        return self.__service_month

    def set_date_of_hiring(self,date):
        Employee.date_of_hiring=date
        
    def get_date_of_hiring(self):
        return Employee.date_of_hiring
    
    def salary_in_year(self):
        return self.get_salary() * 12
    
#Class_Method
    def verify_info(self,id:str,name:str,salary:str,position:str,service_month:int,gender:str):
        while len(id) != 10 or not id.isdigit:
            id = input("Enter a valid id: ")
        self.set_id(id)
        #######################################
        while len(name) < 3 :
            name = input("Enter a valid name: ")
        self.set_name(name)
        #######################################
        while not str(salary).isdigit():
            salary = input("Enter a valid Salary: ")
        self.set_salary(int(salary))  
        #######################################
        while len(position) < 3 :
            position = input("Enter a valid position: ")
        self.set_position(position)  
        #######################################
        while type(service_month) != int :
            service_month = int(input("Enter a valid service month: "))
        self.set_service_month(service_month)  
        #######################################
        while len(gender) < 4 or len(gender) > 6 :
            gender = input("Enter a valid gender: ")
        self.set_gender(gender)
        print('the information has be saved!'.upper())
    

    def get_employees_info(self):
        for employee in Employee.employees_information:
            print(f'National id : {employee[0]}  employee id : {employee[1]}  name : {employee[2]}  salary : {employee[3]}  position : {employee[4]}  service month : {employee[5]}  gender : {employee[6]}  date of hiring : {employee[7]}'.upper())

    def save_employee_info_list(self):
        temp_save_info=[self.get_id(),self.get_emp_id(),self.get_name(),self.get_salary(),self.get_position(),self.get_service_month(),self.get_gender(),self.get_date_of_hiring()]
        Employee.employees_information.append(temp_save_info)
        return f'Information has been saved This is the employee id : {self.get_emp_id()}'.upper()

    def search_by_id(self,id:str):
        for employee in Employee.employees_information:
            if employee[0] == id:
                return employee
        return f'Sorry this national id is not found'.upper()

    def search_by_employee_id(self,employee_id:int):
        for employee in Employee.employees_information:
            if employee[1] == employee_id:
                return employee
        return None

    def search_by_name(self,name:str):
        result = []
        for employee in Employee.employees_information:
            if employee[2].lower() == name.lower():
                result.append(employee)
        return result

    def search_by_salary(self,salary_from:int,salary_to:int):
        result = []
        for employee in Employee.employees_information:
            if salary_from <= employee[3] <= salary_to:
                result.append(employee)
        return result
    def search_by_position(self,position:str):
        result = []
        for employee in Employee.employees_information:
            if employee[4].lower() == position.lower():
                result.append(employee)
        return result

    def search_by_gender(self,gender):
        result = []
        for employee in Employee.employees_information:
            if employee[6].lower() == gender.lower():
                result.append(employee)
        return result

    def search_info(self):

        searching=True
        while searching:
            user_answer=input("Do you want to search by 1-id 2-employee id 3-name 4-salary from-to 5-position 6-gender or enter exit : ")
            if user_answer == '1':
                id = input("Enter the national id: ")
                search_id = self.search_by_id(id)
                print(f'result of national id search : {search_id}\n'.upper())
            elif user_answer == '2':
                employee_id = input("Enter the employee id: ")
                search_emp_id = self.search_by_employee_id(employee_id)
                print(f'result of employee id search : {search_emp_id}\n'.upper())
            elif user_answer == '3':
                name = input("Enter the name: ")
                search_name = self.search_by_name(name)
                print(f'result of name search : {search_name}\n'.upper())
            elif user_answer == '4':
                salary_from = int(input("Enter the salary_from: "))
                salary_to = int(input("Enter the salary_to: "))
                search_salary = self.search_by_salary(salary_from,salary_to)
                print(f'result of salary search : {search_salary}\n'.upper())
                ask_user_for_save = input("Do you want to save the information? in excel file (y/n) : ")
                if ask_user_for_save == 'y':
                    file_name = input("Just Enter the file name don\'t write extend : ")
                    file_name+='.xlsx'
                    wb = Workbook() # creates a workbook object.
                    ws = wb.active # creates a worksheet object.
                    for row in search_salary:
                        ws.append(row) # adds values to cells, each list is a new row. 
                    wb.save(file_name) # save to excel file.
                    print(f'information has been saved in excel file it\'s name {file_name}'.upper()+'.xlsx')

            elif user_answer == '5':
                position = input("Enter the position: ")
                search_position = self.search_by_position(position)
                print(f'result of position search : {search_position}\n'.upper())
            elif user_answer == '6':
                gender = input("Enter the gender: ")
                search_gender = self.search_by_gender(gender)
                print(f'result of gender search : {search_gender}\n'.upper())
            elif user_answer == 'exit':
                searching=False
            else:
                print("Invalid input choose from this list")
                user_answer=input("Re-Enter 1-id,2-employee id,3-name,4-salary_from-to,5-position,6-gender")
