def Multiples_Sum():
    SumAll = 0
    for Number in range(0,1000):
        if Number%5 == 0 or Number%3 == 0 :
            SumAll += Number
    return print(f"sum Multiples from 0 to 1000 is {SumAll}")

if __name__ == '__main__':
    Multiples_Sum()
