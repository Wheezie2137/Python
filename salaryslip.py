def salaryslip(name,salary):
    if salary>=2000:
        tax=salary*20/100
    else:
        tax=salary*15/100
    netsalary=salary-tax
    print("Name of employee:",name)
    print("Salary:",salary)
    print("Tax:",tax)
    print("Net Salary:",netsalary)
salaryslip("Louise",600)
salaryslip("George",8000)