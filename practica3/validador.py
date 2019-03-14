
class Validador():
	alfabeto=['a','b','c'];
	pertenencia=1;

	def __init__(self):
		pass;

	def validarPalabraenAlfabeto(self,w):
		valida=1;
		for i in range (len(w)):
			if w[i] not in self.alfabeto:
				valida=0;
				pertenencia=0;
				break;
		return valida;

	def procesarPalabra(self,w):
		if self.validarPalabraenAlfabeto(w):
			return (w);
		else:
			return ("LA PALABRA '"+w+"' NO PERTENECE AL ALFABETO");

	def booleanoDePertenencia(self):
		return self.pertenencia;
