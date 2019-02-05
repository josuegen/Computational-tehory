
from numpy import *;
import os;
from colorama import *;
import sys;


#autor: Josué Velázquez Gen
#fecha: 04/Febrero/2019
#IPN ESCOM
#Profesor: Yosafat Moscoso

def limpiarPantalla():
	if(os.name=="windows"):
		os.system("cls");	
	else: 
		os.system("clear");
	print (chr(27)+"[1;95m"+"                               P R A C T I C A   1");
	print("");
	print("");
	print("");
	return;

def ingresarAlfabeto():
	alfabeto=[];
	simbolo="";
	limpiarPantalla();
	print("\033[1;33m"+"Ingrese los símbolos de su alfabeto(E), línea a línea");
	print("\033[1;33m"+"Longitud máxima del alfabeto(E) permitida (50)");
	print("\033[1;33m"+"Si ha terminado de ingresar los símbolos para (E) escriba 'fin' y presione enter");
	print(Style.RESET_ALL+"--> Alfabeto :")
	for i in range (50):
		simbolo=input(Style.RESET_ALL);
		if simbolo!="fin": 			
			if len(simbolo)==1: 			
				if simbolo not in alfabeto: 
					alfabeto.append(simbolo);
				else:
					print("\033[91m"+"¡¡ EL SÍMBOLO " +Style.RESET_ALL+"'"+simbolo+"'"+"\033[91m"+" YA EXISTE EN EL ALFABETO(E) !!");
			else	:
				print("\033[91m"+"¡¡ EL SÍMBOLO SOLO PUEDE SER DE LONGITUD (1) !!");
		else:
			if len(alfabeto)<=1:			
				print("\033[91m"+"¡¡ EL ALFABETO DEBE TENER AL MENOS (2) SIMBOLOS !!");
				print(Style.RESET_ALL+"--> Alfabeto :")
			else:
				break;
	return alfabeto;


def ingresarPalabras(E):
	alfabeto=E;
	pertenencia=1;
	palabras=[];
	limpiarPantalla();
	print("\033[1;33m"+"Tu alfabeto (E) es: ");
	print(alfabeto);
	print("\033[1;33m"+"Ahora ingrese dos palabras con símbolos pertenecientes a tu alfabeto (E)\n");
	print(Style.RESET_ALL+"--->  Palabra 1 (w1): ");
	w1=input();
	for i in range(len(w1)):
			if w1[i] not in alfabeto:
				print("\033[91m"+"La palabra (w1): '"+w1+" ' NO pertenece al alfabeto (E)");
				pertenencia=0;
				break;

	print(Style.RESET_ALL+"--->  Palabra 2 (w2): ");
	w2=input();
	for i in range(len(w2)):
		if w2[i] not in E:
			print("\033[91m"+"La palabra (w2): '"+w2+" ' NO pertenece al alfabeto (E)");
			pertenencia=0;
			break;
	palabras.append(w1);
	palabras.append(w2);
	if(pertenencia==1):
		menu(alfabeto,palabras);
	else:
		ingresarPalabras(alfabeto);
		
def longitudDeCadenas(palabras):
	print("");
	print("\033[1;33m"+" ------------------------------- ");
	print("\033[1;33m"+"|      LONGITUD DE CADENAS      |");
	print("\033[1;33m"+" ------------------------------- ");
	print("");
	print(Style.RESET_ALL+"|w1| ("+palabras[0]+") :"+str(len(palabras[0])));
	print(Style.RESET_ALL+"|w2| ("+palabras[1]+") :"+str(len(palabras[1])));
	return;

def preySufijosDeCadenas(palabras):
	prefijo="";
	sufijo="";
	longitud=0;
	print("");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("\033[1;33m"+"|      PREFIJOS Y SUFIJOS DE CADENAS      |");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("");
	print("\033[1;33m"+" ----  Prefijos w1 (* propios)   ----");
	for i in range (len(palabras[0])):
		prefijo=prefijo+palabras[0][i];
		if i == 0:
			print(Style.RESET_ALL+palabras[0][i]);
		elif i != (len(palabras[0])-1):
			print(Style.RESET_ALL+prefijo+" *");
		else:
			print(Style.RESET_ALL+prefijo);
	print("\033[1;33m"+" ----  Sufijos w1 (* propios)   ----");
	for i in range (len(palabras[0])):
		longitud=len(palabras[0])-i;
		sufijo=palabras[0][longitud-1]+sufijo;
		if i!=(len(palabras[0])-1) and i!=0:
			print(Style.RESET_ALL+sufijo+" *");
		else:
			print(Style.RESET_ALL+sufijo);
	prefijo="";
	sufijo="";
	longitud=0;
	print("\033[1;33m"+" ----  Prefijos w2 (* propios)   ----");
	for i in range (len(palabras[1])):
		prefijo=prefijo+palabras[1][i];
		if i == 0:
			print(Style.RESET_ALL+palabras[1][i]);
		elif i != (len(palabras[1])-1):
			print(Style.RESET_ALL+prefijo+" *");
		else:
			print(Style.RESET_ALL+prefijo);
	print("\033[1;33m"+" ----  Sufijos w2 (* propios)   ----");
	for i in range (len(palabras[1])):
		longitud=len(palabras[1])-i;
		sufijo=palabras[1][longitud-1]+sufijo;
		if i!=(len(palabras[1])-1) and i!=0:
			print(Style.RESET_ALL+sufijo+" *");
		else:
			print(Style.RESET_ALL+sufijo);
	return;

