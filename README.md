# 🗂️ TkBackupDrive
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6F61?style=flat&logo=python&logoColor=white)
![Google Drive API](https://img.shields.io/badge/Google%20Drive%20API-4285F4?style=flat&logo=google-drive&logoColor=white)

**TkBackupDrive** é um utilitário simples de **backup automatizado com interface gráfica**, feito em Python com `Tkinter` e integração com a **API do Google Drive**.

Foi pensado para facilitar o envio de pastas locais — no meu contexto, backup de sistema contabil — diretamente para o Google Drive, com nomeação automática por **data e hora**.

---

## 🔧 Tecnologias utilizadas

- **Python 3**
- **Tkinter** (interface gráfica)
- **Google Drive API**
- **google-auth**, **google-api-python-client**
- **datetime**, **os**

---

## 📁 Estrutura do Projeto

```plaintext
TkBackupDrive/
├── main.py           # ponto de entrada (interface + inicialização)
├── desin.py          # tela de login e controle da interface
├── mario3.py         # autenticação + upload para o Drive
├── logo.png          # imagem exibida na janela
├── token.json        # token gerado após autenticação
├── credentials.json  # arquivo de credenciais da API
└── pycache/
```


---

## 🧠 Como funciona

### 🔐 Autenticação

- Tela de login simples (`admin` / `senha123`);
- Após o login, o usuário é questionado se deseja realizar o backup.

### ☁️ Upload para o Google Drive

- O programa acessa a pasta definida (`C:\Mario Monteiro\MM`);
- Cria automaticamente uma pasta no Drive nomeado com a data e hora da realização do backup `Backup_YYYY-MM-DD_HH-MM-SS`;
- Faz upload de todos os arquivos e subpastas usando a **Google Drive API**.

---

## ▶️ Como rodar o projeto

### 1. Instale as dependências:

-pip install google-api-python-client google-auth google-auth-oauthlib

### 2. rode o arquivo "main.py".

---

## ⚠️ Observações 
o caminho da pasta está fixo no código (C:\Mario Monteiro\MM). Edite os arquivos "desin.py" e "main.py" para apontar para o diretório desejado.

Este projeto foi descontinuado após testes, devido a algumas limitações:

- Tkinter se mostrou pouco prático para empacotar e distribuir em outras máquinas;
- Ferramentas de empacotamento (como pyinstaller) não funcionaram bem com dependências como a Google API;
- O processo de backup, mesmo com arquivos pequenos (~250MB), levava cerca de 4 a 5 horas para concluir.

Após identificar as limitações a cima, busquei outras ferramentas e dei continuidade ao [projeto usando **C#**](https://github.com/Nathan-Dev-udia/BackupDriveCSharp) e obtive excelentes resultados!

Mesmo assim, o projeto serviu como prova de conceito e aprendizado sobre:

- Integração com Google Drive via API;
- Interface gráfica com Tkinter;
- Criação de ferramentas internas para automação de rotina.  

> Projeto criado por Nathan Fernandes Alves para automatizar backups locais com envio direto ao Google Drive.
