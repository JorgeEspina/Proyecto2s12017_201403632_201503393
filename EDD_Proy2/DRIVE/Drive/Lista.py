from ArbolB import NodoPr
from ArbolB import ArbolB
from AVL import NodoAVL
from AVL import ArbolAVL

class NodoRaiz:
	def __init__(self):
		self.B = ArbolB()
		self.AVL = ArbolAVL()

class NodoLista:
	def __init__(self,usu,contra):
		self.siguiente = None
		self.anterior = None
		self.usu = usu
		self.contra = contra
		self.Raiz = NodoRaiz()

	def getUsu(self):
		return self.usu

	def setContra(self, contra):
		self.contra = contra

	def getContra(self):
		return self.contra

	def set

class Lista:
	def __init__(self):
		self.cabeza = None
		self.cola = None

	def vacia(self):
		if self.cabeza ==None:
			return True
		else:
			return False

	def insertar(self,usu,contra):
		temporal = NodoLista(usu,contra)
		if self.vacia() == True:
			self.cabeza = temporal
			self.cola = temporal
			print "se creo el usuario %s" %temporal.usu
			print "con contra %s" % temporal.contra
		else:
			temporal.anterior = self.cola
			self.cola.siguiente = temporal
			self.cola=temporal
			print "se creo el usuario %s" %temporal.usu
			print "con contra %s" % temporal.contra

	def listar(self):
		print("*********************")
		temporal = self.cabeza
		while temporal != None:
			print(temporal.getUsu())
			print(temporal.getContra())
			print("-<-<-<-<-<-<-<")
			temporal = temporal.siguiente
		print("**********************")

	def eliminar(self,usu):
		anterior = self.cabeza
		actual=self.cabeza
		while actual.siguiente !=None:
			anterior=actual
			actual=actual.siguiente
			if usu == actual.usu:
				temporal = actual.siguiente
				anterior.siguiente=actual.siguiente
				temporal.anterior = anterior
				print "se elimino el usu %s" %usu
			


listas = Lista()
listas.insertar("daniel","1234")
listas.insertar("majo","mana")
listas.insertar("jose","nodo")
listas.insertar("leon","bien")
listas.listar()
listas.eliminar("jose")
listas.listar()




