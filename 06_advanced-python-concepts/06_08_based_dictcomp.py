# Write a dictionary comprehension that maps each integer
# between `0` and `999` to a list of the digits that represents
# that integer in base 10. That is, your output should be:
#
# {0: [0], 1: [1], 2: [2], 3: [3], ...,
# 10: [1, 0], 11: [1, 1], 12: [1, 2], ...,
# 999: [9, 9, 9]}
#
# CHALLENGE: Write another dictionary comprehension that works the same
# but for base 2 (binary)! The output values should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1], ...,
# 7: [1, 1, 1], 8: [1, 0, 0, 0], 9: [1, 0, 0, 1], ...,
# 999: [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]}



#########Base10###########

###With For Loop########
# base_10 = {}
# for num in range(0, 1000):
#     base_10[num] = [int(x) for x in str(num)]
# print(base_10)


###With Dict Comprehention######
# base_10 = {num:[int(x) for x in str(num)] for num in range(0, 1000)}
# print(base_10)


#To print integer into a number separate by comma in a list
# number = "1234"
# res = []
# for x in number:
#     res.append(int(x))
#     print(res)

############Base2##############


###With For Loop#####
# base_2 = {}
# for num in range(0, 1000):
#     binary = bin(num).split("0b")[1]
#     binary_list = [int(item)for item in str(binary)]
#     print(binary_list)
#     base_2[num] = binary_list
# print(base_2)

    


###With Dict Comprehention####
base_2 = {num:[int(item)for item in str(bin(num).split("0b")[1])] for num in range(0, 1000)}
print(base_2)


###how to get binery from base10##########
# number = 5
# x = bin(number).split("0b")[1]
# print(x)










