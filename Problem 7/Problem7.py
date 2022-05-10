def No10001st_Prime():
    num =  0
    initNumber = 2
    primeNumberList=[]
    while True:
        
        for number2 in range(1,initNumber + 1):
            if initNumber % number2 == 0:
                num += 1
        if num <= 2 :
            primeNumberList.append(initNumber)
            print(len(primeNumberList) ,  primeNumberList[len(primeNumberList) - 1])
        if len(primeNumberList) == 10001:
            return print(primeNumberList[10000])
        initNumber += 1
        num = 0            

if __name__ == '__main__':
    No10001st_Prime()
