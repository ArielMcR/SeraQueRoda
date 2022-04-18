
from tkinter import *
import tkinter
import os
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from csconfig import * 
from lolconfig import * 
from testandoBanco import *
from RDR import * 
import psutil, platform
import cpuinfo
import wmi as w


"""Criando as variaveis que vamos usar para apresentar na interface gráfica"""
ram = psutil.virtual_memory()
"""cpu = platform.processor() não iremos mais utilizar essa biblioteca""" 
cpuCores = str(psutil.cpu_count())
nomeProcessador = cpuinfo.get_cpu_info()['brand_raw']
Frequenciado = cpuinfo.get_cpu_info()['hz_actual_friendly']
arquitetura = cpuinfo.get_cpu_info()['arch']
bits = cpuinfo.get_cpu_info()['bits']
SISTEMA = platform.version()
SO1 = platform.system()
disco = psutil.disk_usage('/')
TRDISCO = disco.total/(1024**3)
ramconvertida = ram.total/(1024.0**3)
computer = w.WMI()
gpu_info = computer.Win32_VideoController()[0]

""" Outra biblioteca para pegar o processador
gpu_info = computer.Win32_VideoController()[0]
gpu = gpu_info.Name
"""


"""def do counter Strike"""
def abrir_janelacs():
    """ Ta em fase de teste ainda vamos com calma"""
    cor ="#8B0000"	

    app2 = tk.Toplevel()
    app2.title('CS')
    app2.geometry("1100x720")
    app2.minsize(height= 720, width= 1100)
    app2.maxsize(height= 720, width= 1100)

    labelCs = Label(app2, borderwidth = 3,width =10, relief="sunken", foreground="#0000CD", background="#696969")
    labelCs.place(x=0, y= 0, width=1500, height= 99)

    mostrarTitulo = Label(app2, text="Comparando as Configurações...",foreground="#000000", background="#696969", font=("Trebuchet MS", 30))
    mostrarTitulo.place(x= 300, y= 30, width=600, height= 45)

    Cs=Label(app2,text="Requisitos Minímos Cs", foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
    Cs.place(x=0, y= 100, width=550, height= 30)

    Ram2=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= " Memoria Ram: " + str(memoria) + " GB", foreground="#00008B", background="#bcbcbc", font = "Bahnschrift")
    Ram2.place(x=0, y= 130, width=550, height= 30)
    cores=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= "Cores do Cpu: " + str(corescpu), foreground="#00008B", background="#bcbcbc", font = "Bahnschrift")
    cores.place(x=0, y= 155, width=550, height= 30)
    frequencia=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= " Frequencia do Cpu: " + str(processador) + " Ghz", foreground="#00008B", background="#bcbcbc", font = "Bahnschrift")
    frequencia.place(x=0, y= 180, width=550, height= 30)
    soVersao=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= " Versão do SO: " + str(SOCS), foreground="#00008B", background="#bcbcbc", font = "Bahnschrift")
    soVersao.place(x=0, y= 210, width=550, height= 30)
    espaçoEmDisco=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= "Espaço em Disco: " + str(discorigido) + " GB", foreground="#00008B", background="#bcbcbc", font = "Bahnschrift")
    espaçoEmDisco.place(x=0, y= 240, width=550, height= 30)

    
    Cs=Label(app2,text="Configuração do seu Pc", foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
    Cs.place(x=550, y= 100, width=550, height= 30)

    if (linha[6] >= linhaCs[3]):
      cor = "#008000"

    Ram2=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= " Memoria Ram: " + str(linha[6]) + " GB", foreground="#00008B", background=cor, font = "Bahnschrift")
    Ram2.place(x=550, y= 130, width=550, height= 30)

    if (linha[4] >= linhaCs[2]):
        cor = "#008000"
    cores=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= "Cores do Cpu: " + str(linha[4]), foreground="#00008B", background=cor, font = "Bahnschrift")
    cores.place(x=550, y= 155, width=550, height= 30)
    if(linha[5] >= linha[1]):
        cor = "#008000"
    frequencia=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= " Frequencia do Cpu: " + str(linha[5]), foreground="#00008B", background=cor, font = "Bahnschrift")
    frequencia.place(x=550, y= 180, width=550, height= 30)
    if (linha[2] >= linhaCs[0]):
        cor = "#008000"
    soVersao=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= " Versão do SO: " + str(linha[2]), foreground="#00008B", background=cor, font = "Bahnschrift")
    soVersao.place(x=550, y= 210, width=550, height= 30)
    if (linha[7] >= linhaCs[4]):
        cor = "#008000"
    espaçoEmDisco=Label(app2,borderwidth = 3,width = 40, relief="sunken", text= "Espaço em Disco: " + str(linha[7]) + " GB", foreground="#00008B", background=cor, font = "Bahnschrift")
    espaçoEmDisco.place(x=550, y= 240, width=550, height= 30)

    botao2 = tk.Button(app2, text="Voltar", command= app2.destroy, foreground = "#FFFFFF", background="#696969")
    botao2.place(x = 1060, y = 2)

    """ era para apresentar na tela uma imagem com as config de vídeo, mas n está aperecendo"""
  

