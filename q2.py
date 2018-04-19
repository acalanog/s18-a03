# Q2: How many full time employees are there?
import helper

data = helper.read_salaries()
job_term = helper.get_column(data,4)
full_time_employees = helper.count(job_term, "F")
print(full_time_employees)

#31,090 full_time_employees
