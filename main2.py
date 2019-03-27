def additive_persistence(num, counter, new_num):
    for each_digit in str(num):
        new_num += int(each_digit)
    counter += 1
    if new_num > 9:
        print("New Function Call")
        additive_persistence(new_num, counter, 0)
    else:
        print("Additive persistence:  " + str(counter))
        return 0


# new_num = 0
success = 0
counter = 0
user_num = 0
while success == 0:
    try:
        user_num = int(input("please input your number: "))
        success = 1
    except ValueError:
        print("Must be a number yo")

additive_persistence(user_num, counter, 0)
