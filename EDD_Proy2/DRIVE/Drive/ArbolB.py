class Bnodo:

	def __init__(self, clave):
		self.Ramas = [None, None, None, None, None]
		self.Claves = [clave, None, None, None]
		self.Cuentas = 0

	def __init__(self):
		self.Ramas = [None, None, None, None, None]
		self.Claves = [None, None, None, None]
		self.Cuentas = 0

class NodoPr:
	def __init__(self, val):
		self.nump = val

class ArbolB:
	def __init__(self):
		self.p = Bnodo()
		self.Xder = Bnodo()
		self.Xizq = Bnodo()
		self.X = None
		self.Xr = None
		self.salida = ""
		self.imps = ""
		self.EmpA = False
		self.Esta = False

	def Inserta(self, clave):
		self.Insertaa(clave, self.p)

	def Insertaa(self, clave, raiz):
		self.Empujar(clave,raiz)
		if self.EmpA:
			self.p = Bnodo()
			self.p.Cuentas = 1
			self.p.Claves[0] = self.X
			self.p.Ramas[0] = raiz
			self.p.Ramas[1] = self.Xr
		print "Insercion Completa de %s" %clave.nump

	def Empujar(self, clave, raiz):
		k=0
		self.Esta = True
		if self.Vacio(raiz):
			self.EmpA = True
			self.X = clave
			self.Xr = None
		else:
			k = self.BuscarNodo(clave, raiz)
			if self.Esta:
				print "No hay claves repetidas"
				self.EmpA = False
			else:
				self.Empujar(clave,raiz.Ramas[k])
				if self.EmpA:
					if raiz.Cuentas < 4:
						self.EmpA = False
						self.MeterHoja(self.X, raiz, k)
					else:
						self.EmpA = True
						self.DividirN(self.X, raiz, k)

	def MeterHoja(self, clave, raiz, k):
		i = raiz.Cuentas
		while i != k:
			raiz.Claves[i] = raiz.Claves[i-1]
			raiz.Ramas[i+1] = raiz.Ramas[i]
			i=i-1

		raiz.Claves[k] = clave
		raiz.Ramas[k+1] = self.Xr
		raiz.Cuentas = raiz.Cuentas = raiz.Cuentas + 1

	def DividirN(self, clave, raiz, k):
		pos = 0
		Posmda = 0
		if k <=2:
			Posmda = 2
		else:
			Posmda = 3
		Mder = Bnodo()
		pos = Posmda +1
		while pos != 5:
			Mder.Claves[(pos - Posmda) -1] = raiz.Claves[pos -1]
			Mder.Ramas[pos - Posmda] = raiz.Ramas[pos]
			pos = pos +1
		Mder.Cuentas = 4 -Posmda
		raiz.Cuentas = Posmda
		if k <=2:
			self.MeterHoja(clave, raiz, k)
		else:
			self.MeterHoja(clave, Mder, (k -Posmda))
		self.X = raiz.Claves[raiz.Cuentas - 1]
		raiz.Cuentas = raiz.Cuentas = raiz.Cuentas -1
		self.Xr = Mder

	def Eliminar(self, clave):
		if self.Vacio(self.p):
			print "No hay elementos"
		else:
			self.Eliminara(self.p, clave)

	def Eliminara(self, raiz, clave):
		try:
			self.EliminarRegistro(raiz, clave)
		except:
			self.Esta = False

		if self.Esta == False:
			print "No se encontro el elemento %s" %clave.nump
		else:
			if raiz.Cuentas == 0:
				raiz = raiz.Ramas[0]
			self.p = raiz
			print "Eliminacion completa de %s" %clave.nump

	def EliminarRegistro(self, raiz, c):
		pos = 0
		sucesor = None
		if self.Vacio(raiz):
			self.Esta = False
		else:
			pos = self.BuscarNodo(c,raiz)
			if self.Esta:
				if self.Vacio(raiz.Ramas[pos -1]):
					self.Quitar(raiz, pos)
				else:
					self.Sucesor(raiz, pos)
					self.EliminarRegistro(raiz.Ramas[pos], raiz.Claves[pos -1])
			else:
				self.EliminarRegistro(raiz.Ramas[pos], c)
				if raiz.Ramas[pos] != None and raiz.Ramas[pos].Cuentas < 2:
					self.Restablecer(raiz, pos)

	def Sucesor(self, raiz, k):
		q = raiz.Ramas[k]
		while not Vacio(q.Ramas[0]):
			q = q.Ramas[0]
		raiz.Claves[k-1] = q.Claves[0]

	def Combina(self, raiz, pos):
		j = None
		self.Xder = raiz.Ramas[pos]
		self.Xizq = raiz.Ramas[pos-1]
		self.Xizq.Cuentas = self.Xizq.Cuentas + 1
		self.Xizq.Claves[self.Xizq.Cuentas -1] = raiz.Claves[pos -1]
		self.Xizq.Ramas[self.Xizq.Cuentas] = self.Xder.Ramas[0]
		j=1
		while j != (self.Xder.Cuentas + 1):
			self.Xizq.Cuentas = self.Xizq.Cuentas + 1
			self.Xizq.Claves[self.Xizq.Cuentas - 1] = self.Xder.Claves[j-1]
			self.Ramas[self.Xizq.Cuentas] = self.Xder.Ramas[j]
			j = j + 1
		self.Quitar(raiz, pos)

	def MoverDer(self, raiz, pos):
		i = raiz.Ramas[pos].Cuentas
		while i != 0:
			raiz.Ramas[pos].Claves[i] = raiz.Ramas[pos].Claves[i-1]
			raiz.Ramas[pos].Ramas[i+1] = raiz.Ramas[pos].Ramas[i]
			i = i-1
		raiz.Ramas[pos].Cuentas = raiz.Ramas[pos].Cuentas + 1
		raiz.Ramas[pos].Ramas[1] = raiz.Ramas[pos].Ramas[0]
		raiz.Ramas[pos].Claves[0] = raiz.clave[pos -1]
		raiz.Claves[pos - 1] = raiz.Ramas[pos -1].Claves[raiz.Ramas[pos-1].Cuentas -1]
		raiz.Ramas[pos].Ramas = raiz.Ramas[pos-1].Ramas[rai.Ramas[pos-1].Cuentas]
		raiz.Ramas[pos-1].Cuentas = raiz.Ramas[pos-1].Cuentas -1

	def MoverIzq(self, raiz, pos):
		i = None
		raiz.Ramas[pos - 1].Cuentas = raiz.Ramas[pos - 1].Cuentas + 1
		raiz.Ramas[pos - 1].Claves[raiz.Ramas[pos - 1].Cuentas - 1] = raiz.Claves[pos - 1]
		raiz.Ramas[pos - 1].Ramas[raiz.Ramas[pos - 1].Cuentas] = raiz.Ramas[pos].Ramas[0]
		raiz.Claves[pos - 1] = raiz.Ramas[pos].Claves[0]
		raiz.Ramas[pos].Ramas[0] = raiz.Ramas[pos].Ramas[1]
		raiz.Ramas[pos].Cuentas = raiz.Ramas[pos].Cuentas - 1
		i = 1
		while i != (raiz.Ramas[pos].Cuentas + 1):
			raiz.Ramas[pos].Claves[i - 1] = raiz.Ramas[pos].Claves[i]
			raiz.Ramas[pos].Ramas[i] = raiz.Ramas[pos].Ramas[i + 1]
			i = i+1

	def Quitar(self, raiz, pos):
		j = pos +1
		while j != (raiz.Cuentas +1):
			raiz.Claves[j-2] = raiz.Claves[j-1]
			raiz.Ramas[j-1] = raiz.Ramas[j]
			j = j+1
			
		raiz.Cuentas = raiz.Cuentas - 1

	def Restablecer(self, raiz, pos):
		if pos > 0:
			if raiz.Ramas[pos-1].Cuentas >2:
				self.MoverDer(raiz,pos)
			else:
				self.Combina(raiz,pos)
		elif raiz.Ramas[1].Cuentas > 2:
			self.MoverIzq(raiz,1)
		else:
			self.Combina(raiz,1)

	def Vacio(self, raiz):
		ret = None
		if raiz == None or raiz.Cuentas == 0:
			ret = True
		else:
			ret = False
		return ret 

	def BuscarNodo(self, clave, raiz):
		j = 0
		if clave.nump < raiz.Claves[0].nump:
			self.Esta = False
			j=0
		else:
			j=raiz.Cuentas
			while clave.nump < raiz.Claves[j-1].nump and j>1:
				j=j-1
			self.Esta = (clave.nump == raiz.Claves[j-1].nump)
		return j

	def Imprimir(self):
		




arbol = ArbolB()
f1 = NodoPr(54)
f2 = NodoPr(57)
f3 = NodoPr(58)
f4 = NodoPr(59)
f5 = NodoPr(50)
f6 = NodoPr(51)
f7 = NodoPr(56)
arbol.Inserta(f1)
arbol.Inserta(f2)
arbol.Inserta(f3)
arbol.Inserta(f4)
arbol.Inserta(f5)
arbol.Inserta(f6)
arbol.Inserta(f7)
arbol.Eliminar(f4)
		

