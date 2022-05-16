def Largest_Prime_Factor():
    Number = 600851475143
    initNumber = 2
    while True:
        res = Number / initNumber
        if str(res).split(".")[1] != "0" :
            initNumber += 1
        else:
            Number = int(res)
            if int(res) == 1:
                return print(initNumber)
            initNumber += 1

            
if __name__ == '__main__':
    Largest_Prime_Factor()
