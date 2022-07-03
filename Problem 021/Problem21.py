from audioop import mul


def Amicable_Numbers():
    number = 10001
    sum = 0
    sum2 = 0
    tsum = 0
    
    for i in range(1 , number):

        for y in range(1,i):
            if i % y == 0:
                sum+=y
        for y2 in range(1,sum):
            if sum % y2 == 0:
                sum2+=y2
        if(sum2 == i and sum2 != sum):
            tsum += sum2
            print(sum2 , i , sum)
        sum2= 0
        sum = 0

    return print(tsum)


if __name__ == '__main__':
    Amicable_Numbers()
