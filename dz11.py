for i in range (1 , 1000):
    x = bin(i)[2:]
    x = str(x)
    for j in range(len(x)):
        if x.count("1") > x.count("0"): 
            x += "1"
        if x.count("1") < x.count("0"):
            x += "0"
    y = int(x , 2)
    if int(y) > 100:
        print(y)
        break 

