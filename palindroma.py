def palindroma(palabra):
    lista=list(palabra)
    if len(palabra)%2==0:
            return("La palabra no es palindroma")
    else:
            for i in range(0,len(lista)):
                    if lista[i]!=lista[-i-1]:
                            return("la palabra no es palindroma")
            return("la palabra si es palindroma")

print(palindroma("reconocer"))