def contar(x):
    conjunto=set(x)
    lista=list(x)
    tabla={}
    for i in conjunto:
        tabla[i]=lista.count(i)
    return tabla
print(contar("aaabbc"))