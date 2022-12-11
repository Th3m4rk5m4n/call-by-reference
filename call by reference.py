# call by reference
def add_more(list):
    list.append(50)
    print("inside function",list)

# DRIVE's code

mylist = [10,20,30,40]

add_more(mylist)
print("outside function",mylist)
