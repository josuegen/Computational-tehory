class Analizador():
	estado=0;
	def __init__ (self):
		pass;

	def devuelveUltimoEstado(self):
		return self.estado;

	def analizaPalabra(self,palabra):
		self.estado=0;
		valida=0;
		i=0;
		while (i in range(len(palabra))):
			if(self.estado==0):
				if(palabra[i]=="a"):
					self.estado=1;
				if(palabra[i]=="b"):
					self.estado=5;
				if(palabra[i]=="c"):
					self.estado=3;
			elif(self.estado==1):
				if(palabra[i]=="a"):
					self.estado=1;
				if(palabra[i]=="b"):
					self.estado=2;
				if(palabra[i]=="c"):
					self.estado=6;
			elif(self.estado==2):
				if(palabra[i]=="a"):
					self.estado=6;
				elif(palabra[i]=="b"):
					self.estado=6;
				elif(palabra[i]=="c"):
					self.estado=6;
			elif(self.estado==3):
				if(palabra[i]=="a"):
					self.estado=6;
				elif(palabra[i]=="b"):
					self.estado=4;
				elif(palabra[i]=="c"):
					self.estado=3;
			elif(self.estado==4):
				if(palabra[i]=="a"):
					self.estado=6;
				elif(palabra[i]=="b"):
					self.estado=4;
				elif(palabra[i]=="c"):
					self.estado=6;
			elif(self.estado==5):
				if(palabra[i]=="a"):
					self.estado=6;
				elif(palabra[i]=="b"):
					self.estado=5;
				elif(palabra[i]=="c"):
					self.estado=6;
			elif(self.estado==6):
				if(palabra[i]=="a"):
					self.estado=6;
				elif(palabra[i]=="b"):
					self.estado=6;
				elif(palabra[i]=="c"):
					self.estado=6;
			i=i+1;
		if(self.estado==2) or (self.estado==4) or (self.estado==5):
			valida=1;
		return valida;

