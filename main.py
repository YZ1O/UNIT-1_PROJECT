from employee import *

print('Welcome to Employee Management System')
user_input = ''
while not user_input=='exit':
    user_input = input("Enter your choice: 1- to add employee, 2- to view all employees, 3- to search or enter exit: ")
    if user_input == '1':
        id = input("Enter national id for employee: ")
        name = input("Enter employee's name: ")
        position = input("Enter employee's position: ")
        salary = input("Enter employee's salary: ")
        service_month = int(input("Enter employee's service month: "))
        gender = input("Enter employee's gender: ")
        object = Employee(id,name,salary,position,service_month,gender)
        print(object.save_employee_info_list())
        
    elif user_input == '2':
        object.get_employees_info()
    elif user_input == '3':
        object.search_info()
    elif user_input == 'exit':
        print('Thank you for using Employee Management System')   
    else:
        print('Invalid choice')
        user_input = input("Re-Enter your choice: 1-to add employee, 2-to view all employees, 3-to search or enter exit: ")