"""" Def da janela do lol"""
def abrir_lol():
     cor ="#8B0000"
     app3 = tk.Toplevel()
     app3.title('League of Legends')
     app3.geometry("1100x720")
     app3.minsize(height= 720, width= 1100)
     app3.maxsize(height= 720, width= 1100)

     Labellol = Label(app3, borderwidth = 3,width =10, relief="sunken", foreground="#0000CD", background="#696969")
     Labellol.place(x=0, y= 0, width=1500, height= 99)

     mostrarTitulo = Label(app3, text="Comparando as Configurações...",foreground="#000000", background="#696969", font=("Trebuchet MS", 30))
     mostrarTitulo.place(x= 300, y= 30, width=600, height= 45)

     Cs=Label(app3,text="Requisitos Minímos LOL", foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
     Cs.place(x=0, y= 100, width=550, height= 30)

     Ram2=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= " Memoria Ram: " + str(ramlol) + " GB", foreground="#00008B", background="#A9A9A9", font = "Bahnschrift")
     Ram2.place(x=0, y= 130, width=550, height= 30)
     cores=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= "Cores do Cpu: " + str(coreslol), foreground="#00008B", background="#A9A9A9", font = "Bahnschrift")
     cores.place(x=0, y= 155, width=550, height= 30)
     frequencia=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= " Frequencia do Cpu: " + str(cpulol) + " Ghz", foreground="#00008B", background="#A9A9A9	", font = "Bahnschrift")
     frequencia.place(x=0, y= 180, width=550, height= 30)
     soVersao=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= " Versão do SO: " + str(Solol), foreground="#00008B", background="#A9A9A9", font = "Bahnschrift")
     soVersao.place(x=0, y= 210, width=550, height= 30)
     espaçoEmDisco=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= "Espaço em Disco: " + str(discolol) + " GB", foreground="#00008B", background="#A9A9A9	", font = "Bahnschrift")
     espaçoEmDisco.place(x=0, y= 240, width=550, height= 30)

     Pc=Label(app3,text="Configuração do seu Pc", foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
     Pc.place(x=550, y= 100, width=550, height= 30)
     
     if(linha[6]>= linhaLOL[4]):
         cor = "#008000"
     Ram2=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= " Memoria Ram: " + str(linha[6]) + " GB", foreground="#00008B", background="#008000", font = "Bahnschrift")
     Ram2.place(x=550, y= 130, width=550, height= 30)
     if(linha[4] >= linhaLOL[3]):
         cor = "#008000"
     cores=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= "Cores do Cpu: " + str(linha[4]), foreground="#00008B", background=cor, font = "Bahnschrift")
     cores.place(x=550, y= 155, width=550, height= 30)
     if(linha[5] >= linhaLOL[2]):
         cor = "#008000"
     frequencia=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= " Frequencia do Cpu: " + str(linha[5]), foreground="#00008B", background=cor, font = "Bahnschrift")
     frequencia.place(x=550, y= 180, width=550, height= 30)
     if(linha[2] >= linhaLOL[1]):
         cor = "#008000"
     soVersao=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= " Versão do SO: " + str(linha[2]), foreground="#00008B", background=cor, font = "Bahnschrift")
     soVersao.place(x=550, y= 210, width=550, height= 30)
     if(linha[7] >= linhaLOL[5]):
         cor = "#008000"
     espaçoEmDisco=Label(app3,borderwidth = 3,width = 40, relief="sunken", text= "Espaço em Disco: " + str(linha[7]) + " GB", foreground="#00008B", background=cor, font = "Bahnschrift")
     espaçoEmDisco.place(x=550, y= 240, width=550, height= 30)

     
     LabeDenovo = Label(app3,relief="sunken", foreground="#0000CD", background="#696969")
     LabeDenovo.place(x=0, y= 270, width=1500, height= 500)

     LabeDenovo2 = Label(app3, borderwidth = 2,width =10, relief="sunken", foreground="#0000CD", background="#ffffff")
     LabeDenovo2.place(x=20, y= 300, width=1060, height= 380)

     LabelTexto = Label(app3, text="Qualidade Gráfica: ", background="#ffffff", font =("Times New Roman", 20))
     LabelTexto.place(x=22, y= 305, width=230, height= 50)

     botao = tk.Button(app3, text="Voltar", command= app3.destroy, foreground = "#FFFFFF", background="#696969")
     botao.place(x = 1060, y = 2)

