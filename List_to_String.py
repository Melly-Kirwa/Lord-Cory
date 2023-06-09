"""Write a function that takes a list value as argument and returns a string with all the items separated
by a comma and a space, with 'and' inserted before the last item. The program should be able to work with
any list value passed to it"""
#my_list = ["eggs", "banana", "oranges", "avocado"]
def list_to_string(my_list):
    my_str = ''
    for i in range(len(my_list)):
        my_str += my_list[i]
        if i != len(my_list) - 1:
            my_str += ', '
        if i == len(my_list) - 2:
            my_str += "and "


    print(my_str)


#list_to_string(['biy', 'ben', 'box', 'bux'])
#list_to_string(['3', '4', '5', '7'])
