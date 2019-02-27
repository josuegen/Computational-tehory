#You gotta create the files: l1.txt, l2.txt. concatenacion.txt, union.txt in the same path you just gonna run this script
#Es necesario crear los archivos: l1.txt, l2.txt. concatenacion.txt, union.txt en la misma ruta donde correrás este script

from numpy import *;
import os;
from colorama import *;
import sys;
import yaml;


#autor: Josue Velazquez Gen
#fecha: 16/Febrero/2019
#IPN ESCOM

def limpiarPantalla():
	if(os.name=="windows"):
		os.system("cls");	
	else: 
		os.system("clear");
	print (chr(27)+"[1;95m"+"                               P R A C T I C A   2");
	print("");
	print("");
	print("");
	return;

def ingresarAlfabeto():
	alfabeto=[];
	simbolo="";
	limpiarPantalla();
	print("\033[1;33m"+"Ingrese los simbolos de su alfabeto(E), linea a linea");
	print("\033[1;33m"+"Longitud maxima del alfabeto(E) permitida (50)");
	print("\033[1;33m"+"Si ha terminado de ingresar los simbolos para (E) escriba 'fin' y presione enter");
	print(Style.RESET_ALL+"--> Alfabeto :")
	for i in range (50):
		simbolo=input(Style.RESET_ALL);
		if simbolo!="fin": 			
			if len(simbolo)==1: 			
				if simbolo not in alfabeto: 
					alfabeto.append(simbolo);
				else:
					print("\033[91m"+"!! EL SiMBOLO " +Style.RESET_ALL+"'"+simbolo+"'"+"\033[91m"+" YA EXISTE EN EL ALFABETO(E) !!");
			else	:
				print("\033[91m"+"!! EL SiMBOLO SOLO PUEDE SER DE LONGITUD (1) !!");
		else:
			if len(alfabeto)<=1:			
				print("\033[91m"+"!! EL ALFABETO DEBE TENER AL MENOS (2) SIMBOLOS !!");
				print(Style.RESET_ALL+"--> Alfabeto :")
			else:
				break;
	return alfabeto;

def validarPertenenciaPalabras(E,palabra):
	pertenece=1;
	for i in range (len(palabra)):
		if palabra[i] not in (alfabeto):
			pertenece=0;
			break;
	return pertenece;

def ingresarLenguaje(E,numerodeLenguaje):
	limpiarPantalla();
	palabra="";
	palabrasL=[];
	print("\033[1;33m"+"--------------------------------------------------------------------------------");
	print("\033[1;33m"+"Tu alfabeto (E) es: ");
	print(E);
	print("--------------------------------------------------------------------------------");
	print("\033[1;33m"+"                          LENGUAJE L"+str(numerodeLenguaje));
	print("");
	print("\033[1;33m"+"Ingrese las palabras del LENGUAJE "+str(numerodeLenguaje)+", linea a linea");
	print("\033[1;33m"+"Para terminar de ingresar palabras a L"+str(numerodeLenguaje)+", escriba '/fin' y presione enter");
	print(Style.RESET_ALL+"--> Palabras :")
	while 1==1:
		palabra=input(Style.RESET_ALL);
		if validarPertenenciaPalabras(E,palabra):
			palabrasL.append(palabra);
		elif palabra=="./fin":
			break;
		else:
			print("\033[91m"+"!! LA PALABRA "+Style.RESET_ALL+palabra+"\033[91m"+" CONTIENE CARACTERES QUE NO FORMAN EL ALFABETO ESTABLECIDO !!");

	return palabrasL;

def copiarLenguagetxt(lenguaje,numerodeLenguaje):
	if numerodeLenguaje==1:
		l1 = open ("l1.txt","w")
		for i in range (len(lenguaje)):
			if i==0:
				l1.write(lenguaje[i]);
			else:
				l1.write("\n"+lenguaje[i]);
		l1.close();
	else:
		l2 = open ("l2.txt","w")
		for i in range (len(lenguaje)):
			if i==0:
				l2.write(lenguaje[i]);
			else:
				l2.write("\n"+lenguaje[i]);
		l2.close();
