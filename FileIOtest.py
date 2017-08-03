test = []
test1 = []
dictionary = {}

if 1:
    file = open("test.txt")
    y = file.read()
    print(y.split(","))
    test = y.split(",")
    for a in test:
        nani = a.split(":")
        test1.append(nani)
    print(test1)
        #dictionary.update({nani[0]:nani[1]})
    #print (dictionary)
    file.close()
    

    #test1 = [user for user in test[::2]]
    #test2 = [pasw for pasw in test[1::2]]
    
else:
    n = {'benny':'2134','tongle':'4325'}
    info = [['Johor','223456', 's@hos.com'],['Kedah','4325','out@ds.com']]
    roominfo = [['Fortunepark',-2],['SouthCity',654]]
    #x = ",".join("%s:%s" %(k,v) for k,v in n.items())
    temp = []
    for a in info:
        temp.append(":".join(a))
    x = ",".join(temp)
    print(x)
    file = open("test.txt","w")
    file.write(x)
    file.close()
