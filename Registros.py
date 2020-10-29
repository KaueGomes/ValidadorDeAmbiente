#Autor: Kaue Gomes
#Date: 30-09-2020

def InfoInternet():
    import winreg
    from winreg import OpenKey
    from winreg import HKEY_CURRENT_USER
    from winreg import KEY_ALL_ACCESS
    from winreg import CloseKey
    f=open("Sistema.txt","a+")
    #Validação dos Https nas opções da internet
    print('insira o nome da farmacia para a verificação das Opções da Internet')
    nomefarmacia = input()
    PathsCurrentUser=["Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fagrontech.com.br\\www\\",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fagrontechnologies.com.br\\www",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fagrontech.com.br\\api-contrato",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fagrontechnologies.com.br\\ftp",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fagrontechnologies.com.br\\backupdb01",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fagrontech.com.br\\formulacertaprod",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fagrontech.com.br\\formulacertaprodv2",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\azurewebsites.net\\formulacertaprod",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\azurewebsites.net\\formulacertaprodv2",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fidelimax.com.br\\api",
    ("Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fidelimax.com.br\\"+ nomefarmacia),
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\pharmanostra.com.br\\shop",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\viafarmanet.com.br\\shop",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fagron.com.br\\shop",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\florien.com.br\\shop",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\organicbr.com.br\\shop",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\message.moby\\fate",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\whatsapp.com\\web",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\whatsapp.com\\*.web",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\Domains\\whatsapp.net",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\rnp.br\\ntp.cais",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\sp.gov.br\\wssathomolog.fazenda",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\sp.gov.br\\wssatnacional.fazenda",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\sp.gov.br\\wssatsp.fazenda",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\sp.gov.br\\www.fazenda",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\fazenda.gov.br\\www.nfe",
    "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\saude.gov.br\\aplicacao"]
    listaHttp = ['https://www.fagrontech.com.br','https://www.fagrontechnologies.com.br',
    'http://api-contrato.fagrontech.com.br','ftp.fagrontechnologies.com.br','backupdb01.fagrontechnologies.com.br',
    'https://formulacertaprod.fagrontech.com.br','https://formulacertaprodv2.fagrontech.com.br','https://formulacertaprod.azurewebsites.net/',
    'https://formulacertaprodv2.azurewebsites.net/','https://api.fidelimax.com.br/',('https://'+nomefarmacia+'.fidelimax.com.br'),
    'https://shop.pharmanostra.com.br/api','https://shop.viafarmanet.com.br/api','https://shop.fagron.com.br/api',
    'https://shop.florien.com.br/api','https://shop.organicbr.com.br/api','http://fate.message.moby',
    'https://web.whatsapp.com/','*.web.whatsapp.com','*.whatsapp.net',
    'http://ntp.cais.rnp.br/','https://wssathomolog.fazenda.sp.gov.br/','https://wssatnacional.fazenda.sp.gov.br/',
    'https://wssatsp.fazenda.sp.gov.br/','http://www.fazenda.sp.gov.br/sat/','http://www.nfe.fazenda.gov.br/','https://aplicacao.saude.gov.br/portalfarmacia']


    def CheckHttp():
        count = 0
        for i in PathsCurrentUser:
            try:
                Chave=winreg.OpenKey(winreg.HKEY_CURRENT_USER, i)
                parentKey = winreg.QueryInfoKey(Chave)
                if parentKey != None:
                    f.write(listaHttp[count] + ' - Encontrado\n')
                winreg.CloseKey(Chave)
                count = count + 1
            except:
                f.write(listaHttp[count] + ' - Não encontrado\n')
                count = count + 1

    ##################################################################################################
    #Validação dos IPs nas Opções da Internet
    #Lista dos ips utilizados hoje na fagron
    listaIp = ['189.39.10.65','189.39.10.66','189.39.10.67','189.39.10.68','189.39.10.69','189.39.10.70',
    '189.39.10.71','189.39.10.72','189.39.10.73','189.39.10.74','189.39.10.75','189.39.10.76','189.39.10.77',
    '189.39.10.78','40.123.34.23','200.147.36.31','189.28.128.37']
    sucess=[]

    def CheckIp(path,ip):
        try:
            t = OpenKey(HKEY_CURRENT_USER, path , 0, KEY_ALL_ACCESS)
            count = 0
            while 1:
                name, value, type = winreg.EnumValue(t, count)
                count = count + 1
                if (str(name) == ':Range') and (str(value) == ip):
                    t = CloseKey
                    return True
                    break
        except WindowsError:
            return False

    CheckHttp()

    #range escolhe quantas pastas serão verificadas para validar os arquivos com ip informado
    for x in range(1,31):
        for i in listaIp:
                listaPath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Ranges\\Range"+str(x)
                if CheckIp(listaPath,i) == True:
                    sucess.append(i)
                    f.write(i + " - Encontrado\n")
    p = [item for item in listaIp if item not in sucess]
    for item in p:
        f.write(item + " - Não encontrado\n")
    f.write("\n-------------------------------------------------\n")
    f.close