""" Criando a def do red dead redemption """
def abrir_rdr2():
     cor ="#8B0000"
     app4 = tk.Toplevel()
     app4.title('red dead redemption')
     app4.geometry("1100x720")
     app4.minsize(height= 720, width= 1100)
     app4.maxsize(height= 720, width= 1100)

     Labellol = Label(app4, borderwidth = 3,width =10, relief="sunken", foreground="#0000CD", background="#696969")
     Labellol.place(x=0, y= 0, width=1500, height= 99)

     mostrarTitulo = Label(app4, text="Comparando as Configurações...",foreground="#000000", background="#696969", font=("Trebuchet MS", 30))
     mostrarTitulo.place(x= 300, y= 30, width=600, height= 45)

     Cs=Label(app4,text="Requisitos Minímos RDR", foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
     Cs.place(x=0, y= 100, width=550, height= 30)

     Ram2=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= " Memória Ram: " + str(linhaRDR[4]) + " GB", foreground="#00008B", background="#A9A9A9", font = "Bahnschrift")
     Ram2.place(x=0, y= 130, width=550, height= 30)
     cores=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= "Cores do Cpu: " + str(linhaRDR[3]), foreground="#00008B", background="#A9A9A9", font = "Bahnschrift")
     cores.place(x=0, y= 155, width=550, height= 30)
     frequencia=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= " Frequência do Cpu: " + str(linhaRDR[2]) + " Ghz", foreground="#00008B", background="#A9A9A9	", font = "Bahnschrift")
     frequencia.place(x=0, y= 180, width=550, height= 30)
     soVersao=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= " Versão do SO: " + str(linhaRDR[1]), foreground="#00008B", background="#A9A9A9", font = "Bahnschrift")
     soVersao.place(x=0, y= 210, width=550, height= 30)
     espaçoEmDisco=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= "Espaço em Disco: " + str(linhaRDR[5]) + " GB", foreground="#00008B", background="#A9A9A9	", font = "Bahnschrift")
     espaçoEmDisco.place(x=0, y= 240, width=550, height= 30)

     Pc=Label(app4,text="Configuração do seu Pc", foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
     Pc.place(x=550, y= 100, width=550, height= 30)
     
     if(linha[6]>= linhaRDR[4]):
         cor = "#008000"
     else:
         cor = "#8B0000"    
     Ram2=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= " Memoria Ram: " + str(linha[6]) + " GB", foreground="#00008B", background="#008000", font = "Bahnschrift")
     Ram2.place(x=550, y= 130, width=550, height= 30)
     if(linha[4] >= linhaRDR[3]):
         cor = "#008000"
     else:
         cor = "#8B0000"    
     cores=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= "Cores do Cpu: " + str(linha[4]), foreground="#00008B", background=cor, font = "Bahnschrift")
     cores.place(x=550, y= 155, width=550, height= 30)
     if(linha[5] >= linhaRDR[2]):
         cor = "#008000"
     
     frequencia=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= " Frequencia do Cpu: " + str(linha[5]), foreground="#00008B", background=cor, font = "Bahnschrift")
     frequencia.place(x=550, y= 180, width=550, height= 30)
     if(linha[2] >= linhaRDR[1]):
         cor = "#008000"
      
     soVersao=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= " Versão do SO: " + str(linha[2]), foreground="#00008B", background=cor, font = "Bahnschrift")
     soVersao.place(x=550, y= 210, width=550, height= 30)
     if(linha[7] >= linhaRDR[5]):
         cor = "#008000"
     else:
         cor = "#8B0000"
     espaçoEmDisco=Label(app4,borderwidth = 3,width = 40, relief="sunken", text= "Espaço em Disco: " + str(linha[7]) + " GB", foreground="#00008B", background=cor, font = "Bahnschrift")
     espaçoEmDisco.place(x=550, y= 240, width=550, height= 30)

     
     LabeDenovo = Label(app4,relief="sunken", foreground="#0000CD", background="#696969")
     LabeDenovo.place(x=0, y= 270, width=1500, height= 500)

     LabeDenovo2 = Label(app4, borderwidth = 2,width =10, relief="sunken", foreground="#0000CD", background="#ffffff")
     LabeDenovo2.place(x=20, y= 300, width=1060, height= 380)

     LabelTexto = Label(app4, text="Qualidade Gráfica: ", background="#ffffff", font =("Times New Roman", 20))
     LabelTexto.place(x=22, y= 305, width=230, height= 50)

     botao = tk.Button(app4, text="Voltar", command= app4.destroy, foreground = "#FFFFFF", background="#696969")
     botao.place(x = 1060, y = 2)



   
