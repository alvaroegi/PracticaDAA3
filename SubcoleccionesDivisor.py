contador = 0

def genera_subconjuntos(i,sol,elementos,size):
    if sum(sol[:i]) > size: #PODA
        return
    if i==len(elementos):
        esDivisor(sol,elementos,size)
    else:
        for k in range(0,2):
            sol[i] = k
            genera_subconjuntos(i+1,sol,elementos,size)

def genera_subconjuntos_wrapper(elementos,size):
    sol = [None] * (len(elementos))
    genera_subconjuntos(0,sol,elementos,size)

def esDivisor(sol,elementos,size):
    global contador
    aux = 0
    esDivisible = True
    subconjunto = []
    for i in range(len(sol)):
        if sol[i]==1 :
            subconjunto.append(elementos[i])
    if(len(subconjunto) == size):
        subconjunto.sort()
        for j in range(1,len(subconjunto)):
            if (subconjunto[j] % subconjunto[0] != 0):
                esDivisible = False
                break
        if size == 1:
            esDivisible = True
    if esDivisible and len(subconjunto) == size:
        contador = contador + 1

def casoDePrueba():
    global contador
    try:
        n = int(input())
        if (n >= 1 and n <= 100):
            numeros = input().split()
            lista = list(map(int, numeros))
            if(len(lista) == n):
                    m = int(input())
                    if (m >=1 and m <= n):
                        genera_subconjuntos_wrapper(lista,m)
                        print(contador)
                        contador = 0
                        return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass