
from tkinter import *
import tkinter
import tkinter as tk
from tkinter import font as tkfont

import psutil, platform


ram = psutil.virtual_memory()
cpu = platform.processor()
SISTEMA = platform.version()
SO1 = platform.system()
disco = psutil.disk_usage('/')
print(disco)

TRDISCO = disco.total/(1024**3)
ramconvertida = ram.total/(1024**3)
app = Tk()
app.title("Será que roda?")
app.geometry("1280x720")
app.configure(background= "#bcbcbc")


mostrarTitulo = Label(app, relief="ridge", text="Vamos checar a configuração da sua máquina gamer???",foreground="#000000", background="#eeeeee", font=("Gabriola", 20))
mostrarTitulo.place(x= 150, y= 0, width=1000, height= 45)

#falando sobre a ram
mostrarRam=Label(app,borderwidth = 3,width = 40, relief="sunken", text=" Sua memoria ram tem um total de: ", foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarRam.place(x=0, y= 100, width=550, height= 30)
#mostrando a ram
mostraRam2=Label(app,borderwidth = 3,width = 40, relief="sunken", text= "" + str(ramconvertida) + " GB", foreground="#00008B", background="#E6E6FA", font = "Bahnschrift")
mostraRam2.place(x= 550,y= 100, width=550, height= 30 )
#Falando sobre cpu
mostrarCpu=Label(app,borderwidth = 3,width = 40, relief="sunken",text="Sua Cpu é: " ,foreground="#000000", background="#bcbcbc",font = "Bahnschrift")
mostrarCpu.place(x=0, y=130, width=550, height=30)
#Mostrando o processador
mostrarCpu2=Label(app,borderwidth = 3,width = 40, relief="sunken", text= "" + str(cpu) + " GB", foreground="#00008B", background="#E6E6FA", font = "Bahnschrift")
mostrarCpu2.place(x= 550,y= 130, width=550, height= 30 )
#Pegando qual sistema operacional é 
mostrarSO=Label(app,borderwidth = 3,width = 40, relief="sunken", text="Sistema Operacional: ",foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarSO.place(x=0, y=160, width=550, height=30)
#Mostando qual sistema operacional é 
mostrarSO01=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(SO1),foreground="#00008B", background="#E6E6FA", font = "Bahnschrift")
mostrarSO01.place(x=550, y=160, width=550, height=30)
#Mostrando qual o sistema operacional é 
mostrarSO02=Label(app,borderwidth = 3,width = 40, relief="sunken", text="Sistema Operacional Versão: ",foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarSO02.place(x=0, y=190, width=550, height=30)
#Mostrando a versão
mostrarSO03=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(SISTEMA),foreground="#00008B", background="#E6E6FA", font = "Bahnschrift")
mostrarSO03.place(x=550, y=190, width=550, height=30)
#Quantidade no disco rigído
mostrarDisoc=Label(app,borderwidth = 3,width = 40, relief="sunken", text="Disco rígido: " , foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarDisoc.place(x=0, y=220, width=550, height=30)

mostrarDisoc=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(TRDISCO) + " GB", foreground="#00008B", background="#E6E6FA", font = "Bahnschrift")
mostrarDisoc.place(x=550, y=220, width=550, height=30)

#def tela(self):
 #   self.frame1= Frame(self.app)
  #  self.frame2.place =(relx = 0.1, rely = 0.1, relwidth = 8.9, relheight = 8.5 )
app.mainloop()