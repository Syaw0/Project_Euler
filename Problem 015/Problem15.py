

def facteriol(number):
    mul = 1
    for num in range(1,number+1):
        mul *= num
    return mul

def Lattice_Paths():
    #grid 20*20
    return  print((facteriol(40)) / (facteriol(20) *facteriol(20)))


if __name__ == '__main__':
    Lattice_Paths()
