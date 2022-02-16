def tax(salary):
    T=salary*21/100
    return T

    
salary=int(input("Enter your Salary: "))
netsalary=salary-tax(salary)
print("Tax:", tax(salary))
print("Net:",netsalary)