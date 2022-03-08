# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.



# Write your code below here

##sorts the numbers##

##     - stores the numbers in tuples of two in a new list
##     - prints each tuple
## If the list has an odd number of items,
## add the last item to a tuple together with the number `0`.

import sys
from resources import randlist
# print(randlist)

randlist.sort()
print(f"This is sorted list{randlist}.")

# print(f"length of randlist is {len(randlist)}")

new_list = []
for index in range(0, len(randlist), 2) :
    new_list.append([index, index+1])
    index += 2
# print(new_list)
# print(f"new_list length is {len(new_list)}")

counter = 0
new_list_num = []
for index, value in enumerate(randlist):
    for i,x in enumerate(new_list):
        # print(f"length of new_list_num is {len(new_list_num)}")
        following = len(new_list_num)+1 if len(new_list_num)+1 < len(new_list) else None
        if following == None:
            if counter == len(new_list):
                tuple_list = [tuple(x) for x in new_list_num]
                print(tuple_list)
                sys.exit()
            elif counter < len(new_list):
                if len(randlist) % 2 == 0:
                    new_list_num.append([randlist[index], randlist[index+1]])
                    tuple_list = [tuple(x) for x in new_list_num]
                    print(tuple_list)
                    sys.exit()
                else:    
                    new_list_num.append([randlist[index], 0])
                    counter += 1
                    tuple_list = [tuple(x) for x in new_list_num]
                    print(tuple_list)
                    sys.exit()   
            else:
                new_list_num.append([randlist[index], randlist[index+1]])
                tuple_list = [tuple(x) for x in new_list_num]
                print(tuple_list)
                sys.exit()   
        else:
            new_list_num.append([randlist[index],randlist[index+1]]) 
            counter += 1
        index+=2
        continue  
    print(new_list_num)


    




