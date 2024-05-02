def convert_list_to_string(char_list):
    if len(char_list) != 5:
        return "This list doesn’t have the right size"
    result_string = ''.join(char_list)
    return "The string is: " + result_string
my_lst1 = ['h', 'e', 'l', 'l', 'o']
output = convert_list_to_string(my_lst1)
print(output)

my_lst2 = ['h', 'e', 'y']
output2 = convert_list_to_string(my_lst2)
print(output2)