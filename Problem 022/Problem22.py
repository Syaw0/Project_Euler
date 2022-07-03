def Names_Scores():
    totalSum = 0
    sumword = 0
    wordsscore = {"A":1 , "B":2 , "C":3 , "D":4 , "E":5 , "F":6 , "G":7, "H":8 , "I":9 ,"J":10 , "K":11 , "L":12 , "M":13 , "N":14 , "O":15 , "P":16 , "Q":17 , "R":18 , "S":19 , "T":20 , "U":21 , "V":22,"W":23 , "X":24 , "Y":25, "Z":26}
    file = open("/home/siavash/Project/Project_Euler/Problem 022/names.txt" , "r")
    words = file.read()
    list = words.split('\"')
    list = sorted("".join(list).split(","))
    for i in range(0,len(list)):
        for i2 in list[i]:
            sumword += wordsscore[i2]
        tsum =  sumword*(i+1)
        totalSum += tsum
        sumword = 0
    file.close()
    return print(totalSum)


if __name__ == '__main__':
    Names_Scores()