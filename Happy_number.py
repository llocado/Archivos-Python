class Solution(object):

    def isHappy(self, n):
        L=[]
        T=[]
        valor=0
        while n not in L:
            L.append(n)       
            for i in str(n):
                T.append(int(i))
                #print(T)
            for i in T:
                valor+=i**2
                #print(valor)
            if valor==1:
                print("It's a Happy number!!")
                return True
            else:
                n=valor
                valor=0
                T=[]
                print(n)
        print("it's not a Happy number :(")
        return(False)
#z=Solution()
#z.isHappy(21)

class Solution2(object):        #version mejorada de happy number
    '''Si la suma de los cuadrados de los digistos del numero resulta en 1, es un happy number, de lo contrario, en algun momento 
    su resultado sera 4, siendo de estonces un unhappy number (que no es happy)'''
    def isHappy2(self,n):
        suma=0
        rem=0
        while n>0:
            rem=n%10
            suma=suma+rem**2
            n=n//10
        if suma==1:
            print("It's a Happy number :)")
            return(True)
        elif suma==4:
            print("It's not a Happy number")
            return(False)
        else:
            self.isHappy2(suma)
x=Solution2()
x.isHappy2(20)
