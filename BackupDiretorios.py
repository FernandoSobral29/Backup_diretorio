import os
import shutil
import datetime
import glob

def BackupDiretorios(Origem, Destino): 
    #Variáveis para armazenar o caminho de origem e destino dos arquivos.
    Origem = Origem
    Destino = Destino

    #CRIA O DIRETÓRIO SE  CASO NÃO EXISTA.
    if not os.path.exists(Destino):
        os.makedirs(Destino)

    #LISTA O QUE TEM NO DIRETÓRIO DE ORIGEM.
    files = os.listdir(Origem)

    #Iterando sobre todos os arquivos que estão no diretório fonte.
    for fname in files:
        fnameDestino = glob.glob(os.path.join(Destino, f"*{fname}*")) #filtra os arquivos que contem que contém nome igual em origem e destino.
        try:
            os.chdir(Destino) #lista o que tem no diretório destino.
            if fnameDestino: #Caso os arquivos do destino existam, execute as regras abaixo.

                #Verifica se a data e hora de criação/modificação dos arquivos de origem, são maiores que os de destino.
                #se for, ele remove os arquivos mais antigos de backup, e copia novamente atualizados.
                if os.path.getmtime(os.path.join(Origem, fname)) > os.path.getmtime(os.path.join(Destino, fnameDestino[0])):
                    os.remove(os.path.join(Destino, fnameDestino[0]))
                    
                    #pega data e hora atual, entra no diretório, copia todos os arquivos do diretório Origem para o de Destino.
                    data_hora_atual = datetime.datetime.now()
                    os.chdir(Destino) #Acessa o diretório de destino.
                    #Copia os arquivos dentro do diretório de origem, para o destino.
                    shutil.copy2(os.path.join(Origem,fname), Destino) 
                    
                    #Renomeia os arquivos para o padrão de nome de backup com data e hora do backup no final.
                    os.rename (f"{fname}", f"backup_{fname}-{data_hora_atual.strftime('%Y%m%d')}") #Somente a data, retirada a hora %H%M%S.
                else:
                    print(f"O arquivo {fname} não foi modificado") #Se não tiver modificação mais recente no arquivo, ele só informa.
            else:
                #Conforme o primeiro IF, se o diretório estiver vazio, ou não existir, ele cria a pasta e realiza o backup.
                os.chdir(Destino)
                data_hora_atual = datetime.datetime.now()
                shutil.copy2(os.path.join(Origem,fname), Destino)
                os.rename (f"{fname}", f"backup_{fname}-{data_hora_atual.strftime('%Y%m%d')}") #Somente a data, retirada a hora %H%M%S.

#Log de erros
        except OSError as e:
            print(f"Error:{ e.strerror}")

#Chamando as funções especificando os valores das váriaveis de Origem e Destino do código de Backup acima (Você pode fazer de quantos diretórios precisar, basta chamar a função e informar o diretório de origem e de destino, para que ele faça o backup na origem e envie para o diretório de destino que você deseja)
BackupDiretorios('/diretorio/origem', '/diretorio/destino')
BackupDiretorios('/diretorio/origem/1', '/diretorio/destino')
BackupDiretorios('/diretorio/origem/2', '/diretorio/destino')
BackupDiretorios('/diretorio/origem/3', '/diretorio/destino')
