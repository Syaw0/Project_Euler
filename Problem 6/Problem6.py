def Sum_Square_Difference():
    SumSquare = 0
    AllSumSquare = 0
    for number in range(1,101):
        AllSumSquare += number
        SumSquare += number ** 2
    AllSumSquare = AllSumSquare ** 2
    return print(AllSumSquare - SumSquare)

        
if __name__ == '__main__':
    Sum_Square_Difference()
