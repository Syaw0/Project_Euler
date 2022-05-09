def Smallest_Multiple():
    initNumber = 20
    while True:
        for number in range(2 , 21):
            res = initNumber / number 
            #print(f"{initNumber} / {number} = {res}")
            if str(res).split(".")[1] != "0":
                break
            elif number == 20 and res % 2 == 0:
                return print(initNumber)
        initNumber += 5
        
if __name__ == '__main__':
    Smallest_Multiple()
