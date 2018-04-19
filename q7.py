# Q7: How common is the most common last name? Which is it?
import helper

data = helper.read_salaries()
with open("/Users/Babycake/Desktop/UChicago/Spring2018/ITP/s18-a03/salaries.csv", "r") as file:
    for line in file:
        item_list = line.strip().replace("\"","").split(',')
        item_list = [item.strip() for item in item_list]
names = helper.get_column(data, 1)   # get first names
counts = helper.counts(names)         # count them

print(helper.dict_max_value(counts)) # print maximum

#'Michael J', 268
