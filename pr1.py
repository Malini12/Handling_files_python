class codekata:
    def __init__(self):
        pass
    def easy(self):
        fh1=open("C:\\Users\\Malini_P_M\\Desktop\\easy.txt","r")
        ea=fh1.read()
        print(ea)
        print("Type display for viewing Testcases")
        a=input()
        if(a=="display"):
            fh2=open("C:\\Users\\Malini_P_M\\Desktop\\testeasy.txt","r")
            eb=fh2.read()
            print(eb)
        else:
            print("enter display")
    def medium(self):
        fh3=open("C:\\Users\\Malini_P_M\\Desktop\\medium.txt","r")
        ma=fh3.read()
        print(ma)
        print("Type display for viewing Testcase")
        b=input()
        if(b=="display"):
            fh4=open("C:\\Users\\Malini_P_M\\Desktop\\testmedium.txt","r")
            mb=fh4.read()
            print(mb)
        else:
            print("enter display")
    def hard(self):
        fh5=open("C:\\Users\\Malini_P_M\\Desktop\\hard.txt","r")
        ha=fh5.read()
        print(ha)
        print("Type display for viewing Testcase")
        c=input()
        if(c=="display"):
            fh6=open("C:\\Users\\Malini_P_M\\Desktop\\testhard.txt","r")
            hb=fh6.read()
            print(hb)
        else:
            print("enter display")

obj=codekata()
print('Welcome to codekata \n enter your options \n 1.Easy \n2.medium\n 3.hard')
option=int(input())
while(1):
    if(option==1):
        obj.easy()
        break
    if(option==2):
        obj.medium()
        break
    if(option==3):
        obj.hard()
        break
