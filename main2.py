number = 0
success = 0
additive_persistence = 0
while success == 0:
    try:
        number = int(input("please input your number: "))
        success = 1
    except ValueError:
        print("Must be a number yo")

while number > 9:
    if number > 99:
        # I thought this was pretty funny to try, oh well!
        number = int(str(number[0])) + int(str(number[1]))
    if number > 999:
        pass
    if number > 9999:
        pass
    if number > 99999:
        pass
    if number > 999999:
        pass
    if number > 9999999:
        pass

print("Additive persistence:  " + str(additive_persistence))
