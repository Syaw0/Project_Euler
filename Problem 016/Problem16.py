
def Power_Digit_Sum():
    number = 2**1000
    sum = 0
    for number in str(number):
        sum+= int(number)
    return print(sum)


if __name__ == '__main__':
    Power_Digit_Sum()
