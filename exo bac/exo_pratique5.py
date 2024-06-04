def max_indice(tab):
    a= tab[0]
    j=0
    for i in  range(1,len(tab)):
        if tab[i]>a:
            a= tab[i]
            j=i
    return (a,j)

tab = [1, 6, 2, 8, 3, 7]

print(max_indice(tab))