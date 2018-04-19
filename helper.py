# A.1: Parse the included salaries.csv file.
# Your parser should split each line on ',' and return a nested list
# where each element is itself a list of fields.
# Additionally you should ignore/remove the first (header) line.
def read_salaries() :
    top_list = []
    item_list = []
    mod_line = []
    # open function will call the file to read it with "r"
    with open("/Users/Babycake/Desktop/UChicago/Spring2018/ITP/s18-a03/salaries.csv", "r") as file:
        for line in file:
            # removes the double quotes and dollar sign in each line column
            item_list = line.strip().replace("\"","").replace("$","").split(',')
            # goes through the while loop and removes the white spaces
            item_list = [item.strip() for item in item_list]
            top_list.append(item_list)
    # removes the header
    del top_list[0]
    # output will be without the header
    return top_list

data = read_salaries()

# A.2: Given a 2d list data and an integer column_index
# return a 1d list of values for that column.
def get_column(data, column_index):
        column_list = []
        # if the length of column_index is greater or equal to than the selected
        # list, then an error should pop up
        # if the length of column index is less than the selected list, then a
        # new list will be made containing only the selected values of the selected column
        if (column_index >= len(data[0])):
            print ("Error: column selected does not exist.")
            return 0.0
        for line in data:
            column_list.append(line[column_index])

        return column_list

# A.3: Given a 1d list of `values` (e.g. the result of get_column),
# return the number of elements that are equal to `search_value`.
def count(value, search_value):
    if (len(value) == 0):
        print ("Search list is empty")
        return 0.0
    if (search_value == "" or search_value is None):
        print ("Search value is empty.")
        return 0.0
    match_count = 0
    for items in value:
        if items == search_value:
            match_count += 1
    return match_count

# A.4: Given a 1d list values (e.g. the result of get_column),
# return a dictionary of value-count pairs.
def counts(values):
    count_dict = dict()
    for item in values:
        count_dict[item] = count_dict.get(item,0) + 1
    return count_dict

# A.5: Given a dictionary d with numeric values, return a list [key, value] of two elements,
# where key is the the key in d with the largest value, and value is it's value.
def dict_max_value(d):
    if d is None:
        print ("dictionary is empty")
        return 0.0
    return max(d.items(), key = lambda x: x[1])

# A.6: Given a list of numbers use the built-in functions sum and len to return their mean.
def mean(num_list):
    if (len(num_list) == 0):
        print ("Error: num list cannot be empty")
        return 0.0
    list_sum = sum(num_list)
    list_count = len(num_list)
    return list_sum/list_count

# A.7: Given a list of numbers calculate the median.
def median(num_list):
    count = len(num_list)
    if (count < 1):
        return None;
    if count % 2 == 1:
        return sorted(num_list)[n//2]
    else:
        return sum(sorted(num_list)[count//2-1:count//2+1])/2.0
