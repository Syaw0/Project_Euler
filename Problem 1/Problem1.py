def Multiples_Sum():
    SumAll = 0
    for Number in range(0,1000):
        if Number%5 == 0 or Number%3 == 0 :
            SumAll += Number
    return print(f"sum Multiples from 0 to 1000 is {SumAll}")
                                                                #i wnat write a function that take an initial range and end range number and number list and return Multiples of them ... hmmm...
if __name__ == '__main__':
    Multiples_Sum()
