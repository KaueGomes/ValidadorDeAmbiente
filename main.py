#Autor: Kaue Gomes
#Date: 30-09-2020

print('Carregando Dependencias\n')
from Sistema import *
from Registros import *
from Serviços import *
from Compara import *
print('Iniciando coleta do Sistema\n')
InfoSistema()
print('Iniciando coleta dos Frameworks\n')
InfoFramework()
#print('Iniciando coleta dos Navegadores\n')
#InfoNavegadores()
print('Iniciando coleta do FireBird\n')
InfoFirebird()
print('Iniciando coleta das Opçoes da Internet\n')
InfoInternet()
print('Iniciando coleta do Firewall\n')
InfoFirewall()
print('Iniciando comparação do sistema\n')
#ChamaCompara()