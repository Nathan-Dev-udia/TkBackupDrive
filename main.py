from desin import iniciar_interface
from mario3 import autenticar_google_drive, upload_pasta_para_drive
import sys
import os

def recurso_absoluto(caminho_relativo):
    """Resolve o caminho correto do recurso, seja no executável ou no ambiente local."""
    if hasattr(sys, '_MEIPASS'):  # _MEIPASS é o diretório temporário usado pelo PyInstaller
        return os.path.join(sys._MEIPASS, caminho_relativo)
    return os.path.join(os.path.abspath("."), caminho_relativo)

# Exemplo de como usar
logo_path = recurso_absoluto("logo.png")
credentials_path = recurso_absoluto("credentials.json")
token_path = recurso_absoluto("token.json")

def main():
    # Inicia a interface gráfica
    iniciar_interface()

if __name__ == "__main__":
    main()