from audioop import mul


def Factorial_Digit_Sum():
    number = 100 
    multiple = 1
    tSum = 0
    for num in range(number , 0 , -1):
        multiple *= num
    for num in str(multiple):
        tSum += int(num)
    return print(tSum)


if __name__ == '__main__':
    Factorial_Digit_Sum()