""" criando a parte de interface gráfica"""
app = Tk()
app.title("Será que roda?")
app.geometry("1100x720")
app.configure(background= "#708090")
app.minsize(height= 720, width= 1100)
app.maxsize(height= 720, width= 1100)

""""
print("Numero de cores do processador", cpuCores) 
print(len(psutil.Process().cpu_affinity()))
print("Frequencia do processador", psutil.cpu_freq(percpu=True)) 
"""
#Alterando a cor de cima 
labelteste = Label(app, borderwidth = 3,width =10, relief="sunken", foreground="#0000CD", background="#696969")
labelteste.place(x=0, y= 0, width=1500, height= 99)

#Mudando de cor em baixo 
labelteste2 = Label(app,borderwidth = 3,width = 20, relief="sunken", foreground="#808080", background="#A9A9A9")
labelteste2.place(x = 0 , y = 340, width= 1100, height=500)

#Parte branca lá em baixo nos buttons
labelteste3 = Label(app, borderwidth=3, width= 20, relief= "sunken", background="#FFFFFF")
labelteste3.place(x = 60, y = 425, width=1000, height= 250)

Titulo = Label(app, text="Checando as configurações do seu computador....", foreground = "#000000", background= "#696969", font=("Trebuchet MS", 30))
Titulo.place(x= 60, y= 30, width=1000, height= 45)