def consultarLenguajetxt(numerodeLenguaje):
	lenguaje=[];
	print ("");
	print("\033[1;33m"+"         --           LENGUAJE L"+str(numerodeLenguaje)+"        --       \n");
	if numerodeLenguaje==1:
		l1= open ("l1.txt","r")
		for linea in l1:
			lenguaje.append(linea.rstrip('\n'));
		l1.close();
	else:
		l2= open ("l2.txt","r")
		for linea in l2.readlines(): 
			lenguaje.append(linea.rstrip('\n'));
		l2.close();
	print("\033[1;33m"+"L"+str(numerodeLenguaje)+" :");
	print (Style.RESET_ALL);
	print (lenguaje);
	wait=input();

def concatenarLenguajes(l1,l2):
	lenguaje1=l1;
	lenguaje2=l2;
	concatenacion=[];
	longitud=0;
	strOpcionConcatenacion="";

	print("\033[1;33m"+"                          CONCATENACION DE LENGUAJES");
	print("");
	print("\033[1;33m"+"Ingrese el orden de la concatenación");
	print("\033[1;33m"+"1. L1*L2");
	print("\033[1;33m"+"2. L2*L1");
	print(Style.RESET_ALL+"--> Opcion:")
	opcion=int(input());
	if opcion==1:
		strOpcionConcatenacion="L1*L2";
		for i in range(len(lenguaje1)):
			for j in range(len(lenguaje2)):
				concatenacion.append(lenguaje1[i]+lenguaje2[j]);
	elif opcion==2:
		strOpcionConcatenacion="L2*L1";
		for i in range(len(lenguaje2)):
			for j in range(len(lenguaje1)):
				concatenacion.append(lenguaje2[i]+lenguaje1[j]);
	concatena= open ("concatenacion.txt","w");
	for k in range (len(concatenacion)):
			if k==0:
				concatena.write(concatenacion[k]);
			else:
				concatena.write("\n"+concatenacion[k]);
	concatena.close();
	print("\033[1;33m"+"----    Concatenacion de "+strOpcionConcatenacion+ "   ----\n");
	print("\033[1;33m"+strOpcionConcatenacion+" :");
	print(Style.RESET_ALL);
	print(concatenacion);
	wait=input();

def unirLenguajes(l1,l2):
	union=open("union.txt","w");
	unionLenguajes=l1;
	for j in range(len(l2)):
		if(l2[j] not in unionLenguajes):
			unionLenguajes.append(l2[j]);
	for i in range (len(unionLenguajes)):
			if i==0:
				union.write(unionLenguajes[i]);
			else:
				union.write("\n"+unionLenguajes[i]);
	print("\033[1;33m"+"         ----    Unión de L1 y L2    ----\n");
	print("\033[1;33m"+"L1UL2 | L2UL1 :");
	print(Style.RESET_ALL);
	print(unionLenguajes);
	wait=input();




def menu(E,lenguajeUno,lenguajeDos):
	salir=0;
	while not salir:
		limpiarPantalla();
		print("\033[1;33m"+"--------------------------------------------------------------------------------");
		print("\033[1;33m"+"Tu alfabeto (E) es: ");
		print(E);
		print("\033[1;33m"+"Tus lenguajes L1 y L2 ya estan definidos");
		print("---------------------------------------------------------------------------------");
		print("\033[1;33m"+"Elija una opcion y presione enter");
		print("\033[1;33m"+"1) Leer archivo de txt L1");
		print("\033[1;33m"+"2) Leer archivo de txt L2");
		print("\033[1;33m"+"3) Concatenar Lenguajes");
		print("\033[1;33m"+"4) Unir Lenguajes");
		print("\033[1;33m"+"5) Salir");
		print(Style.RESET_ALL+"--> Opcion: ")
		opcion=int(input());
		if opcion==1:
			consultarLenguajetxt(1);
		elif opcion==2:
			consultarLenguajetxt(2);
		elif opcion==3:
			concatenarLenguajes(lenguajeUno,lenguajeDos);
		elif opcion==4:
			unirLenguajes(lenguajeUno,lenguajeDos);
		elif opcion==5:
			salir=1;
			break;

if __name__ == '__main__':
	alfabeto=ingresarAlfabeto();
	lenguajeUno=ingresarLenguaje(alfabeto,1);
	copiarLenguagetxt(lenguajeUno,1);
	lenguajeDos=ingresarLenguaje(alfabeto,2);
	copiarLenguagetxt(lenguajeDos,2);
	menu(alfabeto,lenguajeUno,lenguajeDos);
