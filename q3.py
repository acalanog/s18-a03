# Q3: How many part-time employees are there?
import helper

data = helper.read_salaries()
job_term = helper.get_column(data,4)
part_time_employees = helper.count(job_term, "P")
print(part_time_employees)

#2,093 part_time_employees
