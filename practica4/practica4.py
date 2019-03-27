from tkinter import *;
from tkinter import messagebox;
import math;

#IPN ESCOM
#Velazquez Gen Josue
#Marzo de 2019

#Configuracion de la raiz
root = Tk();
root.title("P4: Conjunto Inicial");
root.config(width=300, height=200);

#Variables
palabraN=StringVar();
palabraNstr="";
conjuntoInicial=[];
conjuntoStr=StringVar();
conjuntoStrLabel=StringVar();
numerosBinarios=[];
conjuntoFinal=[];

#Funciones
def limpiar():
	palabraN.set("");

def cancelar():
	limpiar();
	conjuntoInicial.clear();
	numerosBinarios.clear();
	conjuntoStrLabel.set("Conjunto: {}");
	conjuntoStr.set("");


def guardarTextoEnLista(): #guarda el texto de la caja de entrada en una lista
	palabraNstr=palabraN.get();
	conjuntoInicial.append(palabraNstr);
	if(conjuntoStr.get()==""):
		conjuntoStr.set(conjuntoStr.get()+palabraNstr);
	else:
		conjuntoStr.set(conjuntoStr.get()+","+palabraNstr);

	conjuntoStrLabel.set("Conjunto: {"+conjuntoStr.get()+"}");
	limpiar();

def guardarConjuntoInicialenTXT(): #copia el contenido de la lista en el archivo de texto "entrada.txt", cada elemento una linea
	archivoEntrada = open ("entrada.txt","w");
	for i in range (len(conjuntoInicial)):
		if i==0:
			archivoEntrada.write(conjuntoInicial[i]);
		else:
			archivoEntrada.write("\n"+conjuntoInicial[i]);
	archivoEntrada.close();
	messagebox.showinfo("Guardado con exito", "Se ha guardado el conjunto inicial en el TXT")
	limpiar();

def calcularNumerosBinarios():#calcula los numeros binarios que representaran las concatenaciones de estados
	for i in range(pow(2,len(conjuntoInicial))):
		binary=str(bin(i));
		numerosBinarios.append(binary[-int(len(binary)-2):]);
	longitudBinaria=len(numerosBinarios[pow(2,len(conjuntoInicial))-1])
	for j in range(len(numerosBinarios)):
		if (len(numerosBinarios[j])<longitudBinaria):
			for k in range(longitudBinaria-len(numerosBinarios[j])):
				numerosBinarios[j]="0"+numerosBinarios[j];

def calcularConjuntoPotencia():#usando los numeros binarios, crea una lista con los elementos del conjunto potencia
	calcularNumerosBinarios();
	conjuntosConcatenados="";
	for i in range(len(numerosBinarios)):
		palabraTemporal=numerosBinarios[i];
		for j in range(len(palabraTemporal)-1,-1,-1):
			if(palabraTemporal[j]!="0"):
				if(conjuntosConcatenados==""):
					conjuntosConcatenados=conjuntoInicial[j];
				else:
					conjuntosConcatenados=conjuntosConcatenados+","+conjuntoInicial[j];
		conjuntosConcatenados="{"+conjuntosConcatenados+"}";
		conjuntoFinal.append(conjuntosConcatenados);
		conjuntosConcatenados="";

def mostrarConjuntoPotencia():#abre una nueva ventana y muestra el conjunto potencia
	root2=Tk();
	root2.title("Resultado Conjunto Potencia ");
	root2.config(width=300, height=200);
	frame2=Frame(root2,width=300,height=300);
	frame2.pack(fill="both",expand=0);
	frame2.config(padx=15,pady=15);
	lblConjuntoPotencia=Label(frame2,text="Conjunto potencia: \n\n\n",font="bold").grid(row=0,column=0,columnspan=4);
	txtConjuntoPotencia=Text(frame2);
	btnCerrar=Button(frame2,text="OK",background="#0FB845",relief="groove",command=root2.quit());
	btnCerrar.grid(row=2,columnspan=4);
	txtConjuntoPotencia.insert(INSERT,str(conjuntoFinal));
	txtConjuntoPotencia.grid(row=1,columnspan=4);
	root2.mainloop();

def guardarConjuntoPotenciaTXT():#guarda la lista de conjuntoFinal en el txt "salida.txt"
	calcularConjuntoPotencia();
	archivoSalida=open("salida.txt","w");
	for i in range (len(conjuntoFinal)):
		if i==0:
			archivoSalida.write(conjuntoFinal[i]);
		else:
			archivoSalida.write("\n"+conjuntoFinal[i]);
	archivoSalida.close();
	messagebox.showinfo("Guardado con exito", "Se ha guardado el conjunto potencia en el TXT");
	mostrarConjuntoPotencia();


#Frame principal
conjuntoStrLabel.set("Conjunto: {}");
frame=Frame(root,width=720,height=560);
frame.pack(fill='both',expand=1);
frame.config(padx=15,pady=15);

#contenido de la ventana
lblConjuntoInicial=Label(frame,text="CONJUNTO INICIAL",font="bold").grid(row=0,column=0,padx=5, pady=5,columnspan=4);
lblIntruccion=Label(frame,text="(Ingrese estado por estado)\n").grid(row=1,column=0,columnspan=4,padx=5, pady=5);
lblConjunto=Label(frame,text="Estado: ").grid(row=2,column=0,padx=5,pady=5,columnspan=2);
txtConjunto = Entry(frame,textvariable=palabraN).grid(row=2,column=2,padx=5,pady=5); #caja de texto para entrada
btnEnviarALista=Button(frame,text="INGRESAR",command=guardarTextoEnLista,background="#0000FF",relief="groove").grid(row=2,column=3,padx=5,pady=5);
btnIngresarATXT=Button(frame,text="PROCESAR A TXT",command=guardarConjuntoInicialenTXT,background="#0FB845",relief="groove").grid(row=4,column=0,padx=5,pady=5,columnspan=2);
btnCalcularCPotencia=Button(frame,text="Calcular",background="#F8EB03",relief="groove",command=guardarConjuntoPotenciaTXT).grid(column=2,row=4,padx=5,pady=5);
btnCancelar=Button(frame,text="CANCELAR",command=cancelar,background="#F50743",relief="groove").grid(row=4,column=3,padx=5,pady=5);
lblConjuntoActual=Label(frame,textvariable=conjuntoStrLabel).grid(row=3,columnspan=4,padx=5,pady=5);

root.mainloop(); #bucle de la raiz