def concatenarCadenas(palabras):
	print("");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("\033[1;33m"+"|      CONCATENACIÓN DE CADENAS           |");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("");
	print("\033[1;33m"+"w1w2 :"+Style.RESET_ALL+palabras[0]+palabras[1]);
	return;

def longitudDeCadenasConcatenadas(palabras):
	print("");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("\033[1;33m"+"|  LONGITUD DE CONCATENACIÓN DE CADENAS   |");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("");
	print("\033[1;33m"+"|w1w2| ("+palabras[0]+palabras[1]+"): "+Style.RESET_ALL+str(len(palabras[0]+palabras[1])));
	return;

def potenciarCadenas(palabras):
	palabraPotenciadaw1="";
	palabraPotenciadaw2="";
	palabraPotenciadaw1i="";
	palabraPotenciadaw2i="";
	potenciaNegativa=0;
	print("");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("\033[1;33m"+"|            POTENCIAS CADENAS            |");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("");
	print(Style.RESET_ALL+" Ingrese el exponente n: ");
	potencia=int(input());
	if potencia<0:
		potenciaNegativa=1;
		potencia=potencia*(-1)
	palabraPotenciadaw1=potencia*palabras[0];
	palabraPotenciadaw2=potencia*palabras[1];
	if potenciaNegativa==1:
		palabraPotenciadaw1i=palabraPotenciadaw1[::-1];
		palabraPotenciadaw2i=palabraPotenciadaw2[::-1];
		print("--> w1 ^ "+str(potencia)+" : "+Style.RESET_ALL+palabraPotenciadaw1i);
		print("--> w2 ^ "+str(potencia)+" : "+Style.RESET_ALL+palabraPotenciadaw2i);
	else:
		print("--> w1 ^ "+str(potencia)+" : "+Style.RESET_ALL+palabraPotenciadaw1);
		print("\033[1;33m"+"--> w2 ^ "+str(potencia)+" : "+Style.RESET_ALL+palabraPotenciadaw2);
	return;

def evaluarCaracterEnCadenas(palabras):
	cantidadw1=0;
	cantidadw2=0;
	alafabetoPotenciado=[];
	print("");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("\033[1;33m"+"|         BUSCAR CARACTER EN CADENAS       |");
	print("\033[1;33m"+" ----------------------------------------- ");
	print("");
	print(Style.RESET_ALL+"Ingrese el símbolo (C) a buscar: ");
	simbolo=input();
	for i in range (len(palabras[0])):
		if palabras[0][i]==simbolo :
			cantidadw1=cantidadw1+1;
	for i in range (len(palabras[1])):
		if palabras[1][i]==simbolo :
			cantidadw2=cantidadw2+1;
	print(Style.RESET_ALL+"--> |w1|c :"+str(cantidadw1));
	print("--> |w2|c :"+str(cantidadw2));
	return;

def potenciarAlfabeto(E,Enuevo,k):
	alfabeto=E;
	alfabetoNuevo=Enuevo;
	alfabetoPotenciado=[];
	longitudAlfabeto=len(alfabeto);
	kReal=k;
	if kReal==1:
		print(alfabetoNuevo);
	else:
		for i in range (longitudAlfabeto):
			for j in range(len(Enuevo)):
				alfabetoPotenciado.append(alfabeto[i]+alfabetoNuevo[j]);
		kReal=kReal-1;
		potenciarAlfabeto(alfabeto,alfabetoPotenciado,kReal);
	return;



def menu(alfabeto,palabras):
	E=alfabeto;
	w=palabras;
	limpiarPantalla();
	print("\033[1;33m"+"--------------------------------------------------------------------------------");
	print("\033[1;33m"+"Tu alfabeto (E) es: ");
	print(E);
	print("\033[1;33m"+"Tus palabras w1 y w2 son: ");
	print(w);
	print("---------------------------------------------------------------------------------");
	print("\033[1;33m"+"Elija una opcón y presione enter");
	print("\033[1;33m"+"1) Calcular |w1| y |w2|");
	print("\033[1;33m"+"2) Prefijos y sufijos de w1");
	print("\033[1;33m"+"3) Concatenar w1w2");
	print("\033[1;33m"+"4) Calcular |w1w2|");
	print("\033[1;33m"+"5) Potencias w1^n y w2^n");
	print("\033[1;33m"+"6) Evaluar |w1|n y |w2|n");
	print("\033[1;33m"+"7) Potenciar E^k");
	print("\033[1;33m"+"8) Salir");
	print ("");
	print(Style.RESET_ALL+"--> Opcion: ")
	opcion=int(input());
	if opcion==1:
		longitudDeCadenas(w);
	elif (opcion==2):
		preySufijosDeCadenas(w);
	elif opcion==3:
		concatenarCadenas(w);
	elif opcion==4:
		longitudDeCadenasConcatenadas(w);
	elif opcion==5:
		potenciarCadenas(w);
	elif opcion==6:
		evaluarCaracterEnCadenas(w);
	elif opcion==7:
			print("");
			print("\033[1;33m"+" ----------------------------------------- ");
			print("\033[1;33m"+"|         POTENCIAR ALFABETO (E) ^ k      |");
			print("\033[1;33m"+" ----------------------------------------- ");
			print("");
			print(Style.RESET_ALL+"Ingrese la potencia k: ");
			k=int(input());
			potenciarAlfabeto(E,E,k);
	elif opcion==8:
		sys.exit;
	else:
		print ("\033[91m"+"Opcion inválida");
 	
	e=input();
	menu(alfabeto,palabras);



#método principal
if __name__ == '__main__':
	alfabeto=ingresarAlfabeto();
	palabras=ingresarPalabras(alfabeto);


	
