
def Highly_Divisible_Triangular_Number():
    num = 2
    initNum = 1
    secNum = 0
    divnum = 0
    # i think last number of this digit are zero to have more divs...
    while True:
        secNum = initNum + num
        print(secNum  , num)
        if str(secNum)[len(str(secNum)) - 1 ] == "0":
            for number in range(2,secNum + 1 ):
                if secNum % number == 0 :
                    divnum += 1
                    print(f"{secNum}  : {number}  ,,  {divnum} , and this is number : {num}")
        if divnum >= 500:
            return print(f"this number have 500 divition : {secNum}")
        initNum = secNum
        num += 1
        divnum = 0    





if __name__ == '__main__':
    Highly_Divisible_Triangular_Number()
