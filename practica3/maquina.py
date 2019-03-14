from tkinter import *;
from analizador import *;
from validador import *;

#Autor: Josue Velazquez
#ESCOM IPN
#MARZO DE 2019

# -----   RAIZ DE INTERFAZ GRAFICA ------#

#Configuracion de la raiz
root = Tk();
root.title("Maquina reconocedora de lenguaje");
root.config(width=300, height=200)



#------ VARIABLES ----- #
p=StringVar();
r=StringVar();
p.set("");
r.set("");

#------ OBJETOS ------ #
validador=Validador();
analizador=Analizador();

#------ FUNCIONES ------ #
def ingresarCintaDeEntrada():
	#Verifica que los simbolos pertenezcan al alfabeto
	p.set("\nCadena introducida: "+validador.procesarPalabra(txtPalabra.get()));
	#Ejecuta el analisis por tabla de estados
	if(validador.booleanoDePertenencia()):
		if(analizador.analizaPalabra(txtPalabra.get())):
			r.set("Palabra valida  :)\n")
		else:
			r.set("Palabra invalida :(\n");
		state1=analizador.estado;






	
#----- WIDGETS DE INTERFAZ GRAFICA ----#
frame=Frame(root,width=720,height=560);
frame.pack(fill='both',expand=1);
frame.config(padx=15,pady=15);

lblPalabra=Label(frame,text="Palabra : ").grid(row=1,column=0);
txtPalabra=Entry(frame);
txtPalabra.grid(row=1, column=1,padx=10, pady=5);
txtPalabra.config(justify="center");
lblLenguaje=Label(frame,text="Lenguaje (a^+b | c*b^+)\n\n",font='Helvetica 13 bold').grid(row=0,columnspan=3,padx=5,pady=5);
lblCintaEntrada=Label(frame,textvariable=p).grid(row=3,columnspan=2,padx=5, pady=5);
lblResultadoAnalisis=Label(frame,textvariable=r,fg='#0E01F6',font='bold').grid(row=2,columnspan=2,padx=5, pady=5);
lblTituloImagen=Label(frame,text="Ultimo Estado",font="bold").grid(row=1,column=2);
imagen=PhotoImage(file="q0.png")
if(state1==0):
	imagen=PhotoImage(file="q0.png");
if(state1==1):
	imagen=PhotoImage(file="q1.png");
if(state1==2):
	imagen=PhotoImage(file="q2.png");
if(state1==3):
	imagen=PhotoImage(file="q3.png");
if(state1==4):
	imagen=PhotoImage(file="q4.png");
if(state1==5):
	imagen=PhotoImage(file="q5.png");
if(state1==6):
	imagen=PhotoImage(file="q6.png");
print(str(state));
lblImagen=Label(frame,image=imagen,width=200,height=200).grid(row=2,column=2);
btnProcesar=Button(frame,text="PROCESAR",command=ingresarCintaDeEntrada,background="#0FB845",activebackground="#F50743",relief="groove").grid(row=5,columnspan=3,padx=5, pady=5);




#Bucle de aplicacion
root.mainloop();
