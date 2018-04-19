# Q5: How many detectives?
import helper

data = helper.read_salaries()
detective_only = helper.get_column(data,2)
detective_count = helper.count(detective_only,"POLICE OFFICER (ASSIGNED AS DETECTIVE)")
print(detective_count)

#989 detectives 
