
'''
while len(num) > 1:
    temp = 0
    i = 0
    num2 = ""
    while i <= len(num):
        temp = int(num[i]) + int(num[i+1])
        num2 = num2 + str(temp)
        i += 1
'''

user_num = input("Please enter a number: ")
num_list = []

for char in user_num:
    num_list.append(char)

# print(num_list)
print(num_list)
i = 0
new_num2 = []
new_num3 = []
for numbers in num_list:
    try:
        num = int(num_list[i]) + int(num_list[i+1])
        new_num2.append(str(num))
        i = i + 2
    except:
        new_num2.append(num_list[i])
        break

i=0
for numbers in new_num2:
    try:
        num = int(new_num2[i]) + int(new_num2[i + 1])
        new_num3.append(str(num))
        i = i + 1
    except:
        new_num3.append(new_num2[i])
        break

print(new_num2)
print(new_num3)
