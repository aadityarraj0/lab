my_list = []

my_list.insert(0, 10)
my_list.insert(1, 20)
print("After inserting elements:", my_list)

my_list.remove(10)
print("After removing 10:", my_list)

my_list.append(30)
print("After appending 30:", my_list)

print("Length of the list:", len(my_list))

popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After popping:", my_list)

my_list.clear()
print("After clearing the list:", my_list)
