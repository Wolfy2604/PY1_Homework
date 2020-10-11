import sys


def salary_calc(work_time, nominal_pay, bonus=0):
    salary = (work_time * nominal_pay) + bonus
    return salary


params = sys.argv[1:4]
params_num = [int(arg) for arg in params]

print(salary_calc(*params_num))
