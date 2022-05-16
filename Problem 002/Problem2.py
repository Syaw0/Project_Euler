def Even_Fibonacci_Sum():
    sum = 0
    index = 0
    list = [1,2]
    while True:
        NextNumber = list[index] + list[index + 1]
        if(NextNumber >= 4000000):
            for number in list:
                if number % 2 == 0 :
                    sum += number
            return print(sum)
        else:
            list.append(NextNumber)
            index += 1
            
if __name__ == '__main__':
    Even_Fibonacci_Sum()
