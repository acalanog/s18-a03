# Q4: How many employees in the police department?
import helper

data = helper.read_salaries()
police_only = helper.get_column(data,3)
police_count = helper.count(police_only,"POLICE")
print(police_count)

#13,414 employees in the police department
