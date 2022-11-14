class Garrafa:

    def __init__(self, capacidad, maxCap):
        self.capacidad = capacidad
        self.maxCap = maxCap

    def llenar(self):
        self.capacidad = self.maxCap

    def vaciar(self):
        self.capacidad = 0

    def getCapacidad(self):
        return self.capacidad

    def setCapacidad(self, cap):
        self.capacidad = cap

    def getMaxCap(self):
        return self.maxCap


class ArbolGarrafas:

    def __init__(self,padre, estado):
        self.padre = padre
        self.estado = estado
        self.hijos = []


    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getPadre(self):
        return self.padre

    def setPadre(self, padre):
        self.padre = padre

    def getHijos(self):
        return self.hijos

    def setHijos(self, hijos):
        self.hijos = hijos

    def mostrar(self):
        if (self.padre != None):
            print(f"{self.estado} y mi padre es {self.padre.estado}")
            self.padre.mostrar()
        else:
            print(f"{self.estado}")
        for n in self.hijos:
            n.mostrar()
