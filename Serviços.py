#Autor: Kaue Gomes
#Date: 06-10-2020

def InfoFirebird():
    import psutil

    firebird = ['FirebirdServerDefaultInstance','FirebirdGuardianDefaultInstance']
    SuperBird = False

    f=open('Sistema.txt','a+')
    for item in firebird:
        try:
            servico = psutil.win_service_get(item)
            conteudo = servico.as_dict()
            f.write(conteudo['name'] + ' - ' + conteudo['status'] + '\n')
            if (conteudo['name'] == 'FirebirdGuardianDefaultInstance'):
                SuperBird = True
        except:
            f.write(item + ' - Serviço não encontrado' + '\n')
    f.write('\n')
    if SuperBird == True:
        f.write('Está instalado o Firebird Server\n')
    elif SuperBird == False:
        f.write('Está instalado o Firebird Client\n')
    f.write('\n')
    f.write('Link dos Softwares Obrigatórios:\nhttps://fagrontechnologiesbc.zendesk.com/hc/pt-br/articles/360001090807\n')
    f.write('---------------------------------\n')
    f.close

###############################################################
#Hardlock
