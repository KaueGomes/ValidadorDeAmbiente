#Autor: Kaue Gomes
#Date: 30-09-2020

####################################################################
#Sistema
#Cria um txt com as informações do sistema
def InfoSistema():
   import os
   import wmi
   os.system('systeminfo >> Sistema.txt')
   f=open('Sistema.txt','a+')
   f.write('\n')
   f.write('\nLink da base com os requisitos para configuração de hardware - Servidor e Estação:\n https://fagrontechnologiesbc.zendesk.com/hc/pt-br/articles/360001090627\n')
   f.write('\n------------------------------------\n')

   #Coleta o nome do sistema operacional para validar se está homologado ou não
   computer = wmi.WMI()
   os_info = computer.Win32_OperatingSystem()[0]
   sistema = os_info.Name.split('|')[0]

   def TestaSistema(OS):
      Homologados=['Microsoft Windows Server 2012 R2 Standard','Windows Server 2008 R2 Enterprise','Windows Server 2008 R2 Standard',
      'Microsoft Windows 10 Professional','Microsoft Windows 8.1 Professional','Microsoft Windows 8.1 Enterprise']
      for item in Homologados:
         if (OS == item):
               return True
               break

   if TestaSistema(sistema) == True:
      f.write('\n'+sistema + ' - O sistema é homologado\n')
   else:
      f.write('\n'+sistema + ' - O sistema não é homologado\n')
   f.write('\nLink da base para os sistemas operacionais homologados e configuração da rede:\n https://fagrontechnologiesbc.zendesk.com/hc/pt-br/articles/360001090687\n')
   f.write('\n------------------------------------\n')
   f.close

####################################################################
#Firewall
#portas verificadas
def InfoFirewall():
   import socket
   listaPortas = [17,20,21,80,443,475,587,1947,3050,5938,6001,6002,9443,35977]
   listaIp='40.123.34.23'

   #função para checar as portas
   #timeout pode variar de 1 a 3
   def isOpen(ip,port):
      print('Testando porta ' + str(port) + ' do firewall. . .') #Para teste
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(2)
      try:
         s.connect((ip, int(port)))
         s.shutdown(socket.SHUT_RDWR)
         return True
      except:
         return False
      finally:
         s.close()

   #looping para a checagem das portas
   f=open('Sistema.txt','a+')
   f.write('\nPortas abertas no firewall \n')
   for i in listaPortas:
       if isOpen(listaIp,i):
           f.write('porta ' + str(i) + ' [ ]aberta\n')
       else:
           f.write('porta '+ str(i) + ' [x]fechada\n')
   f.write('\n')
   f.write('\nLink da base com as portas do firewall, opções da internet e antivirus:\nhttps://fagrontechnologiesbc.zendesk.com/hc/pt-br/articles/360001091027\n')
   f.write('\n------------------------------------\n')
   f.close

