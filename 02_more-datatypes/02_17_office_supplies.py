# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

# for x in office:
#     i = x["full_name"]
#     h = i.split(" ")


length_of_lastnames = [0]
lastname_list = [0]
firstname_list = [0]
item_list = [0]


for n in office:
    item = n["item"]
    i = n["full_name"].split(" ")
    lastname = i[1]
    firstname = i[0]
    c = len(lastname)
    if c > length_of_lastnames[-1] :
        length_of_lastnames.append(c)
        lastname_list.append(lastname)
        firstname_list.append(firstname)
        item_list.append(item)
    else:
        for i in range(len(length_of_lastnames)):
            if c <= length_of_lastnames[i]:
                lastname_list.insert(i, lastname)
                firstname_list.insert(i, firstname)
                item_list.insert(i, item)
                length_of_lastnames.insert(i, c)
                break

print(lastname_list)

for x in range(1, len(length_of_lastnames)):
    lastname = lastname_list[x]
    firstname = firstname_list[x]
    item = item_list[x]
    namelength = len(firstname) + len(lastname)
    # print(f"{lastname}, {firstname:<30} {item}")
    full_name = f"{lastname.upper()},{firstname}"
    print(f"{full_name:<30} {item}")


    # length_of_lastnames.sort()
    
    
# print(list_)




