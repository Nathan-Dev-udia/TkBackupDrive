import os
import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Função para autenticar no Google Drive
def autenticar_google_drive():
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    creds = None
    
    # Verifica se o token existe e está válido
    if os.path.exists('token.json'):
        try:
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        except Exception as e:
            print("Erro ao carregar o token. Gerando um novo...")

            creds = None

    # Se não houver credenciais ou forem inválidas, gera um novo token
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Salva o token no arquivo 'token.json' para reutilização
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

# Função para fazer o upload de arquivos e pastas para o Google Drive
def upload_pasta_para_drive(service, pasta_local, id_pasta_pai=None, nome_pasta=None):
    # Se o nome da pasta não for passado, cria com a data e hora atual
    if not nome_pasta:
        nome_pasta = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Cria a pasta no Google Drive dentro da pasta pai especificada
    folder_metadata = {
        'name': nome_pasta,  # Usando o nome gerado com data e hora
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [id_pasta_pai] if id_pasta_pai else None  # Aqui é onde o ID da pasta pai é usado
    }
    pasta_drive = service.files().create(body=folder_metadata, fields='id').execute()
    id_pasta_drive = pasta_drive.get('id')

    # Faz o upload de cada arquivo/pasta
    for item in os.listdir(pasta_local):
        caminho_item = os.path.join(pasta_local, item)
        if os.path.isfile(caminho_item):
            file_metadata = {'name': item, 'parents': [id_pasta_drive]}
            media = MediaFileUpload(caminho_item, resumable=True)
            service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f"Arquivo enviado: {item}")
        elif os.path.isdir(caminho_item):
            upload_pasta_para_drive(service, caminho_item, id_pasta_drive, nome_pasta)

# Função principal (não será chamada diretamente pelo frontend, mas serve para a execução completa)
def main():
    # Caminho fixo da pasta
    caminho_pasta_teste = r'C:\Mario Monteiro\MM'  # Atualize para o seu caminho de pasta

    if not os.path.exists(caminho_pasta_teste):
        print(f"A pasta '{caminho_pasta_teste}' não existe.")
        return

    # Autenticar no Google Drive
    print("Autenticando no Google Drive...")
    service = autenticar_google_drive()

    # ID da pasta onde os arquivos serão enviados (ID da pasta no link fornecido)
    id_pasta_pai = '1lseshNQjmUaL-uLLXgGx7QDHFu3lozUH'

    # Fazer o upload da pasta "teste" com o nome gerado automaticamente dentro da pasta específica
    print(f"Enviando arquivos da pasta '{caminho_pasta_teste}' para o Google Drive...")
    upload_pasta_para_drive(service, caminho_pasta_teste, id_pasta_pai, nome_pasta="Backup_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    print("Upload concluído com sucesso!")

# Caso o script seja executado diretamente (para testes)
if __name__ == '__main__':
    main()
