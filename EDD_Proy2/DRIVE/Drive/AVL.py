class NodoAVL:
	def __init__(self,nombre):
		self.left = None
		self.right = None
		self.nombre = nombre

	def __str__(self):
		return "%s" % self.nombre

class ArbolAVL:
	def __init__(self):
		self.nodo = None
		self.altura = -1
		self.balance = 0

	def insertar(self, nombre):
		n=NodoAVL(nombre)
		aux = ASCII(nombre,1)
		num = ASCII(self.nodo.nombre,1)
		for n in range(2,len(nombre)):
			if self.nodo == None:
				self.nodo = n
				self.nodo.left = ArbolAVL()
				self.nodo.right = ArbolAVL()
				num = ASCII(self.nodo.nombre,n)
				break
			elif aux < num:
				self.nodo.left.insertar(nombre)
				break
			elif aux > num:
				self.nodo.right.insertar(nombre)
				break
			elif aux == num:
				aux = ASCII(nombre,n)
				num = ASCII(self.nodo.nombre,n)
		self.balancear()

	def balancear(self):
		self.verAltura(recursive=False)
		self.verBalance(False)
		while self.balance < -1 or self.balance > 1:
			if self.balance > 1:
				if self.nodo.left.balance < 0:
					self.nodo.left.rotarIzq()
					self.verAltura()
					self.verBalance()
				self.rotarDer()
				self.verAltura()
				self.verBalance
			if self.balance < -1:
				if self.nodo.right.balance > 0:
					self.nodo.right.rotarDer()
					self.verAltura()
					self.verBalance
				self.rotarIzq()
				self.verAltura()
				self.verBalance()

	def verAltura(self, recursive=True):
		if self.nodo:
			if recursive:
				if self.nodo.left:
					self.nodo.left.verAltura()
				if self.nodo.right:
					self.nodo.right.verAltura()
			self.altura = 1 + max(self.nodo.left.altura, self.nodo.right.altura)
		else:
			self.altura = -1

	def verBalance(self, recursive=True):
		if self.node:
			if recursive:
				if self.nodo.left:
					self.nodo.left.verBalance()
				if self.nodo.right.verBalance()
			self.balance=self.nodo.left.altura - self.nodo.right.altura
		else:
			self.balance=0

	def rotarDer(self):
		nuevo = self.nodo.left.nodo
		nuevo2 = nuevo.right.nodo
		raiz = self.nodo

		self.nodo = nuevo
		raiz.left.nodo = nuevo2
		nuevo.right.nodo = raiz

	def rotarIzq(self):
		nuevo = self.nodo.right.nodo
		nuevo2 = nuevo.left.nodo
		raiz = self.nodo

		self.nodo = nuevo
		raiz.right.nodo=nuevo2
		nuevo.left.nodo = raiz 

	def eliminar(self, nombre):
		if self.nodo.nombre != None:
			aux = ASCII(nombre,1)
			num = ASCII(self.nodo.nombre,1)
			for n in range(2,len(nombre)):
				if self.nodo.nombre = nombre:
					if not self.nodo.left.nodo and not self.nodo.right.nodo:
						self.nodo = None
					elif not self.nodo.left.nodo:
						self.nodo = self.nodo.right.nodo
					elif not self.nodo.right.nodo:
						self.nodo=self.nodo.left.nodo 
					else:
						siguiente = self.nodo.right.nodo
						while siguiente and siguiente.left.nodo:
							siguiente = siguiente.left.nodo

						if siguiente:
							self.nodo.right.eliminar(siguente.nombre)
					aux = ASCII(nombre,1)
					num = ASCII(self.nodo.nombre,1)
				elif aux < num:
					self.nodo.left.eliminar(nombre)
					break
				elif aux > num:
					self.nodo.right.eliminar(nombre)
					break
				elif aux == num:
					aux = ASCII(nombre,n)
					num = ASCII(self.nodo.nombre,n)
				self.balancear()


	def ASCII(nombre, posi):
		letra = nombre[:posi]
		return ord(letra)

