import ArbolGarrafas as ar


def check(estado, historico, nodos):
    if estado not in historico and estado not in nodos:
        return True
    else:
        return False


def transpasar(garrafaUno, garrafaDos, valorOldUno, valorOldDos):
    if (garrafaUno.capacidad < garrafaUno.maxCap and garrafaDos.capacidad > 0):
        res = valorOldUno + valorOldDos
        if res >= garrafaUno.maxCap:
            if valorOldDos > valorOldUno:
                garrafaUno.llenar()
                garrafaDos.setCapacidad(res - garrafaUno.maxCap)
            elif (valorOldDos == valorOldUno):
                garrafaUno.llenar()
                garrafaDos.setCapacidad(res - garrafaUno.maxCap)
            else:
                garrafaUno.llenar()
                garrafaDos.setCapacidad(valorOldUno - valorOldDos)
        else:
            garrafaUno.setCapacidad(res)
            garrafaDos.setCapacidad(0)

    return [garrafaUno.getCapacidad(), garrafaDos.getCapacidad()]


a = ar.Garrafa(0, 5)
b = ar.Garrafa(0, 3)

nodo = ar.ArbolGarrafas(None, [a.capacidad, b.capacidad])
historico = []
nodos = [nodo]



while (nodo.getEstado()[0] + nodo.getEstado()[1] != 7) and len(nodos) > 0:
    nodo = nodos[0]
    nodosHijos = []
    g5 = nodos[0].getEstado()[0]
    g3 = nodos[0].getEstado()[1]
    a.setCapacidad(nodos[0].getEstado()[0])
    b.setCapacidad(nodos[0].getEstado()[1])
    # print(nodos)
    if a.capacidad != 0:
        a.vaciar()
        if check([a.getCapacidad(), b.getCapacidad()], historico, nodos):
            nodos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
            nodosHijos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
        a.capacidad = g5
        b.capacidad = g3
    if b.capacidad != 0:
        b.vaciar()
        if check([a.getCapacidad(), b.getCapacidad()], historico, nodos):
            nodos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
            nodosHijos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
        a.capacidad = g5
        b.capacidad = g3
    if a.capacidad != 0 and b.capacidad < b.maxCap:
        result = transpasar(b, a, b.capacidad, a.capacidad)
        a.setCapacidad(result[1])
        b.setCapacidad(result[0])
        if check([a.getCapacidad(), b.getCapacidad()], historico, nodos):
            nodos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
            nodosHijos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
        a.capacidad = g5
        b.capacidad = g3
    if b.capacidad != 0 and a.capacidad < a.maxCap:
        result = transpasar(a, b, a.capacidad, b.capacidad)
        b.setCapacidad(result[1])
        a.setCapacidad(result[0])
        if check([a.getCapacidad(), b.getCapacidad()], historico, nodos):
            nodos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
            nodosHijos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
        a.capacidad = g5
        b.capacidad = g3
    if a.capacidad == 0:
        a.llenar()
        if check([a.getCapacidad(), b.getCapacidad()], historico, nodos):
            nodos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
            nodosHijos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
        a.capacidad = g5
        b.capacidad = g3
    if b.capacidad == 0:
        b.llenar()
        if check([a.getCapacidad(), b.getCapacidad()], historico, nodos):
            nodos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
            nodosHijos.append(ar.ArbolGarrafas(nodo, [a.capacidad, b.capacidad]))
        a.capacidad = g5
        b.capacidad = g3
    historico.append([g5, g3])
    nodos.pop(0)

nodo.mostrar()
