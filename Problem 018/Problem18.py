def Maximum_Path_Sum():
    Num = """75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    Num = Num.split(" ")
    rows = 1
    le = 0
    triangle = []
    number = 1
    node = 1
    for num in range(1,len(Num)):
        rows += num
        if rows >= len(Num):
            rows = num
            break
    rows2 = rows
    for num in range(1,rows+1):
        le = num-1+le
        triangle.append(Num[le : le+num])
    rows={}
    for row in triangle:
        rows[f"row{number}"]={}
        for numinrow in row:
            rows[f"row{number}"][node]={"value":numinrow , "index":row.index(numinrow) , "preValue":numinrow , "isFirst":True}
            node+=1
        if number != 1:
            for nums in rows[f"row{number-1}"]:
                for num in rows[f"row{number}"]:
                    preIndex = rows[f"row{number-1}"][nums]["index"]
                    nextIndex = rows[f"row{number}"][num]["index"]
                    if nextIndex == preIndex or nextIndex== preIndex+1 :
                        if rows[f"row{number}"][num]["isFirst"] :
                            # print("PRE",rows[f"row{number}"][num]["value"])
                            x = int(rows[f"row{number}"][num]["value"]) + int(rows[f"row{number-1}"][nums]["value"])
                            rows[f"row{number}"][num]["value"] = x
                            rows[f"row{number}"][num]["isFirst"] = False 
                            # print("nex",rows[f"row{number}"][num]["value"])
                            # print("its first")
                        else:
                            x = int(rows[f"row{number}"][num]["preValue"]) + int(rows[f"row{number-1}"][nums]["value"])
                            if x > int(rows[f"row{number}"][num]["value"] ) :
                                rows[f"row{number}"][num]["value"] = x
        number+=1

    lis = []
    for num in rows[f"row{rows2}"]:
        lis.append(int(rows[f"row{rows2}"][num]["value"]))
    
    return print(max(lis))

if __name__ == '__main__':
    Maximum_Path_Sum()
