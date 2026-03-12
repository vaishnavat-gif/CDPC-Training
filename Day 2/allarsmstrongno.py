for i in range(1, 10000):
    no = i
    temp = no
    sum = 0
    count = 0

    # count digits
    while no > 0:
        no = no // 10
        count = count + 1

    no = temp   

    while no > 0:
        digit = no % 10
        sum = sum + digit ** count
        no = no // 10

    if temp == sum:
        print(temp)
