def isBalanced(x):
    x2=list(x)
    if x2.count("(")!=x2.count(")") or x2.count("[")!=x2.count("]") or x2.count("{")!=x2.count("}") :
        return False
    elif x2.count("(")==x2.count(")") and x2.count("[")==x2.count("]") and x2.count("{")==x2.count("}"):
        count1=0
        for i in x2:
            if i=="(" or i=="[" or i=="{":
                count+=1
            elif i=="(" or i=="]" or i=="}":
                count-=1
                if count==-1:
                    return False
        if count==0:
            return True
        else:
            return False

print(isBalanced("(()"))