##################################################################################################
#Verifica a versão do Framework e se esta instalado via registros
def InfoFramework():
    
    from winreg import ConnectRegistry
    from winreg import HKEY_LOCAL_MACHINE
    from winreg import OpenKey
    from winreg import CloseKey
    from winreg import EnumValue

    PathFrameworks = ['Software\\Microsoft\\NET Framework Setup\\NDP\\v2.0.50727',
        'Software\\Microsoft\\NET Framework Setup\\NDP\\v3.0',
        'Software\\Microsoft\\NET Framework Setup\\NDP\\v3.5',
        'Software\\Microsoft\\NET Framework Setup\\NDP\\v4\\Client',
        'Software\\Microsoft\\NET Framework Setup\\NDP\\v4\\Full']
    Versoes = ['Net Framework 2.0','Net Framework 3.0','Net Framework 3.5','Net Framework 4.0 Client','Net Framework 4.0 Full']

    def SearchRegistry(item):
        try:
            Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            RawKey = OpenKey(Registry, item)
            i = 0
            while 1:
                name, value, type = EnumValue(RawKey, i)
                #print("name:",name,"value:", value,"i:", i)
                i += 1
                if (name == 'Install') and (value == 1):
                    return True
        except WindowsError:
            return False


    f=open("Sistema.txt","a+")
    cont = 0
    for item in PathFrameworks:
            if SearchRegistry(item) == True:
                f.write('Encontrado - ' + Versoes[cont] + '\n')
                cont=cont+1
            elif SearchRegistry(item) == False:
                print('Não encontrado ' + Versoes[cont] + '\n')
                cont=cont+1

    f.write("\n-------------------------------------------------\n")
    f.close

##################################################################################################
#Verifica a versão do Internet Explorer e Google Chrome
def InfoNavegadores():
    from winreg import ConnectRegistry
    from winreg import HKEY_LOCAL_MACHINE
    from winreg import OpenKey
    from winreg import CloseKey
    from winreg import EnumValue
    from winreg import HKEY_CURRENT_USER

    def CheckIExplorer():
        try:
            Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            RawKey = OpenKey(Registry, 'SOFTWARE\\Microsoft\\Internet Explorer')
            i = 0
            while 1:
                name, value, type = EnumValue(RawKey, i)
                #print("name:",name,"value:", value,"i:", i)
                i += 1
                if (name == 'svcVersion'):
                    return value
        except WindowsError:
            return False
    
    def CheckChrome():
        try:
            Registry = ConnectRegistry(None, HKEY_CURRENT_USER)
            RawKey = OpenKey(Registry, 'SOFTWARE\\Google\\Chrome\\BLBeacon')
            i = 0
            while 1:
                name, value, type = EnumValue(RawKey, i)
                #print("name:",name,"value:", value,"i:", i)
                i += 1
                if (name == 'version'):
                    return value
        except WindowsError:
            return False

    f=open("Sistema.txt","a+")
    f.write('Versão do Internet Explorer - ' + CheckIExplorer() + '\n')
    f.write("\n")
    f.write('Versão do Google Chrome - ' + CheckChrome() + '\n')
    f.write("\n-------------------------------------------------\n")
    f.close

    