class Pangram:
    def __init__(self):
        print("WELCOME!!!")
    def check(self,s):
        inp=list()
        s=s.lower()
        s=set(s)
        for i in s:
            if ord(i) in range(ord('a'),ord('z')+1):
                inp.append(i)
        if len(inp)==26:
            print("THE STRING IS PANGRAM")
        else:
            print("THE STRING IS NOT PANGRAM")
p=Pangram()
s=input("ENTER THE STRING TO CHECK WHETHER IT IS PANGRAM OR NOT:\n")
p.check(s)
