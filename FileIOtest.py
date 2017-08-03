if 1:
    file = open("test.txt","r")
    y = file.readlines()
    print(y)
    print(len(y))
    file.close()
    

else:
    n = {'benny':'2134','tongle':'4325'}
    x = "\n".join("%s\n%s" %(k,v) for k,v in n.items())
    print(x)

    file = open("test.txt","w")
    file.write(x)
    file.close()
