phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
L=[]
L.append(plist[1])
L.append(plist[2])
L.append(plist[5])
L.append(plist[4])
L.append(plist[7])
L.append(plist[6])
print(L)
phrase2=""                  #Este es mi codigo
for i in L:
    phrase2=phrase2+i
print(phrase2)

#codigo del libro es el siguiente:

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()         #removes the las for values of the list (nic!)

plist.pop(0)            #takes out the "D"

plist.remove("'")       #takes out the "'"

plist.extend([plist.pop(), plist.pop()]) #swaps the pa to ap

plist.insert(2, plist.pop(3))   #moves the space along with the t

new_phrase = ''.join(plist)     #transforms the list into a new string

print(new_phrase)

phrase2 = "Don't panic!"        #same code but using the square bracket notation
plist2= list(phrase2)
print(phrase2)
print(plist2)
new_phrase2=''.join(plist2[1:3])
new_phrase2=new_phrase2+''.join([plist2[5],plist2[4],plist2[7],plist2[6]])
print("new_phrase2 is: "+str(new_phrase2))


