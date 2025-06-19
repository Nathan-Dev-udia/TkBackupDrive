import os
from tkinter import *
import mario3  # Para importar o arquivo do backend

# Cores definidas
cor1 = '#2e2c28'  # cinza brutus
cor2 = '#f0f0f0'  # cor clara para os campos

# Função de autenticação (substitua por sua lógica real)
def autenticar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    # Aqui você pode adicionar sua lógica de autenticação
    if usuario == 'admin' and senha == 'senha123':
        label_status.config(text="Autenticação bem-sucedida!", fg='green')
        abrir_janela_backup()
    else:
        label_status.config(text="Usuário ou senha incorretos", fg='red')

# Função para abrir a janela de backup
def abrir_janela_backup():
    # Oculta a janela de autenticação
    janela.withdraw()

    # Cria a janela de backup
    janela_backup = Toplevel()
    janela_backup.title('Backup')
    janela_backup.geometry('400x200')
    janela_backup.config(bg=cor1)
    
    label_backup = Label(janela_backup, text="Gostaria de realizar o backup?", font=("Arial", 14), bg=cor1, fg=cor2)
    label_backup.pack(pady=10)
    
    botao_sim = Button(janela_backup, text="Sim", command=lambda: iniciar_upload(janela_backup), bg='#4CAF50', fg='white', font=("Arial", 12))
    botao_sim.pack(side=LEFT, padx=50, pady=20)
    
    botao_nao = Button(janela_backup, text="Não", command=janela_backup.destroy, bg='#F44336', fg='white', font=("Arial", 12))
    botao_nao.pack(side=RIGHT, padx=50, pady=20)

# Função para iniciar o upload e exibir "Aguarde..."
def iniciar_upload(janela_backup):
    # Exibe a mensagem "Aguarde..."
    label_aguarde = Label(janela_backup, text="Aguarde...", font=("Arial", 12), bg=cor1, fg='yellow')
    label_aguarde.pack(pady=10)
    
    # Atualiza a interface para mostrar a mensagem "Aguarde..."
    janela_backup.update_idletasks()  # Garante que o layout seja atualizado imediatamente

    # Desativa os botões para evitar múltiplos cliques
    for widget in janela_backup.winfo_children():
        widget.config(state=DISABLED)

    caminho_pasta_teste = r'D:\pogramacao\teste'  # Substitua com o caminho correto da sua pasta

    if not os.path.exists(caminho_pasta_teste):
        print(f"A pasta '{caminho_pasta_teste}' não existe.")
        return

    # ID da pasta no Google Drive onde será feito o upload (pasta de destino)
    id_pasta_pai = '1lseshNQjmUaL-uLLXgGx7QDHFu3lozUH'

    # Chama a função do backend para autenticar no Google Drive e fazer o upload para a pasta correta
    service = mario3.autenticar_google_drive()
    mario3.upload_pasta_para_drive(service, caminho_pasta_teste, id_pasta_pai)
    
    # Após o upload, atualiza a mensagem para "Concluído!"
    label_aguarde.config(text="Concluído!")
    janela_backup.update_idletasks()  # Atualiza o layout para garantir que "Concluído!" seja mostrado
    
    # Fecha a janela após 3 segundos
    janela_backup.after(3000, janela_backup.destroy)
    
    # Finaliza a aplicação, fechando todas as janelas abertas
    janela_backup.after(3000, janela.quit())

# Criação da janela
janela = Tk()
janela.title('Tela de Autenticação')
janela.geometry('600x250')
janela.config(bg=cor1)

# Ícone da janela (substitua com o caminho correto)
janela.iconphoto(False, PhotoImage(file='logo.png'))

# Rótulo para o título
label_titulo = Label(janela, text="Autenticação", font=("Arial", 20), bg=cor1, fg=cor2)
label_titulo.pack(pady=10)

# Rótulos e campos de entrada (usuario e senha)
label_usuario = Label(janela, text="Usuário", font=("Arial", 12), bg=cor1, fg=cor2)
label_usuario.pack(pady=5)

entry_usuario = Entry(janela, font=("Arial", 12))
entry_usuario.pack(pady=5)

label_senha = Label(janela, text="Senha", font=("Arial", 12), bg=cor1, fg=cor2)
label_senha.pack(pady=5)

entry_senha = Entry(janela, show="*", font=("Arial", 12))
entry_senha.pack(pady=5)

# Botão de autenticação
botao_autenticar = Button(janela, text="Autenticar", command=autenticar, bg='#4CAF50', fg='white', font=("Arial", 12))
botao_autenticar.pack(pady=20)

# Rótulo para exibir o status
label_status = Label(janela, text="", font=("Arial", 12), bg=cor1)
label_status.pack()

# Iniciar a interface
janela.mainloop()
