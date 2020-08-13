def(palabra):
        lista=list(palabra)
        if len(palabra)%2==0:
                return("La palabra no es palindroma")
        else:
                for i in lista:
                        if lista[i]!=lista[-i]:
                                return("la palabra no es palindroma")
                return("la palabra si es palindroma")