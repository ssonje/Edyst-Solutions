# cook your dish here
# slabs values
slabs = list(map(int,input().split()))

# percentage of each slab
tax_per = list(map(int,input().split()))

# rebate amount
rebate = int(input())

# tax payed by each employee
tax_employee = list(map(int,input().split()))

# tax ranges
tax_ranges = [0]
for i in range(len(slabs)-1):
    tax_ranges.append(int((slabs[i+1]-slabs[i]) * tax_per[i] / 100))

# salary ranges
salary_ranges = [slabs[0]]
for i in range(len(slabs)-1):
    salary_ranges.append((slabs[i+1]-slabs[i]))

# TASK :- Find the employee salary
sum_salary = 0
for i in range(len(tax_employee)):
    
    tax = tax_employee[i]
    flag = False

    for i in range(len(slabs)):
        if (tax_ranges[i]) <= tax:
            sum_salary += salary_ranges[i]
            tax -= tax_ranges[i]
        else:
            sum_salary += tax * 100 / tax_per[i-1]
            flag = True

    if flag == False:
         sum_salary += tax * 100 / tax_per[len(tax_per)-1]

    sum_salary += rebate   

print(int(sum_salary))
