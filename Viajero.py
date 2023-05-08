import math

def calculaDistancia(ciudad1, ciudad2):
    return pow(pow(ciudad1[0] - ciudad2[0], 2) + pow(ciudad1[1] - ciudad2[1],2), 1 / 2)


def matrizDistancias(ciudades):
    sol = []
    for l in range(len(ciudades)):
        fila = [None] * len(ciudades)
        sol.append(fila)

    for i in range(len(ciudades)):
        for j in range(len(ciudades)):
            if i <= j:
                if i == j:
                    sol[i][j] = 0
                else:
                    dist = calculaDistancia(ciudades[i], ciudades[j])
                    sol[i][j] = dist
                    sol[j][i] = dist
    return sol

def viajero_wrapper(grafo):
    num_nodes = len(grafo)
    permuta = [None] * (num_nodes + 1)
    permuta[0] = permuta[-1] = 0  # Empiece y acabe en el 0 (ciclo hamiltoniano)
    visitados = [False] * num_nodes
    ciclo = []
    #min_cost igual a infinito para siempre coger el camino con menor valor desde el principio
    min_cost = math.inf

    def viajero(posicion, coste_actual):
        #Introducimos la función viajero dentro de wrapper con min_cost en nonlocal, para que el valor de min_cost sea siempre el mismo.
        #Si lo separásemos como hemos hecho siempre (las dos funciones), este min_cost sería distinto en las dos funciones, luego daría error
        #(Habría que pasar un puntero por referencia, como solución alternativa a esta)
        nonlocal min_cost

        #Podamos las permutaciones que ya se pasen del mínimo acumulado
        if coste_actual > min_cost:
            return

        if posicion == num_nodes:
            if grafo[permuta[posicion - 1]][permuta[posicion]] != 0:
                if coste_actual + grafo[permuta[posicion - 1]][permuta[posicion]] < min_cost:
                    min_cost = coste_actual + grafo[permuta[posicion - 1]][permuta[posicion]]
                    ciclo.clear()
                    for j in range(num_nodes):
                        ciclo.append(permuta[j])

            return

        for node in range(1, num_nodes):
            if not visitados[node] and grafo[permuta[posicion - 1]][node] != 0:
                visitados[node] = True
                permuta[posicion] = node

                viajero(posicion + 1, coste_actual + grafo[permuta[posicion - 1]][node])

                visitados[node] = False

    visitados[0] = True
    viajero(1, 0)

    return ciclo, min_cost


def casodePrueba():
    try:
        n = int(input())
        cities = [None] * n
        for i in range(0, n):
            xy = list(map(float, input().split()))
            tupla = tuple(xy)
            cities[i] = tupla
        cycles, min_cost = viajero_wrapper(matrizDistancias(cities))
        print('%.4f' % min_cost)
        for p in range(len(cycles)):
            print(cycles[p],end=' ')
        print()
        return True
    except:
        return False


if __name__ == "__main__":
      while casodePrueba():
        pass




