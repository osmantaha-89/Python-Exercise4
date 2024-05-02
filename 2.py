def reorder_and_remove(my_lst):
 
  my_lst.remove(max(my_lst))
  my_lst.remove(min(my_lst))
  return my_lst

my_lst_1 = [6,2,7,4,3]
new_lst = reorder_and_remove(my_lst_1)
print("The new list is: ", (new_lst))

  
my_lst_2 = [6,6,3,2,4,5,5]
new_lst = reorder_and_remove(my_lst_2)
print("The new list is: ", (new_lst))



