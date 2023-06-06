def DCP1(numbers = [10, 15, 3, 7], k = 17):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            print(str(numbers[i]) + " + " + str(numbers[j]))
            if(k == (numbers[i] + numbers[j])):
                return True
    return False