#falando sobre a ram // parar criar borda (app,borderwidth = 3,width = 40, relief="sunken")
mostrarRam=Label(text=" Memoria RAM: ", foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarRam.place(x=0, y= 100, width=550, height= 30)
#mostrando a ram
mostraRam2=Label(app,borderwidth = 3,width = 40, relief="sunken", text= "" + str(linha[6]) + " GB", foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostraRam2.place(x= 550,y= 100, width=550, height= 30 )
#Falando sobre cpu
mostrarCpu=Label(text="Cpu" ,foreground="#000000", background="#bcbcbc",font = "Bahnschrift")
mostrarCpu.place(x=0, y=130, width=550, height=30)
#Mostrando o processador
mostrarCpu2=Label(app,borderwidth = 3,width = 40, relief="sunken", text= "" + nomeProcessador, foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostrarCpu2.place(x= 550,y= 130, width=550, height= 30 )
#Pegando qual sistema operacional é 
mostrarSO=Label(text="Sistema Operacional: ",foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarSO.place(x=0, y=160, width=550, height=30)
#Mostando qual sistema operacional é 
mostrarSO01=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(SO1),foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostrarSO01.place(x=550, y=160, width=550, height=30)
#Mostrando qual o sistema operacional é 
mostrarSO02=Label(text="Sistema Operacional Versão: ",foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarSO02.place(x=0, y=190, width=550, height=30)
#Mostrando a versão
mostrarSO03=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(SISTEMA),foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostrarSO03.place(x=550, y=190, width=550, height=30)
#Quantidade no disco rigído
mostrarDisoc=Label(text="Disco rígido: " , foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarDisoc.place(x=0, y=220, width=550, height=30)

mostrarDisoc=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(linha[7]) + " GB", foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostrarDisoc.place(x=550, y=220, width=550, height=30)

mostrarCoresCpu=Label(text="Cores do Cpu: " , foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarCoresCpu.place(x=0, y=250, width=550, height=30)

mostrarDisoc=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(cpuCores) + " Cores", foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostrarDisoc.place(x=550, y=250, width=550, height=30)

mostrarFrequencia=Label(text="Frequência do Processador: " , foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrarFrequencia.place(x=0, y=280, width=550, height=30)

mostrarFrequencia2=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(Frequenciado), foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostrarFrequencia2.place(x=550, y=280, width=550, height=30)

mostrararch=Label(text="Arquitetura do Sistema: " , foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrararch.place(x=0, y=310, width=550, height=30)

mostrararch2=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(arquitetura), foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostrararch2.place(x=550, y=310, width=550, height=30)

mostrararch=Label(text="Placa de Vídeo: " , foreground="#000000", background="#bcbcbc", font = "Bahnschrift")
mostrararch.place(x=0, y=340, width=550, height=30)

mostrararch2=Label(app,borderwidth = 3,width = 40, relief="sunken", text="" + str(gpu_info.name), foreground="#000000", background="#FFFFFF", font = ("Comic Sans MS", 12))
mostrararch2.place(x=550, y=340, width=550, height=30)





botao = tk.Button(app, text=" Counter Strike Global Offensive", command= abrir_janelacs, background="#A9A9A9")
botao.place(x=63, y= 430, width=200, height= 25)

botao = tk.Button(app, text="League Of Legends", command= abrir_lol, background="#A9A9A9")
botao.place(x=275, y= 430, width=200, height= 25)

botao = tk.Button(app, text="Red Dead Redemption", command= abrir_rdr2, background="#A9A9A9")
botao.place(x=487, y= 430, width=200, height= 25)

botaofechar = tk.Button(app, text="Fechar", command= app.destroy, foreground= "#FFFFFF",background= "#696969")
botaofechar.place(x = 1050, y = 2, width=55)

jogo = Label(app, text="Escolha o jogo a ser comparado: ",foreground="#000000", background="#A9A9A9", font=("Times New Roman", 25))
jogo.place(x= 280, y=370, width=520, height= 35)



app.mainloop()
