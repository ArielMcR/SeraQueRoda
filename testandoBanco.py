from tkinter.constants import INSERT
import mysql.connector
import psutil, platform
import GPUtil
from csconfig import *
from lolconfig import *
from RDR import * 


"""criando a conexão com o banco de dados"""
banco = mysql.connector.connect(
host="localhost",
user="root",
password="",
database = "SeraQueRoda"
)

"""definindo o cursos e as variaveis da qual vamos utilizar"""
cursor = banco.cursor()
ram = (psutil.virtual_memory())
ramconvertida = ram.total/(1024.0**3)
SO1 = platform.system()
cpu = platform.processor()
sistema= platform.version()
disco = (psutil.disk_usage('/'))
TRDISCO = disco.total/(1024**3)
cpuCores = psutil.cpu_count()
Freq = str(psutil.cpu_freq(percpu=True))


"""inserindo valores ao nosso banco de dados na tabela antedeguemon2, sempre lembrar de comentar para não 
ficar colocando dados toda hora que rodar o código"""
"""
info = ("INSERT INTO seraqueroda(so,versaoSo, cpu, cores, freq, ram, disco) VALUES (%s,%s,%s,%s,%s,%s,%s)")
valores = (SO1, sistema,cpu, cpuCores, Freq,ramconvertida, TRDISCO)
cursor.execute(info,valores)
"""

#Inserindo as informações do Cs no banco de dados
"""info = ("INSERT INTO lolconfig(solol,cpulol,coreslol,ramlol, discolol) VALUES (%s,%s,%s,%s,%s)")
valores = (Solol, cpulol, coreslol, ramlol, discolol)
cursor.execute(info,valores)"""

"""info = ("INSERT INTO rdrconfig(Sordr,frequenciaRDR,coresrdr,ramrdr, discordr) VALUES (%s,%s,%s,%s,%s)")
valores = (Sordr, frquenciaRDR, coresrdr, ramrdr, discordr)
cursor.execute(info,valores)"""


"""dando select all na tabela antedeguemon2"""
sql = ("SELECT * FROM seraqueroda")
cursor.execute(sql)


"""apresentando na tela os valores que estão dentro do nosso banco"""
resultados = cursor.fetchall()
print("Temos um total de ", cursor.rowcount, "resultados")
for linha in resultados:
 
 print("ID: ", linha[0])
 print(" SO1:", linha[1])
 print(" sistema: ", linha[2])
 print(" cpu: ", linha[3])
 print(" cpuCores: ", linha[4])
 print(" frequencia: ", linha[5])
 print(" Memoria ram: ", linha[6])
 print(" Disco Rigido: ", linha[7])


""" Vendo os resultados da aplicação das configurações do Counter Strike no banco de dados (Ignorar)"""
sql2 = ("SELECT * FROM csconfig")
cursor.execute(sql2)
resultadosCs = cursor.fetchall()
for linhaCs in resultadosCs:
  print(" SO1:", linhaCs[0])
  print(" Frequencia do Cpu: ", linhaCs[1])
  print(" Cores do cpu: ", linhaCs[2])
  print(" Memoria", linhaCs[3], "GB")
  print("Disco: ", linhaCs[4], "GB" )

  
sql3 = ("SELECT * FROM lolconfig")
cursor.execute(sql3)
resultadosLOL = cursor.fetchall()
for linhaLOL in resultadosLOL:
    print("SISTEMA OPERACIONAL: ", linhaLOL[1])
    print("Frequencia do Processor: ", linhaLOL[2])
    print("Cores do Lol: ", linhaLOL[3])
    print("Memoria Ram: ", linhaLOL[4])
    print("Disco Rígido: ", linhaLOL[5])
  
sql4 = ("SELECT * FROM rdrconfig")
cursor.execute(sql4)
resultadosRDR = cursor.fetchall()
for linhaRDR in resultadosRDR:
    print("SISTEMA OPERACIONAL: ", linhaRDR[0])
    print("Frequencia do Processor: ", linhaRDR[1])
    print("Cores do Lol: ", linhaRDR[2])
    print("Memoria Ram: ", linhaRDR[3])
    print("Disco Rígido: ", linhaRDR[4])

"""bom aqui eu fiz um teste para analisar se era possivel comparar valores que estão dentro do banco com valores 
 determinados aqui no python"""

"""
 if linha[1] == SO1:
     print('deu bom fml')
    
 if linha[1] >= SOCS:
    print('Sistema operacional: ok')
   
 if linha[4] >= corescpu:
     print('cores ok')
    
else:
        print('cores status: menor que requisitado')
        
if linha[5] >= processador:
      print("cpu: ok")      
    
else: 
    print("frequencia de cpu menor do que dos requisitos minimos")
   
if linha[6] >= memoria:
    print("memoria: ok")
    
else:
    print("Memoria não é o suficiente para o aplicativo")
if linha[7] >= discorigido:
    print("Disco rígido: ok")
else:
    print("Quantidade no disco rigido menor que preciso")
"""
banco.commit()
cursor.close()
banco.close()