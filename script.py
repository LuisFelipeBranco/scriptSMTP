#!/usr/bin/python3.6
import gmail, time, os

def main():
    srv = gmail.GMail('Username do Gmail', 'Senha do Gmail')
    att1 = 'nome do anexo(opcional) ou caminho do anexo'
    exist = os.path.exists(att1) # verifica se o anexo existe (opcional);

    if exist == False:#anexo não existe;
        warning = gmail.Message('Título do e-mail', to='destinatario@domain.com', text='Texto do e-mail')
        srv.send(warning)

    else:#anexo existe;
        msg = gmail.Message('Título do e-mail', to='destinatario@domain.com', text='Texto do e-mail', attachments=[att1])
        srv.send(msg)
        delArchive()#procedimento para deletar o anexo(opcional);

def delArchive(): #deleta os arquivos que foram enviados por anexo;
    for raiz, diretorio, arquivos in os.walk('caminho do anexo'):
        for arquivo in arquivos:
            if arquivo.endswith('.cfg'):
                os.remove(os.path.join(raiz, arquivo))

if __name__ == "__main__":
    main()