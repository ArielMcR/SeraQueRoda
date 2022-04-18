from distutils.log import error
from doctest import testfile
from os import sep
from pyexpat import model
import pandas as pd
from IPython.display import display
import cpuinfo


#Pegando o nome do processador
nomeProcessador = cpuinfo.get_cpu_info()['brand_raw']
a,b,c,d = nomeProcessador.split(' ', 3)
# Tirando o (TM) do core pois na nossa base dados esta listado sem o TM
b = b
characters = "(TM)"
b = ''.join( x for x in b if x not in characters)
# Somando as String para termos um resultado como Core é o processador
D = b + ' ' + c

# Lendo o csv
df = pd.read_csv(r'C:\Users\User\vs\Exec\CPU_UserBenchmarks4.csv', sep = ";", encoding= "UTF-8")
#print(nomeProcessador.split(' ', 3))
#print(nomeProcessador)~
#print(D)
#Apresentado a linha onde o model é igual o nome do nosso processador
apresenta = df.loc[df['Model'] == D, 'Benchmark']


if (apresenta.astype(int) >= 50):
    display(apresenta)
else:
    display('Vasco Gigante')
#teste
#cpuben = df.loc[df['Model'] == D ]

