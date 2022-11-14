class ArbolGarrafas:

    def __init__(self):
        self.estado = None
        self.hijos = []

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getHijos(self):
        return self.hijos

    def setHijos(self, hijos):
        self.hijos = hijos

    def mostrar(self):
        print(self.estado)
        if len(self.getHijos()) > 0:
            for i in self.getHijos():
                i.mostrar()


a = ArbolGarrafas()
b = ArbolGarrafas()
c = ArbolGarrafas()
d = ArbolGarrafas()
e = ArbolGarrafas()
f = ArbolGarrafas()
g = ArbolGarrafas()
h = ArbolGarrafas()
j = ArbolGarrafas()
a.setEstado(5)
b.setEstado(3)
g.setEstado(6)
a.setHijos([b, g])
c.setEstado(1)
d.setEstado(7)
e.setEstado(9)
f.setEstado(11)
h.setEstado(8)
j.setEstado(12)
b.setHijos([c, d, e, f])
g.setHijos([h, j])
a.mostrar()