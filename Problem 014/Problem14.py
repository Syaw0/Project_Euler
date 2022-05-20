from mimetypes import init
from re import L


def Longest_Collatz_Sequence():
    initnum = 100
    flist = []
    dic = {}
    
    for number in range(1000000 , 0 , -1):
        res = number 
        while True:
            if res%2 == 0 :
                res = res / 2;
            else:
                res = res * 3  + 1
            flist.append(res)
            if res == 1:
                break
        dic[number] = len(flist)
        flist = []
    for number in dic:
        print(dic[number]  , max(dic.values()))
        print(number)
        if dic[number] == max(dic.values()) :
            return print(number)
    

if __name__ == '__main__':
    Longest_Collatz_Sequence()
